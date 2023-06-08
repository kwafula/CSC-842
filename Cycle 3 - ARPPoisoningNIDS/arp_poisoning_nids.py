#!/usr/bin/env python3 

#import subprocess
import scapy.all as scapy
import csv
import json
import argparse
import sqlite3
import requests
from requests.structures import CaseInsensitiveDict
import time
#import sys
#import netifaces
from datetime import datetime

# Create menu arguments here

# Initialize SQLLite IP Address Management (IPAM) database - In memory database for authoritative IP Address to MAC Address mappings
def init_ipam_db():

    ## Pontentia Additional Fields ###
    ### AlertDate text, AlertMsg txt, EthIIType text, ARPMsgOpCode int, ARPMsgIsGrat BOOLEAN, EthIISrcMAC text, EthIIDstMAC text, ARPMsgSrcMAC text, 
    ### ARPMsgDstMAC text,
    ### ARPMsgSrcIP text,
    ### ARPMsgDstIP text
    db = sqlite3.connect(':memory:')
    cur = db.cursor()
    cur.execute( 'CREATE TABLE ipam_db_reservations(tbl_host_name text, tbl_reserved_ip text, tbl_mac_address text, tbl_lease_time int, tbl_lease_expire int, tbl_time_stamp int, tbl_timestamp_diff int)') 
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
    reservations_dict = {}
    
    ##### Option 1: ### Read Active IP Address Lease Reservations from Kea DHCP4 Server Config File (/etc/kea/kea-dhcp4.config) 
    """
    url = "http://127.0.0.1:8000/"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    data = '{"command": "config-get", "service": [ "dhcp4" ] }'
    resp = requests.post(url, headers=headers, data=data)
    print(resp.status_code)
    print(resp.json())
    ####### Add code to parse the config file getting values IP Address to MAC Address reservation mappings
    """
    
    ##### Option 2: ### Read Active IP Address Lease Reservations from Kea DHCP4 Server (/var/lib/kea/kea-leases4.csv)
    csvfile = open('/var/lib/kea/kea-leases4.csv', 'r')
    fieldnames = ("address", "hwaddr", "client_id", "valid_lifetime", "expire", "subnet_id", "fqdn_fwd", "fqdn_rev", "hostname", "state", "user_context")
    reader = csv.DictReader(csvfile) # without headers
    # reader = csv.DictReader( csvfile, fieldnames) # with headers
    json_data = json.dumps(list(reader))
    #print(json_data)
    
    with open('/var/lib/kea/kea-leases4.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)

    with open("/var/lib/kea/kea-leases4.json", 'r', encoding='utf-8') as active_leases:
        try:
            lease_data = json.load(active_leases)
            json_list_dict= json.loads(lease_data)
            print("")
            for item in json_list_dict:
                    print(item)
            print("")
            for dict in json_list_dict:
                host_name = dict["hostname"]
                reserved_ip = dict["address"]
                mac_address = dict["hwaddr"]
                lease_time = dict["valid_lifetime"]
                lease_expire = dict["expire"]
                cur = db.cursor()
                time_stamp = time.mktime(datetime.now().timetuple())
                timestamp_diff = float(lease_expire) - time_stamp
                print("")
                for x in range(0, 3):
                    cur.execute("SELECT tbl_mac_address FROM ipam_db_reservations WHERE tbl_reserved_ip = ? AND tbl_mac_address = ?", (reserved_ip, mac_address))
                    get_tbl_entry = cur.fetchone()
                    cur.execute("SELECT tbl_timestamp_diff FROM ipam_db_reservations WHERE tbl_reserved_ip = ? AND tbl_mac_address = ?", (reserved_ip, mac_address))
                    get_tbl_timestamp_diff = cur.fetchone()
                    check_tbl_entry = str(get_tbl_entry).replace("'",'').replace(",",'').replace("(",'').replace(")",'')
                    get_tbl_timestamp_diff = str(get_tbl_timestamp_diff).replace("'",'').replace(",",'').replace("(",'').replace(")",'')
                    timestamp_diff_int = int(timestamp_diff)
                    print(timestamp_diff_int)
                    print(get_tbl_timestamp_diff)
                    print("ARP Respone MAC Addr: {0}  | IPAM Database Entry: {1} ".format(mac_address, check_tbl_entry))
                    print("")
                    if ((mac_address == check_tbl_entry)): # ) and (float(timestamp_diff) >= get_tbl_timestamp_diff 
                        update_query = """UPDATE ipam_db_reservations SET tbl_host_name = ?, tbl_reserved_ip = ?, tbl_mac_address = ?, tbl_lease_time = ?, tbl_lease_expire = ?, tbl_time_stamp = ?, tbl_timestamp_diff = ? WHERE tbl_reserved_ip = ? AND tbl_mac_address = ?"""
                        update_values = (host_name, reserved_ip, mac_address, lease_time, lease_expire, time_stamp, timestamp_diff, reserved_ip, mac_address)
                        cur.execute(update_query, update_values)
                        db.commit
                    elif mac_address != check_tbl_entry:
                        cur.execute("INSERT INTO ipam_db_reservations VALUES(?, ?, ?, ?, ?, ?, ?)", (host_name, reserved_ip, mac_address, lease_time, lease_expire, time_stamp, timestamp_diff)) 
                        db.commit()
                    else:
                        pass
                    time.sleep(4)
            cur = db.cursor()    
            cur.execute("SELECT * FROM ipam_db_reservations ORDER BY tbl_reserved_ip ASC, tbl_time_stamp DESC")
            #reservation_entry = cur.fetchone()
            reservation_entries = cur.fetchall()
            print("")
            print("IPAM IP Address Reservarions Database Table")
            print("-----------------------------------------------------------------------------------------------------------")
            print("| IP Address  | MAC Address       | Lease Exp  | Time Stamp | Diff | Lease | Host Name |")
            print("-----------------------------------------------------------------------------------------------------------")
            for row in reservation_entries:
                print("| {} | {} | {} | {} | {}    | {}    | {}    |".format(row[1],row[2],row[4],row[5],row[6],row[3],row[0]))
                key = row[1]
                value = row[2]
                reservations_dict[key] = value
                #print(reservation_entries)
            print("-----------------------------------------------------------------------------------------------------------")
            print("")
            print(reservations_dict)
            print("")
        except json.JSONDecodeError:
            print("kea-lease4.json file is empty")
    return reservations_dict

def get_ReservedMacAddress(ip): 
    # Troubleshooting code, proof of concept of in-memory IPAM Database in lieu of in-memory sqlite3 database above.
    # change IP Addresses and MAC Adderess to test
    ipam_db_dict = {
        ## Proof of concept in lue of sqlite3 in-memory database
        "192.168.2.1": "00:50:56:01:7a:e2",
        "192.168.2.2": "00:50:56:01:7a:cd",
        "192.168.2.3": "00:50:56:01:7a:ce",
        "192.168.2.4": "00:50:56:01:58:78"
    }
    #print(ipam_db_dict)
    reserved_mac_address = ipam_db_dict[ip]
    #ipam_reservations_dict = {}
    #ipam_reservations_dict = get_ipAddress_reservations()
    
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
    
