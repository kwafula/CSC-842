#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import numpy as np
import time
import argparse
import os
import base64

### Product Backlog: QR Code Inspector
##### Functions #####
# Configure Virus Total API Key

# Load image file(s) from local file system, return image file object(s)

# Download image file(s) from URL, return image file object(s)

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
                                 usage = 'python3 qrcode_inspector.py addKey -s <service: "Virus Total" | "Other Sevice N1" | "Other Sevice N2" | ....> -k <api-key>,\n'
                                 '       python3 qrcode_inspector.py deleteKey -s <service: "Virus Total" | "Other Sevice N1" | "Other Sevice N2" | ....> -k <api-key>,
                                 '       python3 qrcode_inspector.py readKey -s <service: "Virus Total" | "Other Sevice N1" | "Other Sevice N2" | ....> -k <api-key>,\n'
                                 '       python3 qrcode_inspector.py localFile -f <local_file_path>,\n'
                                 '       python3 qrcode_inspector.py remoteFile -u <remote_file_url>,\n'
                                 '       python3 qrcode_inspector.py remoteCrawl -u <remote_website_url>,\n'
subparser = parser.add_subparsers(dest = 'command')

localFile = subparser.add_parser('localFile', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Inspect local QR Code image file,\n'
                    'Usage Example: python3 qrcode_inspector.py localFile -f ./input-datafile.png -i \n\n')

decode = subparser.add_parser('decode', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Read the icon to decode and extract embedded data,\n'
                    'Usage Example: sudo python3 qrcode_courier.py decode -i ./myapp.png -d ./output_datafile.txt \n\n')

localFile.add_argument('-f', '--file', action = 'store', type=str, dest = 'local_file_path', required = True)

decode.add_argument('-i', action = 'store', type=str, dest = 'image_file', required = True)
decode.add_argument('-d', action = 'store', type=str, dest = 'output_file', required = True)

parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')

args = parser.parse_args()

if args.command == 'localFile':
    print("[+] Reading local file..............................")
    print("")
    # Load data from local QR Code file
    local_file_path = args.local_file_path
    source_data = read_file(str(local_file_path))


# https://github.com/Entity0x1A/QR-Code-Compromise
# https://www.onsecurity.io/blog/how-i-made-rapid7s-project-sonar-searchable/
# https://docs.umbrella.com/investigate/docs/passive-dns
# https://0xpatrik.com/project-sonar-guide/
