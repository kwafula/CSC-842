#!/usr/bin/env python3 

#import subprocess
import scapy.all as scapy
import json
import argparse
import sqlite3
#import time
#import sys
#import netifaces
#import time
#from datetime import datetime

# Create menu arguments here

# Initialize SQLLite IP Address Management (IPAM) database - In memory database for authoritative IP Address to MAC Address mappings
def init_ipam_db():
  
    ## Fields
    ### Alert.Date
    ### Alert.Msg
    ### EthII.SrcMAC
    ### EthII.DstMAC
    ### EthII.Type
    ### ARPMsg.OpCode
    ### ARPMsg.SrcMAC
    ### ARPMsg.DstMAC
    ### ARPMsg.SrcIP
    ### ARPMsg.DstIP
    ### ARPMsg.IsGrat
    
    db = sqlite3.connect(':memory:')
    cur = db.cursor()
    cur.execute('CREATE TABLE ipam_db_leases (AlertDate text,  AlertMsg text, EthIISrcMAC text, EthIIDstMAC text, EthIIType text, ARPMsgOpCode int, ARPMsgSrcMAC text, ARPMsgDstMAC text, ARPMsgSrcIP text, ARPMsgDstIP text, ARPMsgIsGrat BOOLEAN )')
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
    parser.add_argument("-i", "--interface", dest = "interface", default = "ens33", help = "Monitored Interface")
    args = parser.parse_args()
    return args

def get_ReservedMacAddress(ip): # Troubleshooting code, proof of concept of an IPAM Database, replace with sqlite3 database synced to DHCP reserved scope 
    ipam_db_dict = {
        "172.16.100.2": "00:0C:29:ED:F7:24",
        "172.16.100.100": "00:50:56:3C:EA:DC",
        "172.16.100.150": "00:0C:29:74:91:65",
        "172.16.100.200": "00:50:56:28:A2:62"
    }
    reserved_mac_address = ipam_db_dict[ip]
    return reserved_mac_address 

def process_sniffed_packet(packet):
    db = sqlite3.connect(':memory:')
    #if packet[ARP].op == ARP.who_has or packet[ARP].op == ARP.is_at: # ARP Requests and ARP Replies only
    if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2: # ARP Requests and ARP Replies only
        try:
            #real_mac = get_mac(packet[scapy.ARP].psrc)
            #real_mac = "00:50:56:28:A2:62" # Troubleshooting code, returned MAC of the target host
            #real_mac = "00:0C:29:74:91:65" # Troubleshooting code, returned MAC of the attacking host
            #response_mac = packet[ARP].hwsrc
            
            ethHeader_SenderMacAddress = packet[scapy.Ether].src
            print("[+] ARP Response Ethernet Header Sender MAC Address: {0}".format(ethHeader_SenderMacAddress))
            print(" ")
            
            ethPayload_SenderMacAddress = packet[scapy.ARP].hwsrc
            print("[+] ARP Response Ethernet Payload Sender MAC Address: {0}".format(ethPayload_SenderMacAddress))
            print(" ")
            
            ethPayload_SenderIPAddress = packet[scapy.ARP].psrc
            print("[+] ARP Response Ethernet Payload Sender IP Address: {0}".format(ethPayload_SenderIPAddress))
            print(" ")
            
            reservedMacAddress = get_ReservedMacAddress(ethPayload_SenderIPAddress)
            print("[+] IPAM/DHCP Reserved/Assigned Mac Address: {0}".format(reservedMacAddress))
            print(" ")
            
            if reservedMacAddress == ethPayload_SenderMacAddress:
                print("[+] ARP Poisoning Attack *{@ v @ }* Detectected !!!!")
                print("[+] ARP Payload IP Address: {0} Is Reserved For And/Or Assigned To IPAM/DHCP MAC Address: {1}. ARP Payload MAC Addrress: {2} Is A Spoof".format(ethPayload_SenderIPAddress, reservedMacAddress))
                print(" ")
            else:
                print("[+] ARP Poisoning Attack Not Detectected")
                print("[+] ARP Payload IP Address: {0} Is Reserved For And/Or Assigned To IPAM/DHCP MAC Address: {1}. ARP Payload MAC Addrress: {2} Is Legit".format(ethPayload_SenderIPAddress, reservedMacAddress))
                print(" ")
        except IndexError:
            pass
        
if __name__ == '__main__':

    print("[+] Initializing IPAM Database")
    db = init_ipam_db()

    print("[+] Starting ARP Poisonin NIDS")    
    args = get_arguments()
    scapy.sniff(filter = "arp", iface = args.interface, store = 0, prn = process_sniffed_packet)
