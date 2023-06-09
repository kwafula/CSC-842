#!/usr/bin/env python3 

import scapy.all as scapy
import csv
import json
import argparse
import sqlite3
import requests
from requests.structures import CaseInsensitiveDict
import time
from datetime import datetime

# Create menu arguments here

# Initialize SQLLite IP Address Management (IPAM) database - In memory database for authoritative IP Address to MAC Address mappings
def init_ipam_db():
    db = sqlite3.connect(':memory:')
    cur = db.cursor()
    cur.execute( 'CREATE TABLE ipam_db_reservations(tbl_host_name text, tbl_reserved_ip text, tbl_mac_address text, tbl_lease_time int, tbl_lease_expire int, tbl_time_stamp int, tbl_timestamp_diff int)') 
    db.commit()
    return db

# Add script exit code and usage menu
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest = "interface", default = "enp0s3", help = "Monitored Interface") ## Update the monitoring interface with your configuration
    args = parser.parse_args()
    return args

def get_dhcp4_leases():
    """
    ##### Troubleshooting code:### Proof of concept of in-memory IPAM Database in lieu of in-memory sqlite3 database above.
    ##### change IP Addresses and MAC Adderess to test
    ##### Proof of concept in lue of sqlite3 in-memory database
    reservations_dict = { "192.168.2.1": "00:50:56:01:7a:e2", "192.168.2.2": "00:50:56:01:7a:cd", "192.168.2.3": "00:50:56:01:7a:ce", "192.168.2.4": "00:50:56:01:58:78"}
    """
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
    print("-----------------------------------------------------------------------------------------------------------")
    print("[+]Dumping DHCP4 Leases From: //var/lib/kea/kea-leases4.csv To: /var/lib/kea/kea-leases4.json file") 
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    ##### Option 2: ### Read Active IP Address Lease Reservations from Kea DHCP4 Server (/var/lib/kea/kea-leases4.csv)
    csvfile = open('/var/lib/kea/kea-leases4.csv', 'r')
    fieldnames = ("address", "hwaddr", "client_id", "valid_lifetime", "expire", "subnet_id", "fqdn_fwd", "fqdn_rev", "hostname", "state", "user_context")
    reader = csv.DictReader(csvfile) # without headers
    # reader = csv.DictReader( csvfile, fieldnames) # with headers
    json_data = json.dumps(list(reader))
    
    with open('/var/lib/kea/kea-leases4.json', 'w') as jsonfile:
        json.dump(json_data, jsonfile)
    print(" ")
    return

#def get_registered_macAddress(ip):
def load_ipam_db():
    #db = sqlite3.connect(':memory:')
    #reservations_dict = {}
    
    for x in range(0, 5):    
        get_dhcp4_leases()
        with open("/var/lib/kea/kea-leases4.json", 'r', encoding='utf-8') as active_leases:
            try:
                print("-----------------------------------------------------------------------------------------------------------")
                print("[+]Loading DHCP Lease Reservations From: /var/lib/kea/kea-leases4.json file ") 
                print("-----------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------------------------------")
                lease_data = json.load(active_leases)
                json_list_dict= json.loads(lease_data)
                for item in json_list_dict:
                    print(item)
                    print("-----------------------------------------------------------------------------------------------------------")
                    print("")
                print("-----------------------------------------------------------------------------------------------------------")
                print("[+]Registering DHCP Lease Reservation To SQLite3 IPAM Database") 
                print("-----------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------------------------------")
                for dict in json_list_dict:
                    host_name = dict["hostname"]
                    reserved_ip = dict["address"]
                    mac_address = dict["hwaddr"]
                    lease_time = dict["valid_lifetime"]
                    lease_expire = dict["expire"]
                    cur = db.cursor()
                    time_stamp = time.mktime(datetime.now().timetuple())
                    timestamp_diff = float(lease_expire) - time_stamp
                    cur.execute("SELECT tbl_mac_address FROM ipam_db_reservations WHERE tbl_reserved_ip = ? AND tbl_mac_address = ?", (reserved_ip, mac_address))
                    get_tbl_entry = cur.fetchone()
                    cur.execute("SELECT tbl_timestamp_diff FROM ipam_db_reservations WHERE tbl_reserved_ip = ? AND tbl_mac_address = ?", (reserved_ip, mac_address))
                    get_tbl_timestamp_diff = cur.fetchone()
                    check_tbl_entry = str(get_tbl_entry).replace("'",'').replace(",",'').replace("(",'').replace(")",'')
                    get_tbl_timestamp_diff = str(get_tbl_timestamp_diff).replace("'",'').replace(",",'').replace("(",'').replace(")",'')
                    timestamp_diff_int = int(timestamp_diff)
                    print("ARP Respone: Sender MAC Addr {0} Sender IP Addr {1} < > IPAM Database MAC Addr Entry: {2} ".format(mac_address, reserved_ip, check_tbl_entry))
                    if ((mac_address == check_tbl_entry) and (timestamp_diff_int >= int(get_tbl_timestamp_diff))): # 
                        update_query = """UPDATE ipam_db_reservations SET tbl_host_name = ?, tbl_reserved_ip = ?, tbl_mac_address = ?, tbl_lease_time = ?, tbl_lease_expire = ?, tbl_time_stamp = ?, tbl_timestamp_diff = ? WHERE tbl_reserved_ip = ? AND tbl_mac_address = ?"""
                        update_values = (host_name, reserved_ip, mac_address, lease_time, lease_expire, time_stamp, timestamp_diff, reserved_ip, mac_address)
                        cur.execute(update_query, update_values)
                        db.commit
                    elif mac_address != check_tbl_entry:
                        cur.execute("INSERT INTO ipam_db_reservations VALUES(?, ?, ?, ?, ?, ?, ?)", (host_name, reserved_ip, mac_address, lease_time, lease_expire, time_stamp, timestamp_diff)) 
                        db.commit()
                    else:
                        pass
                    print("-----------------------------------------------------------------------------------------------------------")
                print("")
            except json.JSONDecodeError:
                print("kea-lease4.json file is empty")
        time.sleep(5)
    return

def process_sniffed_packet(packet):
    #db = sqlite3.connect(':memory:')
    reservations_dict = {}
    
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2: # ARP Requests and ARP Replies only
        try:
            print("-----------------------------------------------------------------------------------------------------------")
            print("[+]Sniffing ARP Response Ethernt Packets On The Protected LAN ") 
            print("-----------------------------------------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------------------------------------")
            eth_header_source_mac_address = packet[scapy.Ether].src
            print("[+] Sender Ethernet Header MAC Address: {0}".format(eth_header_source_mac_address))
            print("---------------------------------------------------------")
            
            eth_header_destination_mac_address = packet[scapy.Ether].dst
            print("[+] Destination Ethernet Header MAC Address: {0}".format(eth_header_destination_mac_address))
            print("---------------------------------------------------------")
            
            eth_payload_sender_mac_address = packet[scapy.ARP].hwsrc
            print("[+] Sender Ethernet Payload MAC Address: {0}".format(eth_payload_sender_mac_address))
            print("---------------------------------------------------------")
            
            eth_payload_sender_ip_address = packet[scapy.ARP].psrc
            print("[+] Sender Ethernet Payload IP Address: {0}".format(eth_payload_sender_ip_address))
            print("---------------------------------------------------------")
            
            eth_payload_target_mac_address = packet[scapy.ARP].hwdst
            print("[+] Target Ethernet Payload MAC Address: {0}".format(eth_payload_target_mac_address))
            print("---------------------------------------------------------")
            
            eth_payload_target_ip_address = packet[scapy.ARP].pdst
            print("[+] Target Ethernet Payload IP Address: {0}".format(eth_payload_target_ip_address))
            print("----------------------------------------------------------------------------------------------------------")
            print("")
            print("")
            
            cur = db.cursor()    
            cur.execute("SELECT * FROM ipam_db_reservations ORDER BY tbl_reserved_ip ASC, tbl_time_stamp DESC")
            reservation_entries = cur.fetchall()
            print("")
            print("IPAM IP Address Reservarions Database Table")
            print("-----------------------------------------------------------------------------------------------------------")
            print("| IP Address  | MAC Address       | Lease Exp  | Time Stamp | Diff | Lease | Host Name |")
            print("-----------------------------------------------------------------------------------------------------------")
            print("-----------------------------------------------------------------------------------------------------------")
            for row in reservation_entries:
                print("| {} | {} | {} | {} | {}    | {}    | {}    |".format(row[1],row[2],row[4],row[5],row[6],row[3],row[0]))
                key = row[1]
                value = row[2]
                reservations_dict[key] = value
            print("-----------------------------------------------------------------------------------------------------------")
            print("")
            if reservations_dict.get(eth_payload_sender_ip_address):
                #reserved_mac_address = reservations_dict[ip]
                reserved_mac_address = reservations_dict[eth_payload_sender_ip_address]
            else:
                reserved_mac_address = "00:00:00:00:00:00"
                 
            if reserved_mac_address == "00:00:00:00:00:00":
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] No ARP Attacks Detectected")
                print("----------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Payload IP Address: {0} Is Reserved For ARP NIDS MAC Address: {1}".format(eth_payload_sender_ip_address, eth_header_source_mac_address))
                print("[+] ARP Payload MAC Addrress: {0} Is Legit".format(eth_payload_sender_mac_address))
            elif reserved_mac_address != eth_payload_sender_mac_address:
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Poisoning Attack *{@ v @ }* Detectected !!!!")
                print("----------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Payload IP Address: {0} Is Reserved And/Or Assigned To MAC Address: {1}".format(eth_payload_sender_ip_address, reserved_mac_address))
                print("[+] ARP Payload MAC Addrress: {0} Is A Spoof".format(eth_payload_sender_mac_address))
                print("----------------------------------------------------------------------------------------------------------")
                print(" ")
            else:
                print("----------------------------------------------------------------------------------------------------------")
                print("[+] No ARP Attacks Detectected")
                print("----------------------------------------------------------------------------------------------------------")
                print("-----------------------------------------------------------------------------------------------------------")
                print("[+] ARP Payload IP Address: {0} Is Reserved And/Or Assigned To MAC Address: {1}".format(eth_payload_sender_ip_address, reserved_mac_address))
                print("[+] ARP Payload MAC Addrress: {0} Is Legit".format(eth_payload_sender_mac_address))
                print("----------------------------------------------------------------------------------------------------------")
                print(" ")
        except IndexError:
            pass
        
if __name__ == '__main__':

    print("-----------------------------------------------------------------------------------------------------------")
    print("[+] Initializing IPAM Database")
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    print("")
    db = init_ipam_db()
    
    load_ipam_db()
  
    print("-----------------------------------------------------------------------------------------------------------")
    print("[+] Starting ARP Poisonin NIDS")   
    print("-----------------------------------------------------------------------------------------------------------")
    print("-----------------------------------------------------------------------------------------------------------")
    print(" ")
    args = get_arguments()
    scapy.sniff(iface = args.interface, prn = process_sniffed_packet, store = 0)       # filter = "arp",
    print(" ")
    print("----------------------------------------------------------------------------------------------------------")
    
