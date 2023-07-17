#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
# import numpy as np
# import time
import argparse
import os
# import base64
# import requests
# import shutil
import subprocess


# Configure Virus Total API Key

# Read file from local file system, return file object
def read_file(file_name):
    with open(file_name, mode="r", encoding="utf8") as file_obj:
        file_data = file_obj.read()
        return file_data

# Function to write data file
# Excluding the encoding="utf8" argument, not sure how it might image QR Code data
def write_file(file_name, file_data):
    with open(file_name, mode="wb") as file_obj: 
        file_obj.write(file_data)
        file_obj.close()
        return 
        
def run_shell_command(shell_cmd):
    if shell_cmd is not None: 
        try:
            pro = subprocess.run(shell_cmd, capture_output=True, text=True, shell=True)
            if pro.stdout:
                return pro.stdout
            elif pro.stderr:
                return f"---------------STDERR Detail---------------\n {pro.stderr}"
        except Exception as ex:
            print("exception occurred", ex)
            return f"   [subprocess broke]"
        
# Run hash of image file, return image file hash (QA test if image file hash is the same for manual download and script download) 

# Extract QR Code URL and Domain, return URL and Domain

# Check if image file is QR Code, if QR Code, return QR Code image file object 

# Check if QR Code content has URL content, if yes, return image file hash, URL, domain, and IP Address,
#     else, display QR Code content for manual review to decide if it should be saved for offline analysis

# Run URL, hash, domain, and IP Address checks in VirusTotal sequentially, returns results sequentially


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
qrcode_file_hash = None
qrcode_file_obj = None
qrcode_decoded_url = None
qrcode_decoded_domain = None
qrcode_decoded_ip = None

if args.command == 'localFile':
    # Troubleshooting code
    print(os.path.exists(args.input_file))
    print("")
    if args.input_file and os.path.exists(args.input_file):
        print(f"[+] Reading the following QR Code file:\n {os.path.basename(args.input_file)}")
        qrcode_local_file = args.input_file
        qrcode_file_obj = cv2.imread(qrcode_local_file)
        print("QR Code File Object:\n ", qrcode_file_obj)
        print("")
    
    # Get file hash
    sha256_set_cmd = "sha256=$(sha256sum " + qrcode_local_file + ")" + " | cut -f 1 -d ' '"
    qrcode_file_hash = run_shell_command(sha256_set_cmd)
    print(sha256_set_cmd)
    sha256_echo_cmd = "echo $sha256"
    qrcode_file_hash = run_shell_command(sha256_echo_cmd)
    print(qrcode_file_hash)
    sha256_unset_cmd = "unset sha256"
    qrcode_file_hash = run_shell_command(sha256_unset_cmd)
    
    # Initialize the cv2 QRCode detector
    print("[+] Initializing decoder........................")
    detector = cv2.QRCodeDetector()
    print("")
          
    # Detect and decode
    print("[+] Extracting content............................")
    data, vertices_array, binary_qrcode = detector.detectAndDecode(qrcode_file_obj)
    print("")

    # Troubleshooting code
    print("QR Code Vertices Array:\n ", vertices_array)
    print("")
    print("QR Code Binary Data:\n ", binary_qrcode)
    print("")
    print("QR Code Data:\n ", data)
    print("")
else:
    print('Error: Verify command arguments and run the program again')
