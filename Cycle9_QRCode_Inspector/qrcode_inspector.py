#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import argparse
import os
import base64
import requests
import json
import subprocess
import urllib.parse

def fetch_virus_total_record(hostname: str, api_key: str) -> dict[str, any]:
  
  headers = {"x-apikey": api_key}
  encoded_hostname = base64.b64encode(hostname.encode("utf8")).decode("utf8").replace("=", "")
  url = f"https://www.virustotal.com/api/v3/urls/{encoded_hostname}"
  response = requests.get(url, headers=headers)

  return response.json()

        
def run_shell_command(shell_cmd):
    if shell_cmd is not None: 
        try:
            pro = subprocess.run(shell_cmd, capture_output=True, text=True, shell=True)
            if pro.stdout:
                return f"---------------Open Services---------------\n {pro.stdout}", pro.stdout
            elif pro.stderr:
                return f"---------------STDERR Detail---------------\n {pro.stderr}"
        except Exception as ex:
            print("exception occurred", ex)
            return f"   [subprocess broke]"

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = 'QRCode Inspector Usage Details:',\
                                 usage = '       python3 qrcode_inspector.py localFile -f|--file <local_file_path>,\n\n')
subparser = parser.add_subparsers(dest = 'command')
localFile = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Inspect local QR Code image file,\n'
                    'Usage Example: python3 qrcode_inspector.py localFile -f ./image1.jpg \n'
                    '               python3 qrcode_inspector.py localFile --file ./image1.jpg \n\n')
localFile.add_argument('-f', '--file', action = 'store', type=str, dest = 'input_file', required = True)
parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')
args = parser.parse_args()


qrcode_local_file = None
qrcode_file_obj = None
qrcode_decoded_url = None
qrcode_decoded_hostname = None
virus_total_apikey = input("Enter the Virus Total API Key :")

if args.command == 'localFile':
    # Troubleshooting code
    print(os.path.exists(args.input_file))
    print("")

    qrcode_local_file = args.input_file
    
    if args.input_file and os.path.exists(args.input_file):
        print(f"[+] Reading the following QR Code file:\n {os.path.basename(args.input_file)}")
        qrcode_file_obj = cv2.imread(qrcode_local_file)
        print("QR Code File Object:\n ", qrcode_file_obj)
        print("")
    
    # Initialize the cv2 QRCode detector
    print("[+] Initializing decoder........................")
    detector = cv2.QRCodeDetector()
    print("")
          
    # Detect and decode
    print("[+] Extracting content............................")
    data, vertices_array, binary_qrcode = detector.detectAndDecode(qrcode_file_obj)
    print("")
    
    qrcode_decoded_url = data
    
    # Troubleshooting code
    '''
    print("QR Code Vertices Array:\n ", vertices_array)
    print("")
    print("QR Code Binary Data:\n ", binary_qrcode)
    print("")
    print("QR Code Data:\n ", data)
    print("")
    '''
  
    # Get hostname
    qrcode_decoded_hostname = urllib.parse.urlparse(qrcode_decoded_url)
 
    print(qrcode_decoded_hostname)
    print("The hostname is :", qrcode_decoded_hostname.netloc)
    
    headers = {"x-apikey": virus_total_apikey}
    encoded_hostname = base64.b64encode(qrcode_decoded_hostname.netloc.encode("utf8")).decode("utf8").replace("=", "")
    virus_total_url = f"https://www.virustotal.com/api/v3/urls/{encoded_hostname}"
    virus_total_response = requests.get(virus_total_url, headers=headers)
    json_data = virus_total_response.json())
    json_object = json.loads(json_data)
    json_formatted_str = json.dumps(json_object, indent=2)
    print(json_formatted_str)
    
else:
    print('Error: Verify command arguments and run the program again')
