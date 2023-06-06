#!/usr/bin/env python3 

#import subprocess
import scapy.all as scapy
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
    #url = curl -X POST -H "Content-Type: application/json" -d '{ "command": "config-get", "service": [ "dhcp4" ] }' http://127.0.0.1:8000/
    #url = "http://127.0.0.1:8000/"
    #payload = { "command": "config-get", "service": [ "dhcp4" ] }
    #headers = {'Content-Type': 'application/json'}
    #response_data = requests.post(url, data=payload, headers=headers)
    #response_data = response.content.decode('utf-8').splitlines()
    #print(response_data)
    #return response_data
    url = "http://127.0.0.1:8000/"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"command": "config-get", "service": [ "dhcp4" ] }'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.json)
    return resp

def get_ReservedMacAddress(ip): # Troubleshooting code, proof of concept of an IPAM Database, replace with sqlite3 database synced to DHCP reserved scope 
    ipam_db_dict = {
        ## Proof of concept in lue of sqlite3 in-memory database
        "192.168.2.1": "00:50:56:01:65:6f",
        "192.168.2.2": "00:50:56:01:7a:cd",
        "192.168.2.3": "00:50:56:01:7a:c3",
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
    
