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
import sys
import subprocess

## Note: Post exploitation tool

## Create help and menu

## Create lockbox
## If veracrypt is not installed:
##     Install veracrypt
##     Create lockbox
## else:
##    Create lockbox

## Stash the lockbox (optional)

## Upload the lockbox 






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
    
