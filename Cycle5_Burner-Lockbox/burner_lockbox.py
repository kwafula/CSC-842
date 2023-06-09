#!/usr/bin/env python3 

import argparse
import subprocess
import sys
import getpass
 

#### Relevant Filebin Info ####
# Bucket : https://filebin.net/p5oig73mhgaieu04
# POST   : curl -T monocacygatewayplan800w.jpg https://filebin.net/p5oig73mhgaieu04/
# GET    : curl -L https://filebin.net/p5oig73mhgaieu04//monocacygatewayplan800w.jpg --output monocacygatewayplan800w-2.jpg

#### Relevant volume check Linux commands ####
# df -hT /mnt
# lsblk

# Fix for issue with curl not reading download https://stackoverflow.com/questions/72627218/openssl-error-messages-error0a000126ssl-routinesunexpected-eof-while-readin

def parseArguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter, description='Burner Lockbox Manager:')
    
    subparser = parser.add_subparsers(dest='function')
    
    create_dir = subparser.add_parser('create_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a directory,\n'
                                 'Arguments: --name <directory name including path>,\n'
                                 'Usage: python3 burner_lockbox.py create_dir --name /opt/tempveracrypt\n\n')
    
    remove_dir = subparser.add_parser('remove_dir', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Deletes a directory,\n'
                                 'Arguments: --name <directory name>,\n'
                                 'Usage: python3 burner_lockbox.py remove_dir --name /opt/tempveracrypt\n\n')

    resolve_dependencies = subparser.add_parser('resolve_dependencies', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Install Veracrypt package and dependencies,\n'
                                 'Arguments: None,\n'
                                 'Usage: python3 burner_lockbox.py resolve_dependencies\n\n')
    
    create_lockbox = subparser.add_parser('create_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a lockbox container,\n'
                                 'Arguments: --name <lockbox name>  --size <size> --type <normal | hidden>,\n' ## verify hidden argument value
                                 'Usage: python3 burner_lockbox.py create_lockbox --name lockboxA.vc --size 25M --type normal \n\n')
    
    mount_lockbox = subparser.add_parser('mount_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Mounts a lockbox container,\n'
                                 'Arguments: --name <lockbox name> --location <mount location>,\n'
                                 'Usage: python3 burner_lockbox.py mount_lockbox --name lockboxA.vc --location /opt/mnt\n\n')
                                 
    list_lockbox = subparser.add_parser('list_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: List lockbox containers,\n'
                                 'Arguments: None,\n'
                                 'Usage: python3 burner_lockbox.py list_lockbox\n\n')
    
    dismount_lockbox = subparser.add_parser('dismount_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Dismounts a lockbox container,\n'
                                 'Arguments: --name <lockbox name>,\n'
                                 'Usage: python3 burner_lockbox.py dismount_lockbox --name lockboxA.vc \n\n')

    upload_lockbox = subparser.add_parser('upload_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Upload a lockbox container to a public repo,\n'
                                 'Arguments: --name <lockbox name> --url <lockbox upload URL>,\n'
                                 'Usage: python3 burner_lockbox.py upload_lockbox --name lockboxA.vc --url https://filebin.net/p5oig73mhgaieu04/\n\n')
                                 
    download_lockbox = subparser.add_parser('download_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Downloads a lockbox container from a public repo,\n'
                                 'Arguments: --name <lockbox name> --url <lockbox download URL>,\n'
                                 'Usage: python3 burner_lockbox.py download_lockbox --name lockboxB.vc --url https://filebin.net/p5oig73mhgaieu04/lockboxA.vc\n\n')
    
    create_dir.add_argument('--name', type=str, required=True)
    
    remove_dir.add_argument('--name', type=str, required=True)
    
    create_lockbox.add_argument('--name', type=str, required=True)
    create_lockbox.add_argument('--password', type=str, required=False)
    create_lockbox.add_argument('--size', type=str, required=True)
    create_lockbox.add_argument('--type', type=str, required=True)
    
    mount_lockbox.add_argument('--name', type=str, required=True)
    mount_lockbox.add_argument('--location', type=str, required=True)
    mount_lockbox.add_argument('--password', type=str, required=False)

    dismount_lockbox.add_argument('--name', type=str, required=True)

    upload_lockbox.add_argument('--name', type=str, required=True)
    upload_lockbox.add_argument('--url', type=str, required=True)

    download_lockbox.add_argument('--name', type=str, required=True)
    download_lockbox.add_argument('--url', type=str, required=True)

    args = parser.parse_args()
    cmd_string = None
    
    if args.function == 'create_dir':
        print('[+] This option will create the following directory:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string)
        cmd_string = 'mkdir' + ' ' + args.name
        
    elif args.function == 'remove_dir':
        print('[+] This option will delete the following directory:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string)
        cmd_string = 'rm -fr' + ' ' + args.name
        
    elif args.function == 'resolve_dependencies': # Need to handle none type iteration exception
        print('[+] This option will install Veracrypt package and dependencies:')
        print('')
        
        pkg_query = 'dpkg-query -W '
        installer = 'apt-get install -y '
        libwixgtk3 = 'libwxgtk3.0-gtk3-0v5 '
        exfat_fuse = 'exfat-fuse '
        exfatprogs = 'exfatprogs '
        add_repo = 'add-apt-repository -y '
        ppa_unit193 = 'ppa:unit193/encryption'
        update_manager = 'apt-get update -y'
        veracrypt = 'veracrypt '
        grep = '| grep '
        wc = '| wc -l'
     
        if run_pkg_check(pkg_query + libwixgtk3 + grep + libwixgtk3 + wc)[0] == '1':
            print('[+] Dependency installed:', libwixgtk3)
        else: 
            print('[+] Installing dependency:', libwixgtk3)
            run_shell_command(installer + libwixgtk3)
         
        if run_pkg_check(pkg_query + exfat_fuse + grep + exfat_fuse + wc)[0] == '1':
            print('[+] Dependency installed:', exfat_fuse)
        else: 
            print('[+] Installing dependency:', exfat_fuse)
            run_shell_command(installer + exfat_fuse)

        if run_pkg_check(pkg_query + exfatprogs + grep + exfatprogs + wc)[0] == '1':
            print('[+] Dependency installed:', exfatprogs)
        else:
            print('[+] Installing dependency: ', exfatprogs)
            run_shell_command(installer + exfatprogs)

        if run_pkg_check(pkg_query + veracrypt + grep + veracrypt + wc)[0] == '1':
            print('[+] Dependency installed:', veracrypt)
        else: 
            print('[+] Installing dependency:', veracrypt)
            run_shell_command(add_repo + ppa_unit193)
            run_shell_command(update_manager)
            run_shell_command(installer + veracrypt)

    elif args.function == 'create_lockbox':
        args.password = get_password()
        cmd_string = 'veracrypt --text --create ' + args.name + ' --size ' + args.size + ' --password ' + args.password + ' --volume-type ' + args.type + ' --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" --random-source /dev/urandom --verbose'
        cmd_string2 = 'veracrypt --text --create ' + args.name + ' --size ' + args.size + ' --volume-type ' + args.type + ' --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" --random-source /dev/urandom --verbose'
        print('[+] This option will create the following lockbox:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string2)
        # veracrypt --text --create vctest.vc --password Ch@ngeM3 --size 200M --volume-type normal --encryption AES --hash sha-512 --filesystem exfat --pim 0 --keyfiles "" --random-source /dev/urandom 
        
    elif args.function == 'mount_lockbox': # Need to handle wrong password
        args.password = get_password()
        cmd_string = 'veracrypt --text --mount ' + args.name + ' ' + args.location + ' --password ' + args.password + ' --pim 0 --keyfiles "" --protect-hidden no'
        cmd_string2 = 'veracrypt --text --mount ' + args.name + ' ' + args.location + ' --pim 0 --keyfiles "" --protect-hidden no'
        print('[+] This option will mount the following lockbox:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string2)
        # veracrypt --text --mount vctest.vc /mnt --password Ch@ngeM3 --pim 0 --keyfiles "" --protect-hidden no --slot 1 --verbose
        
    elif args.function == 'list_lockbox':
        cmd_string = 'veracrypt --text --list'
        print('[+] This option will list mounted lockboxes:')
        print('')
        print('[+] Executing the following command:', cmd_string)
        # veracrypt --text --list
        
    elif args.function == 'dismount_lockbox':
        cmd_string = 'veracrypt --text --dismount ' + args.name
        print('[+] This option will dismount the following lockbox:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string)
        # veracrypt --text --dismount vctest.vc
        
    elif args.function == 'upload_lockbox':
        cmd_string = 'curl -T ' + args.name + ' ' + args.url
        print('[+] This option will upload the following lockbox:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string)
        # curl -T monocacygatewayplan800w.jpg https://filebin.net/p5oig73mhgaieu04/
        
    elif args.function == 'download_lockbox':
        cmd_string = 'curl -L ' + args.url + ' --output ' + args.name
        print('[+] This option will download the following lockbox:', args.name)
        print('')
        print('[+] Executing the following command:', cmd_string)
        # curl -L https://filebin.net/p5oig73mhgaieu04/lockbox.vc
    
    return cmd_string

def get_password():
    try:
        password_entry1 = '123PASSWORD'
        password_entry2 = 'PASSWORD123'
        while password_entry1 not in password_entry2:
            password_entry1 = getpass.getpass(prompt='Enter the encryption password: ')
            password_entry2 = getpass.getpass(prompt='Confirm the encryption password: ')
            print('')
        return password_entry1
    except Exception as error:
        print('ERROR', error)
 
def run_shell_command(shell_cmd):
    if shell_cmd is not None: 
        try:
            pro = subprocess.run(shell_cmd, capture_output=True, text=True, shell=True)
            if pro.stdout:
                return f"---------------STDOUT Detail---------------\n {pro.stdout}"
            elif pro.stderr:
                return f"---------------STDERR Detail---------------\n {pro.stderr}"
            else:
                return f"[+] Executed"
        except Exception as ex:
            print("exception occurred", ex)
            return f"   [subprocess broke]"
    #else:
        #break
     
def run_pkg_check(shell_cmd):
    try:
        pro = subprocess.run(shell_cmd, capture_output=True, text=True, shell=True)
        if pro.stdout:
            exit_code = pro.stdout.split('\n')
            return exit_code
        elif pro.stderr:
            error_info = pro.stderr
            return error_info
        else:
            return f"[+] Executed"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"

if __name__ == '__main__':
    
    print("-----------------------------------------------------------------------------------------------------------")
    
    cmd = parseArguments()
    # print(type(cmd))
    output = run_shell_command(cmd)
    print(output)
    
    print("----------------------------------------------------------------------------------------------------------")
    

