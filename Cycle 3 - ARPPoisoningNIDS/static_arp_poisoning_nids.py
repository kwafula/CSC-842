#!/usr/bin/env python3 

import scapy.all as scapy
import csv
import json
import argparse
import sqlite3
import requests
from requests.structures import CaseInsensitiveDict

# Create menu arguments here

def get_ReservedMacAddress(ip): # Troubleshooting code, proof of concept of an IPAM Database, replace with sqlite3 database synced to DHCP reserved scope 
    ipam_db_dict = {
        ## Proof of concept in lue of sqlite3 in-memory database
        "192.168.2.1": "00:50:56:01:7a:e2",
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
    
    print("[+] Starting ARP Poisonin NIDS")    
    args = get_arguments()
    scapy.sniff(iface = args.interface, prn = process_sniffed_packet, store = 0)       # filter = "arp",
    print(" ")
    print("----------------------------------------------------------------------------------------------------------")
