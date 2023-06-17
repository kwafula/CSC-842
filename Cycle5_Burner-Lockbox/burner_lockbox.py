#!/usr/bin/env python3 

import argparse
import requests
from requests.structures import CaseInsensitiveDict
import subprocess
from subprocess import output
import time
import sys
from datetime import datetime

## Note: Post-exploitation tool
## 
def parseArguments(valid_choices):
    parser = argparse.ArgumentParser(description="Burner Lockbox Manager")
    parser.add_argument('-c', '--command ', help="Add files to lockbox container", nargs="?")  ## "mkdr" "/opt/temp_dir? "sudo mkdir /opt/temp_dir (Choices)
    parser.add_argument('-f', '--file_name', help="Create lockbox container", nargs="?")
    parser.add_argument('-m', '--mount', help="Mount lockbox container", nargs="?")
    parser.add_argument('-u', '--unmount', help="Unmount lockbox container", nargs="?")
    parser.add_argument("-s", "--command", dest='outfile', help="file to save the output", nargs="?")
    return parser.parse_args()
    
## Create lockbox
def create_burner_lockbox():
    
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

def run_shell_command(cmd):
    try:
        pro = subprocess.run(cmd, capture_output=True, text=True, shell=True)#, shell=True,env=myenv,executable='/bin/bash')#
        if pro.stdout:
            output = pro.stdout
            
            return f"---------------Exploit/Shellcode Detail---------------\n {pro.stdout}"
        elif pro.stderr:
            return f"---------------Error----------------------------------\n {pro.stderr}"
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"
        

if __name__ == '__main__':
    global command
    ## Create help and menu
    print("-----------------------------------------------------------------------------------------------------------")
    while True:

    print("----------------------------------------------------------------------------------------------------------")
    

