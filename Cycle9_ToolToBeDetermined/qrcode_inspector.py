#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
# import numpy as np
import time
import argparse
import os
# import base64
import requests


# Configure Virus Total API Key

# Read file from local file system, return file object
def read_file(file_name):
    with open(file_name, mode="r", encoding="utf8") as file_obj:
        file_data = file_obj.read()
        return file_data

# Download image file from URL, return image file object

# Scrape website and download enumerated image file(s), return image file object(s)

# Decode QR Code content, return QR Code content object

# Save URL-based QR Code file object with a naming convention that will persist for the session, return file location (path and name)

# Save Non-URL-Based QR Code file for later manual analysis

# Run hash of image file, return image file hash (QA test if image file hash is the same for manual download and script download) 

# Extract QR Code URL and Domain, return URL and Domain

# Check if image file is QR Code, if QR Code, return QR Code image file object 

# Check if QR Code content has URL content, if yes, return image file hash, URL, domain, and IP Address,
#     else, display QR Code content for manual review to decide if it should be saved for offline analysis

# Run URL, hash, domain, and IP Address checks in VirusTotal sequentially, returns results sequentially


parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = 'QRCode Inspector Usage Details:',\
                                 usage = 'python3 qrcode_inspector.py addService -s|--service <service-name> -a|--api <service-api> -k|--key <service-api-key>,\n'
                                 '       python3 qrcode_inspector.py deleteService -s|--service <service-name> -a|--api <service-api> -k|--key <service-api-key>,\n'
                                 '       python3 qrcode_inspector.py readServices,\n'
                                 '       python3 qrcode_inspector.py localFile -f|--file <local_file_path>,\n'
                                 '       python3 qrcode_inspector.py remoteFile -u|--url <remote_file_url>,\n'
                                 '       python3 qrcode_inspector.py remoteScrape -u|--url <remote_website_url>,\n\n')
subparser = parser.add_subparsers(dest = 'command')

addService = subparser.add_parser('addKey', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Add CTI service for analysis,\n'
                    'Usage Example: python3 qrcode_inspector.py addService -s "Virus Total" -a "https://www.virustotal.com/api/v3/urls" -k "abcd123" \n'
                    '               python3 qrcode_inspector.py addService --service "Virus Total" --api "https://www.virustotal.com/api/v3/urls" --key "abcd123" \n\n')

deleteService = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Delete configured CTI service,\n'
                    'Usage Example: python3 qrcode_inspector.py deleteService -s "Virus Total" -a "https://www.virustotal.com/api/v3/urls" -k "abcd123" \n'
                    '               python3 qrcode_inspector.py deleteService --service "Virus Total" --api "https://www.virustotal.com/api/v3/urls" --key "abcd123" \n\n')

readServices = subparser.add_parser('readServices', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Read configured CTI services,\n'
                    'Usage Example: python3 qrcode_inspector.py readServices \n\n')

localFile = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Inspect local QR Code image file,\n'
                    'Usage Example: python3 qrcode_inspector.py localFile -f ./image.png \n'
                    '               python3 qrcode_inspector.py localFile --file ./image.png \n\n')

remoteFile = subparser.add_parser('remoteFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Download and inspect remote QR Code image file,\n'
                    'Usage Example: python3 qrcode_inspector.py remoteFile -u "https://github.com/kwafula/CSC-842/blob/main/Cycle7_QRCode_Courier/logo3.png"\n'
                    '               python3 qrcode_inspector.py remoteFile --url "https://github.com/kwafula/CSC-842/blob/main/Cycle7_QRCode_Courier/logo3.png"\n\n')

remoteScrape = subparser.add_parser('remoteScrape', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Scrape remote website and inspect enumerated QR Code image files,\n'
                    'Usage Example: python3 qrcode_inspector.py remoteScrape -u "https://github.com/kwafula/kwafula.github.io" \n'
                    '               python3 qrcode_inspector.py remoteScrape --url "https://github.com/kwafula/kwafula.github.io" \n\n')

addService.add_argument('-s', '--service', action = 'store', type=str, dest = 'cti_service_name', required = True)
addService.add_argument('-a', '--api', action = 'store', type=str, dest = 'cti_service_name', required = True)
addService.add_argument('-k', '--key', action = 'store', type=str, dest = 'service_api_key', required = True)

deleteService.add_argument('-s', '--service', action = 'store', type=str, dest = 'cti_service_name', required = True)
deleteService.add_argument('-a', '--api', action = 'store', type=str, dest = 'cti_service_name', required = True)
deleteService.add_argument('-k', '--key', action = 'store', type=str, dest = 'service_api_key', required = True)

localFile.add_argument('-f', '--file', action = 'store', type=str, dest = 'input_file', required = True)

remoteFile.add_argument('-r', '--url', action = 'store', type=str, dest = 'input_url', required = True)

remoteScrape.add_argument('-u', '--url', action = 'store', type=str, dest = 'input_url', required = True)

parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')

args = parser.parse_args()

qrcode_file_path = None
qrcode_file_hash = None
qrcode_file_obj = None
qrcode_decoded_url = None
qrcode_decoded_domain = None
qrcode_decoded_ip = None
'''
if args.command == 'localFile':
    print("[+] Reading local file..............................")
    print("")
    # Load data from local QR Code file
    qrcode_file_path = args.input_file
    qrcode_decoded_data = Image.open(str(qrcode_file_path))
    print(qrcode_decoded_data)
'''
if args.command == 'localFile':
    # Troubleshooting code
    print(os.path.exists(args.input_file))
    print("")
    if args.input_file and os.path.exists(args.input_file):
        qrcode_file_path = args.input_file
        print(f"[+] Reading the following file:\n {os.path.basename(qrcode_file_path)}")
        qrcode_file_obj = cv2.imread(qrcode_file_path)
        print("QR Code File Object:\n ", qrcode_file_obj)
        print("")
        print("")
    
    # FIlE HASH FUNCTION HERE 
    
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

    '''
    # If there is a QR code, decode and print the data
    output_file = args.output_file
    if vertices_array is not None:
        print("[+] Decoding content..............................")
        print("")
        source_data_base64_string = data
        print(f"[+] Reading base64 string:\n {source_data_base64_string}")
        print("")
        source_data_base64_bytes = source_data_base64_string.encode("ascii")
        print(f"[+] Econding base64 string into base64 bytes:\n {source_data_base64_bytes}")
        print("")
        source_data_ascii_bytes = base64.b64decode(source_data_base64_bytes)
        print(f"[+] Decoding base64 bytes into ascii bytes:\n {source_data_ascii_bytes}")
        print("")
        source_data = source_data_ascii_bytes.decode("ascii")
        print(f"[+] Decoding ascii bytes into plaintext string: {source_data}")
        print('[+] Writing file the following file to the following disk location:\n ', output_file)
        write_file(output_file, source_data)
    '''
else:
    print('Error: Verify command arguments and run the program again')
# https://github.com/Entity0x1A/QR-Code-Compromise
# https://www.onsecurity.io/blog/how-i-made-rapid7s-project-sonar-searchable/
# https://docs.umbrella.com/investigate/docs/passive-dns
# https://0xpatrik.com/project-sonar-guide/
