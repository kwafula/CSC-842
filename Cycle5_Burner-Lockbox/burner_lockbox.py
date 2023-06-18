#!/usr/bin/env python3 

import argparse
import requests
from requests.structures import CaseInsensitiveDict
import subprocess
import time
import sys
from datetime import datetime

## Note: Post-exploitation tool

#Dependencies
# sudo with/nopassword
# python requirement
# sudo add-apt-repository ppa:unit193/encryption -y
# sudo apt-get update -y
# sudo apt-get install -y libwxgtk3.0-gtk3-0v5
# sudo apt-get install -y exfat-fuse exfat-utils
# sudo apt-get install -y exfatprogs

# Randomdata.text https://github.com/arcanecode/VeraCrypt-CommandLine-Examples
# curl
#
# veracrypt

## Implement Argparse: Refer -> https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
def parseArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Burner Lockbox Manager:')
    
    subparser = parser.add_subparsers(dest='function')
    
    create_dir = subparser.add_parser('create_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a directory,\n'
                                 'Arguement: --name <directory name>,\n'
                                 'Usage: python3 burner_lockbox.py create_dir --name /opt/tempveracrypt\n\n')
    check_dependencies = subparser.add_parser('check_dependencies', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a directory,\n'
                                 'Arguement: None,\n'
                                 'Usage: python3 burner_lockbox.py check_dependencies\n\n')
    create_lockbox = subparser.add_parser('create_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a lockbox container,\n'
                                 'Arguement: --name <lockbox name> --password <password string> --size <size> --type <normal | hidden>,\n'
                                 'Usage: python3 burner_lockbox.py create_lockbox --name lockbox.vc --password Ch@ngeM3 --size 1G \n\n')
    mount_container = subparser.add_parser('mount_container')
    cp_file = subparser.add_parser('cp_file')
    del_file = subparser.add_parser('del_file')
    dmount_container = subparser.add_parser('dmount_container')
    uload_container = subparser.add_parser('uload_container')
    dload_container = subparser.add_parser('dload_container')
    remove_dir = subparser.add_parser('remove_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Deletes a directory,\n'
                                 'Arguement: --name <directory name>,\n'
                                 'Usage: python3 burner_lockbox.py remove_dir --name /opt/tempveracrypt\n\n')

    create_dir.add_argument('--name', type=str, required=True)
    
    create_lockbox.add_argument('--name', type=str, required=True)
    create_lockbox.add_argument('--password', type=str, required=True)
    create_lockbox.add_argument('--size', type=str, required=True)
    create_lockbox.add_argument('--type', type=str, choice = ['normal', 'hidden'], required=True)
    
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

    remove_dir.add_argument('--name', type=str, required=True)

    args = parser.parse_args()
    cmd_string = None
    #cmd_string = args.command + ' ' + args.name
    
    if args.function == 'make_dir':
        print('This option will create a temporary directory: ', args.name)
        cmd_string = 'mkdir' + ' ' + args.name
    elif args.function == 'remove_dir':
        print('This option will delete a temporary directory: ', args.name)
        cmd_string = 'rm -fr' + ' ' + args.name
    elif args.function == 'check_dependencies':
        print('This option will check and resolve lockbox check_dependencies:')
        cmd_repo = 'add-apt-repository ppa:unit193/encryption -y'
        cmd_update = 'apt-get update -y'
        cmd_libwixgtk = 'apt-get install -y libwxgtk3.0-gtk3-0v5'
        cmd_exfat_fuse = 'apt-get install -y exfat-fuse exfat-utils'
        cmd_exfatprogs = 'apt-get install -y exfatprogs'
        packages = [cmd_repo, cmd_update,cmd_libwixgtk, cmd_exfat-fuse, cmd_exfatprogs]
        for pkg_cmd in packages:
            run_shell_command (pkg_cmd)
        '''
        packages = ['curl','git','libwxgtk3.0-gtk3-0v5','exfat_fuse','exfatprogs']
        for pkg in packages:
            pkg_query = 'dpkg-query -W ' + pkg + ' | grep ' + pkg + ' | wc -l'
            pkg_install = 'dpkg-query -W ' + pkg + ' | grep ' + pkg + ' | wc -l'
            if pkg_query == 1:
                pass
            else:
        '''
                
    elif args.function == 'creat_lockbox':
        cmd_string = 'veracrypt' + ' --text --create ' + args.name + ' --size ' + args.size + ' --password ' + args.password + ' --volume-type ' + args.type + ' --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" '
        print(cmd_string)
        #veracrypt --text --create vctest.vc --size 200M --password MySuperSecurePassword1! --volume-type normal --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" 
    elif args.function == 'mount_container':
         print('This option will mount a lockbox container using command string: ', args.mount_container_command_string, ' and container name: ', args.mount_container_name)
    elif args.function == 'cp_file':
         print('This option will mount a lockbox container using command string: ', args.cp_file_command_string, ' and container name: ', args.cp_file_name)
    elif args.function == 'del_file':
         print('This option will mount a lockbox container using command string: ', args.del_file_command_string, ' and container name: ', args.del_file_name)
    elif args.function == 'dmount_container':
         print('This option will mount a lockbox container using command string: ', args.dmount_container_command_string, ' and container name: ', args.dmount_container_name)
    elif args.function == 'uload_container':
         print('This option will mount a lockbox container using command string: ', args.uload_container_command_string, ' and container name: ', args.uload_container_name)
    elif args.function == 'dload_container':
         print('This option will mount a lockbox container using command string: ', args.dload_container_command_string, ' and container name: ', args.dload_container_name)
    
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
            exit_string = pro.stdout
            return exit_string
        elif pro.stderr:
            exit_string = pro.stderr
            return exit_string
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"
        

if __name__ == '__main__':
    
    print("-----------------------------------------------------------------------------------------------------------")
    '''
    cmd_string = parseArguments()
    if cmd_string.command == 'make_dir':
        cmd = 'mkdir' + ' ' + cmd.name
        print('This option will run this command string: ', cmd)
    '''
    
    cmd = parseArguments()
    print('Running the following command under subprocess: ', cmd)
    print(type(cmd))
    run_shell_command(cmd)
    
    print("----------------------------------------------------------------------------------------------------------")
    

