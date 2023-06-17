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

## Implement Argparse: Refer -> https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
def parseArguments():
    parser = argparse.ArgumentParser(description="Burner Lockbox Manager:")
    
    subparser = parser.add_subparsers(dest='command')
    
    create_container = subparser.add_parser('create_container')
    mount_container = subparser.add_parser('mount_container')
    add_file = subparser.add_parser('add_file')
    delete_file = sub parser.add_parser('delete_file')
    dismount__container = subparser.add_parser('dismount_container')
    upload_container = subparser.add_parser('upload_container')
    download_container = subparser.add_parser('download_container')

    create_container.add_argument('--create_container_command_string', type=str, required=True, help='Name of lockbox container\n\n')
    create_container.add_argument('--create_container_name', type=str, required=True, help='Name of lockbox container\n\n')

    mount_container.add_argument('--mount_container_command_string', type=str, required=True, help='Name of lockbox container\n\n')
    mount_container.add_argument('--mount_container_name', type=str, required=True, help='Name of lockbox container\n\n')

    add_file.add_argument('--add_file_command_string', type=str, required=True, nargs='+', help='File name(s) of a tool(s) to add to the lockbox container\n\n')
    add_file.add_argument('--add_file_name', type=str, required=True, nargs='+', help='File name(s) of a tool(s) to add to the lockbox container\n\n')

    delete_file.add_argument('--delete_file_command_string', type=str, required=True, nargs='+', help='File name(s) of a tool(s) to delete from the lockbox container\n\n')
    delete_file.add_argument('--delete_file_name', type=str, required=True, nargs='+', help='File name(s) of a tool(s) to delete from the lockbox container\n\n')

    dismount_container.add_argument('--dismount_container_command_string', type=str, required=True, help='Name of lockbox container\n\n')
    dismount_container.add_argument('--dismoint_container_name', type=str, required=True, help='Name of lockbox container\n\n')

    upload_container.add_argument('--upload_container_command_string', type=str, required=True, help='URL string of the public Github repository of the lockbox container\n\n')
    upload_container.add_argument('--upload_url_string', type=str, required=True, help='URL string of the public Github repository of the lockbox container\n\n')

    download_container.add_argument('--download_container_command_string', type=str, required=True, help='URL string of the public Github repository of the lockbox container\n\n')
    download_container.add_argument('--download_url_string', type=str, required=True, help='URL string of the public Github repository of the lockbox container\n\n')
    
    return parser.parse_args()
    
## Create lockbox
#def create_burner_lockbox():
    
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
    #global command
    print("-----------------------------------------------------------------------------------------------------------")
    if args.command == 'create_container':
        print('This option will create a lock box continaer using command string: ', args.create_container_command_string, ' and container name: ', args.creater_container_name)
    elif args.command == 'mount_container':
         print('This option will mount a lock box continaer using command string: ', args.mount_container_command_string, ' and container name: ', args.mount_container_name)
    elif args.command == 'add_file':
         print('This option will mount a lock box continaer using command string: ', args.add_file_command_string, ' and container name: ', args.add_file_name)
    elif args.command == 'delete_file':
         print('This option will mount a lock box continaer using command string: ', args.delete_file_command_string, ' and container name: ', args.delete_file_name)
    elif args.command == 'dismount_container':
         print('This option will mount a lock box continaer using command string: ', args.dismount_container_command_string, ' and container name: ', args.dismount_container_name)
    elif args.command == 'upload_container':
         print('This option will mount a lock box continaer using command string: ', args.upload_container_command_string, ' and container name: ', args.upload_container_name)
    elif args.command == 'download_container':
         print('This option will mount a lock box continaer using command string: ', args.download_container_command_string, ' and container name: ', args.download_container_name)
    print("----------------------------------------------------------------------------------------------------------")
    

