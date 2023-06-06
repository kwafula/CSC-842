#!/usr/bin/env python3 

#import subprocess
import scapy.all as scapy
import csv
import json
import argparse
import sqlite3
import requests
from requests.structures import CaseInsensitiveDict
#import time
#import sys
#import netifaces
#import time
#from datetime import datetime

# Create menu arguments here

# Initialize SQLLite IP Address Management (IPAM) database - In memory database for authoritative IP Address to MAC Address mappings
def init_ipam_db():
  
    ## Pontentia Additional Fields ###
    ### AlertDate text, AlertMsg text, EthIIType text, ARPMsgOpCode int, ARPMsgIsGrat BOOLEAN, EthIISrcMAC text, EthIIDstMAC text, ARPMsgSrcMAC text, 
    ### ARPMsgDstMAC text, 
    ### ARPMsgSrcIP text, 
    ### ARPMsgDstIP text
    db = sqlite3.connect(':memory:')
    cur = db.cursor()
    cur.execute( 'CREATE TABLE ipam_db_reservations ( reserved_ip text, mac_address text ) ')
    db.commit()
    return db

# Read IP Address reservation from Windows DHCP Reserved Scope for the protected subnet - All IP Addresses are issue by means of reservation only as security measure

# Populate the IPAM Database with authoritative IP Address to MAC address reservations from Windows DHCP Server 

# Read packets on the protected subnet promiscously and filter for arp messages

# Compare IP/MAC association in ARP Op Code 1/ARP Requests and Op Code 2/ARP Responses againts authorititive IPAM Database and enumarate inconsistencies

# Optionally do checks i.e. Ping etc.

# Create notification message templates for Op Code 1 violations and Op Code 2 violations

# Raise Alarm (1) Write messag to log (2) print on screen (3) send email (4) post on Slack (5) log to graylog)

# Add script exit code and usage menu
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest = "interface", default = "ens32", help = "Monitored Interface")
    args = parser.parse_args()
    return args

def get_ipAddress_reservations():
    ##### option 1: Read raw reservations in the dhcp config file
    """
    url = "http://127.0.0.1:8000/"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"command": "config-get", "service": [ "dhcp4" ] }'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.json())
    ####### Now parse and retrieve the data ## code need fixing, parsing and getting values
    json_resp = resp.json()
    #json_data = json.load(json_resp)
    #reservations = json_resp["reservations"]
    reservations = json_resp[0][10][3]
    reservations_dict = {}  
    for dict in reservations:
        for key, val in dict.items():
            #keys = x.keys()
            #values = x.values()
            #reservations_dict[values] = keys
            reservations_dict[val] = key
    print(reservations_dict)
    #for x in reservations:
        #keys = x.keys()
        #print(keys)
        #values = x.values()
        #print("IP Address: {0} | MAC Address: {1}".format(values, keys)) 
    """   
    ##### Option 2: Read active leases
    reservations_dict = {} 
    csvfile = open('/var/lib/kea/kea-leases4.csv', 'r')
    #jsonfile = open('/var/lib/kea/kea-leases4.json', 'w', encoding='utf-8')

    fieldnames = ("address", "hwaddr", "client_id", "valid_lifetime", "expire", "subnet_id", "fqdn_fwd", "fqdn_rev", "hostname", "state", "user_context")
    reader = csv.DictReader( csvfile) # without headers
    # reader = csv.DictReader( csvfile, fieldnames) # with headers
    json_data = json.dumps(list(reader))
    #print(json_data)
    with open('/var/lib/kea/kea-leases4.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    with open("/var/lib/kea/kea-leases4.json", 'r', encoding='utf-8') as active_leases:
        try:
            lease_data = json.load(active_leases)
            print(type(lease_data))
            print(lease_data)
            json_lease_dict = json.loads(lease_data)
            for dict in json_lease_dict:
                for key, val in dict.items():
                    reservations_dict[key] = val
                print(type(reservations_dict))
                print(reservations_dict)
        except json.JSONDecodeError:
            print("kea-lease4.json file is empty")
    return reservations_dict

def get_ReservedMacAddress(ip): # Troubleshooting code, proof of concept of an IPAM Database, replace with sqlite3 database synced to DHCP reserved scope 
    ipam_db_dict = {
        ## Proof of concept in lue of sqlite3 in-memory database
        "192.168.2.1": "00:50:56:01:65:6f",
        "192.168.2.2": "00:50:56:01:7a:cd",
        "192.168.2.3": "00:50:56:01:7a:ce",
        "192.168.2.4": "00:50:56:01:58:78"
    }
    #print(ipam_db_dict)
    reserved_mac_address = ipam_db_dict[ip]
    return reserved_mac_address 

def process_sniffed_packet(packet):
    db = sqlite3.connect(':memory:')
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2: # ARP Requests and ARP Replies only
        try:
            print("----------------------------------------------------------------------------------------------------------")
            ethHeader_SourceMacAddress = packet[scapy.Ether].src
            print("[+] ARP Response Ethernet Header Sender MAC Address: {0}".format(ethHeader_SourceMacAddress))
            print("---------------------------------------------------------")
            
            ethHeader_DestinationMacAddress = packet[scapy.Ether].dst
            print("[+] ARP Response Ethernet Header Destination MAC Address: {0}".format(ethHeader_DestinationMacAddress))
            print("---------------------------------------------------------")
            
            ethPayload_SenderMacAddress = packet[scapy.ARP].hwsrc
            print("[+] ARP Response Ethernet Payload Sender MAC Address: {0}".format(ethPayload_SenderMacAddress))
            print("---------------------------------------------------------")
            
            ethPayload_SenderIPAddress = packet[scapy.ARP].psrc
            print("[+] ARP Response Ethernet Payload Sender IP Address: {0}".format(ethPayload_SenderIPAddress))
            print("---------------------------------------------------------")
            
            ethPayload_TargetMacAddress = packet[scapy.ARP].hwdst
            print("[+] ARP Response Ethernet Payload Target MAC Address: {0}".format(ethPayload_TargetMacAddress))
            print("---------------------------------------------------------")
            
            ethPayload_TargetIPAddress = packet[scapy.ARP].pdst
            print("[+] ARP Response Ethernet Payload Target IP Address: {0}".format(ethPayload_TargetIPAddress))
            print("---------------------------------------------------------")
            
            reservedMacAddress = get_ReservedMacAddress(ethPayload_SenderIPAddress)
            print("[+] IPAM/DHCP Lease Table | IP Address: {0} ==> MAC Addrress: {1}".format(ethPayload_SenderIPAddress,reservedMacAddress))
            #ip_to_mac_reservations = get_ipAddress_reservations()
            print("----------------------------------------------------------------------------------------------------------")
            
            if reservedMacAddress != ethPayload_SenderMacAddress:
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Poisoning Attack *{@ v @ }* Detectected !!!!")
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Payload IP Address: {0} Is Reserved And/Or Assigned To IPAM/DHCP MAC Address: {1}".format(ethPayload_SenderIPAddress, reservedMacAddress))
                print("[+] ARP Payload MAC Addrress: {0} Is A Spoof".format(ethPayload_SenderMacAddress))
                print("----------------------------------------------------------------------------------------------------------")
                print(" ")
            else:
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] No ARP Attacks Detectected")
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Payload IP Address: {0} Is Reserved And/Or Assigned To IPAM/DHCP MAC Address: {1}".format(ethPayload_SenderIPAddress, reservedMacAddress))
                print("[+] ARP Payload MAC Addrress: {0} Is Legit".format(ethPayload_SenderMacAddress))
                print("----------------------------------------------------------------------------------------------------------")
                print(" ")
        except IndexError:
            pass
        
if __name__ == '__main__':

    print("[+] Initializing IPAM Database")
    db = init_ipam_db()
    
    ip_to_mac_reservations = get_ipAddress_reservations()
    
    print("[+] Starting ARP Poisonin NIDS")    
    args = get_arguments()
    scapy.sniff(iface = args.interface, prn = process_sniffed_packet, store = 0)       # filter = "arp",
    print(" ")
    print("----------------------------------------------------------------------------------------------------------")
    
