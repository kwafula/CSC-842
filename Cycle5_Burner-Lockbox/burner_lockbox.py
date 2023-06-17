#!/usr/bin/env python3 

import argparse
import requests
from requests.structures import CaseInsensitiveDict
import subprocess
import time
import sys
from datetime import datetime

## Note: Post-exploitation tool

## Implement Argparse: Refer -> https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
def parseArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Burner Lockbox Manager:')
    
    subparser = parser.add_subparsers(dest='command')
    
    make_dir = subparser.add_parser('make_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function description: Make temporary directory,\n'
                                 'Arguements: --command <command> --name <directory name>,\n'
                                 'Usage: python3 burner_lockbox.py make_dir --command mkdir --dir-name /opt/tempveracrypt\n\n')
    create_container = subparser.add_parser('create_container')
    mount_container = subparser.add_parser('mount_container')
    cp_file = subparser.add_parser('cp_file')
    del_file = subparser.add_parser('del_file')
    dmount_container = subparser.add_parser('dmount_container')
    uload_container = subparser.add_parser('uload_container')
    dload_container = subparser.add_parser('dload_container')
    remove_dir = subparser.add_parser('remove_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function description: Delete temporary directory,\n'
                                 'Arguements: --command <command> --name <directory name>,\n'
                                 'Usage: python3 burner_lockbox.py remove_dir --command rm -fr --name /opt/tempveracrypt\n\n')

    make_dir.add_argument('--command', type=str, required=True)
    make_dir.add_argument('--name', type=str, required=True)
    
    create_container.add_argument('--create_container_command_string', type=str, required=True, help='Command string to createlockbox container\n')
    create_container.add_argument('--create_container_name', type=str, required=True, help='Name of lockbox container to create\n\n')

    mount_container.add_argument('--mount_container_command_string', type=str, required=True, help='Command string to mount lockbox container\n')
    mount_container.add_argument('--mount_container_name', type=str, required=True, help='Name of lockbox container to mount\n\n')

    cp_file.add_argument('--cp_file_command_string', type=str, required=True, nargs='+', help='Command string to add file(s) to lockbox container\n')
    cp_file.add_argument('--cp_file_name', type=str, required=True, nargs='+', help='File name(s) of a tool(s) to add to the lockbox container\n\n')

    del_file.add_argument('--del_file_command_string', type=str, required=True, nargs='+', help='Command string to delete file(s) to lockbox containerr\n')
    del_file.add_argument('--del_file_name', type=str, required=True, nargs='+', help='File name(s) of a tool(s) to delete from the lockbox container\n\n')

    dmount_container.add_argument('--dmount_container_command_string', type=str, required=True, help='Command string to dismount lockbox container\n')
    dmount_container.add_argument('--dmoint_container_name', type=str, required=True, help='Name of lockbox container to dismount\n\n')

    uload_container.add_argument('--uload_container_command_string', type=str, required=True, help='Command string to upload lockbox container\n')
    uload_container.add_argument('--uload_url_string', type=str, required=True, help='URL string of the public Github repository of the lockbox container\n\n')

    dload_container.add_argument('--dload_container_command_string', type=str, required=True, help='Command string to download lockbox container\n')
    dload_container.add_argument('--dload_url_string', type=str, required=True, help='URL string of the public Github repository of the lockbox container\n\n')

    remove_dir.add_argument('--command', type=str, required=True)
    remove_dir.add_argument('--name', type=str, required=True)

    args = parser.parse_args()
    
    #cmd_string = args.command + ' ' + args.name
    
    if args.command == 'make_dir':
        print('This option will create a temporary directory using command string: ', args.command, ' and directory name: ', args.dir-name)
        cmd_string = args.command + ' ' + args.name
    elif args.command == 'create_container':
        print('This option will create a lockbox container using command string: ', args.create_container_command_string, ' and container name: ', args.create_container_name)
    elif args.command == 'mount_container':
         print('This option will mount a lockbox container using command string: ', args.mount_container_command_string, ' and container name: ', args.mount_container_name)
    elif args.command == 'cp_file':
         print('This option will mount a lockbox container using command string: ', args.cp_file_command_string, ' and container name: ', args.cp_file_name)
    elif args.command == 'del_file':
         print('This option will mount a lockbox container using command string: ', args.del_file_command_string, ' and container name: ', args.del_file_name)
    elif args.command == 'dmount_container':
         print('This option will mount a lockbox container using command string: ', args.dmount_container_command_string, ' and container name: ', args.dmount_container_name)
    elif args.command == 'uload_container':
         print('This option will mount a lockbox container using command string: ', args.uload_container_command_string, ' and container name: ', args.uload_container_name)
    elif args.command == 'dload_container':
         print('This option will mount a lockbox container using command string: ', args.dload_container_command_string, ' and container name: ', args.dload_container_name)
    elif args.command == 'del_dir':
        print('This option will create a lockbox container using command string: ', args.del_dir_command_string, ' and container name: ', args.del_dir_name)
    
    return cmd_string #args
    
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

def run_shell_command(shell_cmd):
    try:
        pro = subprocess.run(shell_cmd, capture_output=True, text=True, shell=True)#, shell=True,env=myenv,executable='/bin/bash')#
        if pro.stdout:
            return f"---------------Exploit/Shellcode Detail---------------\n {pro.stdout}"
        elif pro.stderr:
            return f"---------------Error----------------------------------\n {pro.stderr}"
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"
        

if __name__ == '__main__':
    global cmd_string
    
    print("-----------------------------------------------------------------------------------------------------------")
    cmd = parseArguments()
    print('Running the following command under subprocess: ', cmd)
    print(type(cmd))
    run_shell_command(cmd)
    print("----------------------------------------------------------------------------------------------------------")
    

