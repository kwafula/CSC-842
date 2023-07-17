#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import argparse
import os
import base64
import requests
import json
import urllib.parse

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
virus_total_apikey = input("Enter the Virus Total API Key : ")
print("")

if args.command == 'localFile':
    # Troubleshooting code
    # print(os.path.exists(args.input_file))
    # print("")

    qrcode_local_file = args.input_file
    
    if args.input_file and os.path.exists(args.input_file):
        print(f"[+] Reading the following QR Code file:\n {os.path.basename(args.input_file)}")
        qrcode_file_obj = cv2.imread(qrcode_local_file)

        # Troubleshooting code
        # print("QR Code File Object:\n ", qrcode_file_obj)
        # print("")
    
    # Initialize the cv2 QRCode detector
    print("[+] Initializing decoder........................")
    detector = cv2.QRCodeDetector()
    print("")
          
    # Detect and decode
    print("[+] Decoding content............................")
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
  
    # Troubleshooting code
    # print(qrcode_decoded_hostname)
    # print("The hostname is :", qrcode_decoded_hostname.netloc)
    # print("")
    
    headers = {"x-apikey": virus_total_apikey}
    encoded_hostname = base64.b64encode(qrcode_decoded_hostname.netloc.encode("utf8")).decode("utf8").replace("=", "")
    virus_total_url = f"https://www.virustotal.com/api/v3/urls/{encoded_hostname}"
    virus_total_response = requests.get(virus_total_url, headers=headers)
    json_data = virus_total_response.json()
    virus_total_report_data = json.dumps(json_data, sort_keys=True, indent=4)
    print(virus_total_report_data)
    print("")

    base = os.path.basename(qrcode_local_file)
    virus_total_report_file = os.path.splitext(base)[0]
    
    with open((virus_total_report_file + "json"), mode="w") as file_obj: 
        json.dump(json_data, file_obj)
    
else:
    print('Error: Verify command arguments and run the program again')
