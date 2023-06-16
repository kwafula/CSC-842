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
## 

## Create help and menu

## Create lockbox
## If veracrypt is not installed:
##     Install veracrypt
##     Create lockbox
## else:
##    Create lockbox

## Stash the lockbox (optional)

## Upload the lockbox to a public repo

## Create short download URL : https://zapier.com/blog/best-url-shorteners/

## Download lockbox

## If veracrypt is not installed:
##     Install veracrypt
##     Download lockbox
## else:
##    Downalod lockbox

## Lockbox timer or auto-lock on exit or independent auto-lock memory resident code

## Detect memory dump routine and trigger auto-lock

## Detect vm snapshot routine and trigger auto-lock

## Generate PE install package for Windows install package windows
## Generate DMG install package for Mac
## Generate RPM install package for CentOS/Redhat
## Generate Deb install package for Ubuntu/Debian 










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
    

