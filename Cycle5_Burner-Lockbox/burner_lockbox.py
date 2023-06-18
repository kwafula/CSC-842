#!/usr/bin/env python3 

import argparse
import subprocess
import sys

## Note: Post-exploitation tool
# curl -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle5_Burner-Lockbox/burner_lockbox.py --output burner_lockbox.py

######### Feature List ############
## Lockbox timer or auto-lock on exit or independent auto-lock memory resident code
## Detect memory dump routine and trigger auto-lock
## Detect vm snapshot routine and trigger auto-lock    
## Generate PE install package for Windows install package windows
## Generate DMG install package for Mac
## Generate RPM install package for CentOS/Redhat
## Generate Deb install package for Ubuntu/Debian

# Randomdata.text https://github.com/arcanecode/VeraCrypt-CommandLine-Examples
# Implement Argparse: Refer -> https://towardsdatascience.com/a-simple-guide-to-command-line-arguments-with-argparse-6824c30ab1c3
# Filebin https://filebin.net/p5oig73mhgaieu04
# curl -T monocacygatewayplan800w.jpg https://filebin.net/p5oig73mhgaieu04/
# curl -L https://filebin.net/p5oig73mhgaieu04//monocacygatewayplan800w.jpg --output monocacygatewayplan800w-2.jpg

def parseArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Burner Lockbox Manager:')
    
    subparser = parser.add_subparsers(dest='function')
    
    create_dir = subparser.add_parser('create_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a directory,\n'
                                 'Arguments: --name <directory name including path>,\n'
                                 'Usage: python3 burner_lockbox.py create_dir --name /opt/tempveracrypt\n\n')
    
    remove_dir = subparser.add_parser('remove_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Deletes a directory,\n'
                                 'Arguments: --name <directory name>,\n'
                                 'Usage: python3 burner_lockbox.py remove_dir --name /opt/tempveracrypt\n\n')

    check_dependencies = subparser.add_parser('check_dependencies', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Install Veracrypt package dependencies,\n'
                                 'Arguments: None,\n'
                                 'Usage: python3 burner_lockbox.py check_dependencies\n\n')
    
    create_lockbox = subparser.add_parser('create_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a lockbox container,\n'
                                 'Arguments: --name <lockbox name> --password <password string> --size <size> --type <normal | hidden>,\n' ## verify hidden argument value
                                 'Usage: python3 burner_lockbox.py create_lockbox --name lockbox.vc --password Ch@ngeM3 --size 25M --type normal \n\n')
    
    mount_lockbox = subparser.add_parser('mount_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Mounts a lockbox container,\n'
                                 'Arguments: --name <lockbox name and mount location> --password <password string>,\n'
                                 'Usage: python3 burner_lockbox.py mount_lockbox --name lockbox.vc /mnt --password Ch@ngeM3\n\n')
                                 
    list_lockbox = subparser.add_parser('list_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: List lockbox containers,\n'
                                 'Arguments: None,\n'
                                 'Usage: python3 burner_lockbox.py list_lockbox\n\n')
    
    dismount_lockbox = subparser.add_parser('dismount_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Dismounts a lockbox container,\n'
                                 'Arguments: --name <lockbox name>,\n'
                                 'Usage: python3 burner_lockbox.py dismount_lockbox --name lockbox.vc \n\n')

    upload_lockbox = subparser.add_parser('upload_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Upload a lockbox container to a public repo,\n'
                                 'Arguments: --name <lockbox name> --url <lockbox upload URL>,\n'
                                 'Usage: python3 burner_lockbox.py upload_lockbox --name lockbox.vc --url https://filebin.net/p5oig73mhgaieu04/ \n\n')
                                 
    download_lockbox = subparser.add_parser('download_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Downloads a lockbox container from a public repo,\n'
                                 'Arguments: --name <lockbox name> --url <lockbox download URL>,\n'
                                 'Usage: python3 burner_lockbox.py download_lockbox --name lockbox.vc --url https://filebin.net/p5oig73mhgaieu04//monocacygatewayplan800w.jpg \n\n')
    
    create_dir.add_argument('--name', type=str, required=True)
    
    remove_dir.add_argument('--name', type=str, required=True)
    
    create_lockbox.add_argument('--name', type=str, required=True)
    create_lockbox.add_argument('--password', type=str, required=True)
    create_lockbox.add_argument('--size', type=str, required=True)
    create_lockbox.add_argument('--type', type=str, required=True)
    
    mount_lockbox.add_argument('--name', type=str, required=True)
    mount_lockbox.add_argument('--password', type=str, required=True)

    list_lockbox.add_argument('--name', type=str, required=True)
    list_lockbox.add_argument('--password', type=str, required=True)

    dismount_lockbox.add_argument('--name', type=str, required=True)

    upload_lockbox.add_argument('--name', type=str, required=True)
    upload_lockbox.add_argument('--url', type=str, required=True)

    download_lockbox.add_argument('--name', type=str, required=True)
    download_lockbox.add_argument('--url', type=str, required=True)

    args = parser.parse_args()
    cmd_string = None
    
    if args.function == 'create_dir':
        print('[+] This option will create the following directory: ', args.name)
        print('')
        cmd_string = 'mkdir' + ' ' + args.name
        
    elif args.function == 'remove_dir':
        print('[+] This option will delete the following directory: ', args.name)
        print('')
        cmd_string = 'rm -fr' + ' ' + args.name
        
    elif args.function == 'install_dependencies':
        print('[+] This option will install Veracrypt package dependencies:')
        print('')
        cmd_repo = 'add-apt-repository ppa:unit193/encryption -y'
        cmd_update = 'apt-get update -y'
        cmd_libwixgtk = 'apt-get install -y libwxgtk3.0-gtk3-0v5'
        cmd_exfat_fuse = 'apt-get install -y exfat-fuse exfat-utils'
        cmd_exfatprogs = 'apt-get install -y exfatprogs'
        packages = [cmd_repo, cmd_update,cmd_libwixgtk, cmd_exfat-fuse, cmd_exfatprogs]
        for pkg_cmd in packages:
            run_shell_command (pkg_cmd)
      
    elif args.function == 'create_lockbox':
        cmd_string = 'veracrypt --text --create ' + args.name + ' --size ' + args.size + ' --password ' + args.password + ' --volume-type ' + args.type + ' --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" --random-source /dev/urandom'
        print('[+] This option will create the following lockbox: ', args.name)
        print('')
        # veracrypt --text --create vctest.vc --size 200M --password MySuperSecurePassword1! --volume-type normal --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" --random-source /dev/urandom 
        
    elif args.function == 'mount_lockbox':
        cmd_string = 'veracrypt --text --mount ' + args.name + ' --password ' + args.password + ' --pim 0 --keyfiles "" --protect-hidden no'  
        print('[+] This option will mount the following lockbox: ', args.name)
        print('')
        # veracrypt --text --mount vctest.vc /mnt --password MySuperSecurePassword1! --pim 0 --keyfiles "" --protect-hidden no --slot 1 --verbose
        
    elif args.function == 'list_lockbox':
        cmd_string = 'veracrypt --text --list'
        print('[+] This option will list the following lockbox: ', args.name)
        print('')
        # veracrypt --text --list
        
    elif args.function == 'dismount_lockbox':
        cmd_string = 'veracrypt --text --dismount ' + args.name
        print('[+] This option will dismount the following lockbox: ', args.name)
        print('')
        # veracrypt --text --dismount vctest.vc
        
    elif args.function == 'upload_lockbox':
        cmd_string = 'curl -T ' + args.name + ' ' + args.url
        print('[+] This option will upload the following lockbox: ', args.name)
        print('')
        # curl -T monocacygatewayplan800w.jpg https://filebin.net/p5oig73mhgaieu04/
        
    elif args.function == 'download_lockbox':
        cmd_string = 'curl -L ' + args.url + ' --output ' + args.name
        print('[+] This option will download the following lockbox: ', args.name)
        print('')
        # curl -L https://filebin.net/p5oig73mhgaieu04//monocacygatewayplan800w.jpg --output monocacygatewayplan800w-2.jpg
    
    return cmd_string
 
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
    
    cmd = parseArguments()
    print('[+] Executing the following command: ', cmd)
    # print(type(cmd))
    run_shell_command(cmd)
    
    print("----------------------------------------------------------------------------------------------------------")
    

