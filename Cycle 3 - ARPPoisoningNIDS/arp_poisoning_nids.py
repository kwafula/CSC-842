
import subprocess
import json
#import random
#import threading
import argparse
import time
import sys
import sqlite3
#import socket
import netifaces
import time
import scapy.all as scapy
from datetime import datetime


# Create menu arguments

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
    cur.execute('CREATE TABLE nat_entries (Alert.Date text,  Alert.Msg text, EthII.SrcMAC text, EthII.DstMAC text, EthII.Type text, ARPMsg.OpCode int, ARPMsg.SrcMAC text, ARPMsg.DstMAC text, ARPMsg.SrcIP text, ARPMsg.DstIP text, ARPMsg.IsGrat BOOLEAN )')
    db.commit()
    return db

# Read IP Address reservation from Windows DHCP Reserved Scope for the protected subnet - All IP Addresses are issue by means of reservation only as security measure

# Populate the IPAM Database with authoritative IP Address to MAC address reservations from Windows DHCP Server 

# Read packets on the protected subnet promiscously and filter for arp messages

# Compare IP/MAC association in ARP Op Code 1/ARP Requests and Op Code 2/ARP Responses againts authorititive IPAM Database and enumarate inconsistencies

# Optionally do checks i.e. Ping etc.

# Create notification message templates for Op Code 1 violations and Op Code 2 violations

# Raise Alarm (1) Write messag to log (2) print on screen (3) send email (4) post on Slack (5) log to graylog)
def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest = "interface", default = "ens33", help = "Monitored Interface")
    args = parser.parse_args()
    return args

def get_mac(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout = 1, verbose = False)[0]
    
    return answered_list[0][1].hwsrc

def sniff(interface):
    scapy.sniff(filter ='arp', iface = interface, store=0, prn = process_sniffed_packet)  ## potential add ARP filter option

def process_sniffed_packet(packet):
    db = sqlite3.connect(':memory:')
    #if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
    if packet[scapy.ARP].op == ARP.who_has or if packet[scapy.ARP].op == ARP.is_at:: # ARP Requests and ARP Replies only
        try:
            #real_mac = get_mac(packet[scapy.ARP].psrc)
            real_mac = "00:50:56:28:A2:62" # Troubleshooting code
            response_mac = packet[scapy.ARP].hwsrc
        
            if real_mac == response_mac:
                print("[+] ARP Poisoning Attack Detectected")
                ## Detailed Attack Info
                print(" ")
            else:
                print("[+] ARP Poisoning Attack Not Detected")
                print(" ")
        except IndexError:
            pass
        
if __name__ == '__main__':

    print("[+] Initializing IPAM Database")
    db = init_ipam_db()

    print("[+] Starting ARP Poisonin NIDS")    
    args = get_arguments()
    sniff(args.interface)
