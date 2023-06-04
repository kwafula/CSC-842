
import subprocess
import json
import random
import threading
import argparse
import time
import sys
import sqlite3
import socket
import netifaces
import time
from scapy.all import *
from datetime import datetime


# Create menu arguments

# Initialize SQLLite IP Address Management (IPAM) database - In memory database for authoritative IP Address to MAC Address mappings
def ipam_db():
  
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
    cur.execute('CREATE TABLE nat_entries (Alert.Date text,  Alert.Msg text, EthII.SrcMAC text, EthII.DstMAC text, EthII.Type text, ARPMsg.OpCode int, ARPMsg.SrcMAC text, \ 
    ARPMsg.DstMAC text, ARPMsg.SrcIP text, ARPMsg.DstIP text, ARPMsg.IsGrat BOOLEAN )')
    db.commit()
  return db

# Read IP Address reservation from Windows DHCP Reserved Scope for the protected subnet - All IP Addresses are issue by means of reservation only as security measure

# Populate the IPAM Database with authoritative IP Address to MAC address reservations from Windows DHCP Server 

# Read packets on the protected subnet promiscously and filter for arp messages

# Compare IP/MAC association in ARP Op Code 1/ARP Requests and Op Code 2/ARP Responses againts authorititive IPAM Database and enumarate inconsistencies

# Optionally do checks i.e. Ping etc.

# Create notification message templates for Op Code 1 violations and Op Code 2 violations

# Raise Alarm (1) Write messag to log (2) print on screen (3) send email (4) post on Slack (5) log to graylog)
