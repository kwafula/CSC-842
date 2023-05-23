#!/usr/bin/env python3

from datetime import datetime
import sys
import time
import subprocess
import nvdlib

#global exitcode 
#exitcode = "No"
global command
command = ' '

print('Started WebApp Attack Vector Enumerator. For menu options, type < 1 > at the prompt (without angle brackets): ')

def run_nmap_scan(com):
    try:
        pro = subprocess.run(com, capture_output=True, text=True, shell=True)#, shell=True,env=myenv,executable='/bin/bash')#
        if pro.stdout:
            return f"---------------Open Services---------------\n {pro.stdout}"
        elif pro.stderr:
            return f"---------------error----------------\n {pro.stderr}"
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"

def run_nvd_query(srvc_prod_name):
    cve_list = nvdlib.cve.searchCVE(keywordExactMatch=True, keywordSearch= srvc_prod_name, key='f409e6f3-b5eb-4487-a95e-584c5d7edadb')
    for each_cve in cve_list:
        print('CVE ID: ' + str(each_cve.id) + ' ----> '+ 'Common Platform Enumeration: ' + str(each_cve.cpe[0]) + '\n')

def run_exploitdb_query(cveid):
    try:
        pro = subprocess.run(cveid, capture_output=True, text=True, shell=True)#, shell=True,env=myenv,executable='/bin/bash')#
        if pro.stdout:
            return f"---------------Associated Exploits---------------\n {pro.stdout}"
        elif pro.stderr:
            return f"---------------error----------------\n {pro.stderr}"
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"

def run_exploit_detail(edbid):
    try:
        pro = subprocess.run(edbid, capture_output=True, text=True, shell=True)#, shell=True,env=myenv,executable='/bin/bash')#
        if pro.stdout:
            return f"---------------Exploit/Shellcode Detail---------------\n {pro.stdout}"
        elif pro.stderr:
            return f"---------------error----------------\n {pro.stderr}"
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"

while True:
    command = ' '
    menu_option = input('Enter your menu selection e.g. 1 for Help Menu or 8 for Exit >>>: ')
    if '1' in menu_option:
        print('-'*100)
        print('++++++++++++++++++++++Help Menu+++++++++++++++++++++++++++++++')
        print(' ')
        print(' 1: Display Help Menu')
        print(' 2: Enumerate Services')
        print(' 3: Enumerate CVEs')
        print(' 4: Enumerate Exploits/Shellcode')
        print(' 5: Display Exploit/Shellcode Path')
        print(' 6: Automate Steps 1, 2, and 3')
        print(' 7: Display Exploit Details')
        print(' 8: Exit')
        print('-'*100)
        print(' ')
    elif '2' in menu_option:
        host = input('Enter the web application DNS domain name or IP Address e.g xyz.com, 1.2.4.5 >>>: ')
        command = 'nmap -sV -T4 -F -Pn %s | grep open' %host
        print('Executing the web application service scan')
        nmap_results = run_nmap_scan(command)
        print(nmap_results)
    elif '3' in menu_option:
        service_product_name = input('Enter the service name including the version number e.g OpenSSH 6.4, Apache httpd 2.2 >>>: ')
        print('Executing the NVD CVE-ID query')
        cve_results = run_nvd_query(service_product_name)
        print(cve_results)
    elif '4' in menu_option:
        cve_id = input('Enter the CVE-ID corresponding to product the version number, exlude the "CVE-" prefix e.g 2018-16905 >>>: ')
        #cve_id = cve_id[4:]
        exploitdb_cmd = 'searchsploit --cve %s --id' %cve_id
        print('Executing the ExploitDB CVE-ID query \n')
        exploit_results = run_exploitdb_query (exploitdb_cmd)
        print(exploit_results)
    elif '5' in menu_option:
        edb_id = input('Enter the EDB-ID corresponding to product the version number e.g 16905 >>>: ')
        exploitdb_cmd = 'searchsploit --path %s' %edb_id
        print('Executing the ExploitDB EDB-ID query \n')
        exploit_path_results = run_exploitdb_query(exploitdb_cmd)
        print(exploit_path_results)
    elif '6' in menu_option:
        host = input('Enter the web application DNS domain name or IP Address e.g xyz.com, 1.2.4.5 >>>: ')
        print('Executing automated web application service scan \n')
        nmap_xml_cmd = 'nmap -sV -T4 -F -Pn %s -oX /opt/csc-842/01-attack-surface-enumerator/nmap-output-%s.xml' %(host, host)
        automated_nmap_results = run_nmap_scan(nmap_xml_cmd)
        print('Executing automated ExploitDB query \n')
        exploitdb_xml_cmd = 'searchsploit --nmap /opt/csc-842/01-attack-surface-enumerator/nmap-output-%s.xml' %host
        automated_exploitdb_results = run_exploitdb_query(exploitdb_xml_cmd)
        print(automated_nmap_results)
        print(automated_exploitdb_results)
    elif '7' in menu_option:
        edb_id = input('Enter the EDB-ID corresponding to product the version number e.g 16905 >>>: ')
        print('Preparing Exploit/Shellcode details')
        exploitdetail_cmd = 'searchsploit --examine %s' %edb_id
        exploit_detail_results = run_exploit_detail(exploitdetail_cmd)
        print(exploit_detail_results)
    elif '8' in menu_option:
        quit()
    else:
        print('Error: Entered selection not a menu option, please enter on of the menu options: ')
        pass
