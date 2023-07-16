#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import numpy as np
import time
import argparse
import os
import base64

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

# Check if QR Code content has URL content, if yes, return image file hash, URL, domain, historical ip associated with domain (nexpose passive dns db) else, display QR Code content for manual review to decide if shoul be save for late analysis

# Run URL, hash, domain, IP Address checks in VirusTotal sequentially, returns results sequentially


parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = 'QRCode Inspector Usage Details:',\
                                 usage = 'python3 qrcode_inspector.py addService -s|--service <service-name> -a|--api <service-api> -k|--key <service-api-key>,\n'
                                 '       python3 qrcode_inspector.py deleteService -s|--service <service-name> -a|--api <service-api> -k|--key <service-api-key>,\n'
                                 '       python3 qrcode_inspector.py readServices,\n'
                                 '       python3 qrcode_inspector.py localFile -f|--file <local_file_path>,\n'
                                 '       python3 qrcode_inspector.py remoteFile -u|--url <remote_file_url>,\n'
                                 '       python3 qrcode_inspector.py remoteCrawl -u|--url <remote_website_url>,\n'
subparser = parser.add_subparsers(dest = 'command')

addService = subparser.add_parser('addKey', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Add CTI service for analysis,\n'
                    'Usage Example: python3 qrcode_inspector.py addService -s "Virus Total" -a "https://www.virustotal.com/api/v3/urls" -k "abcd123" \n
                    '               python3 qrcode_inspector.py addService --service "Virus Total" --api "https://www.virustotal.com/api/v3/urls" --key "abcd123\n\n')

deleteService = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Delete configured CTI service,\n'
                    'Usage Example: python3 qrcode_inspector.py deleteService -s "Virus Total" -a "https://www.virustotal.com/api/v3/urls" -k "abcd123" \n
                    '               python3 qrcode_inspector.py deleteService --service "Virus Total" --api "https://www.virustotal.com/api/v3/urls" --key "abcd123\n\n')

readServices = subparser.add_parser('readServices', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Read configured CTI services,\n'
                    'Usage Example: python3 qrcode_inspector.py readServices \n\n')

localFile = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Inspect local QR Code image file,\n'
                    'Usage Example: python3 qrcode_inspector.py localFile -f ./image.png \n')
                    '               python3 qrcode_inspector.py localFile --file ./image.png \n\n')

remoteFile = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Download and inspect remote QR Code image file,\n'
                    'Usage Example: python3 qrcode_inspector.py remoteFile -u "https://github.com/kwafula/CSC-842/blob/main/Cycle7_QRCode_Courier/logo3.png"\n')
                    '               python3 qrcode_inspector.py remoteFile --url "https://github.com/kwafula/CSC-842/blob/main/Cycle7_QRCode_Courier/logo3.png"\n\n')

remoteCrawl = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Scrape remote website and inspect enumerated QR Code image files,\n'
                    'Usage Example: python3 qrcode_inspector.py localFile -u "https://github.com/kwafula/kwafula.github.io" \n')
                    '               python3 qrcode_inspector.py localFile --url "https://github.com/kwafula/kwafula.github.io" \n\n')

addKey.add_argument('-s', '--service', action = 'store', type=str, dest = 'cti_service_name', required = True)
addKey.add_argument('-a', '--api', action = 'store', type=str, dest = 'cti_service_name', required = True)
addKey.add_argument('-k', '--key', action = 'store', type=str, dest = 'service_api_key', required = True)

deleteKey.add_argument('-s', '--service', action = 'store', type=str, dest = 'cti_service_name', required = True)
deleteKey.add_argument('-a', '--api', action = 'store', type=str, dest = 'cti_service_name', required = True)
deleteKey.add_argument('-k', '--key', action = 'store', type=str, dest = 'service_api_key', required = True)

readKey.add_argument('-s', '--service', action = 'store', type=str, dest = 'cti_service_name', required = True)
readKey.add_argument('-a', '--api', action = 'store', type=str, dest = 'cti_service_name', required = True)
readKey.add_argument('-k', '--key', action = 'store', type=str, dest = 'service_api_key', required = True)

localFile.add_argument('-f', '--file', action = 'store', type=str, dest = 'input_file', required = True)

remoteFile.add_argument('-r', '--url', action = 'store', type=str, dest = 'input_url', required = True)

remoteCrawl.add_argument('-u', '--url', action = 'store', type=str, dest = 'input_url', required = True)

parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')

args = parser.parse_args()

qrcode_file_path = None
qrcode_file_hash = None
qrcode_decoded_data = None
qrcode_decoded_url = None
qrcode_decoded_domain = None
qrcode_decoded_ip = None

if args.command == 'localFile':
    print("[+] Reading local file..............................")
    print("")
    # Load data from local QR Code file
    qrcode_file_path = args.input_file
    qrcode_decoded_data = Image.open(str(qrcode_file_path))
    print(qrcode_decoded_data)


# https://github.com/Entity0x1A/QR-Code-Compromise
# https://www.onsecurity.io/blog/how-i-made-rapid7s-project-sonar-searchable/
# https://docs.umbrella.com/investigate/docs/passive-dns
# https://0xpatrik.com/project-sonar-guide/
