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


parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = 'QRCode Courier Usage Details:',\
                                 usage = 'sudo python3 qrcode_courier.py encode -s <input_file> -i <image_file> -d <output_file>,\n'
                                 '       sudo python3 qrcode_courier.py decode -i <image_file> -d <output_file>,\n')
subparser = parser.add_subparsers(dest = 'command')

encode = subparser.add_parser('encode', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Encode source data in a QRCode and generate an icon,\n'
                    'Usage Example: sudo python3 qrcode_courier.py encode -s ./input-datafile.txt -i ./gihhub.png -d ./myapp.png \n\n')

decode = subparser.add_parser('decode', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Read the icon to decode and extract embedded data,\n'
                    'Usage Example: sudo python3 qrcode_courier.py decode -i ./myapp.png -d ./output_datafile.txt \n\n')

encode.add_argument('-s', action = 'store', type=str, dest = 'input_file', required = True)
encode.add_argument('-i', action = 'store', type=str, dest = 'image_file', required = True)
encode.add_argument('-d', action = 'store', type=str, dest = 'output_file', required = True)

decode.add_argument('-i', action = 'store', type=str, dest = 'image_file', required = True)
decode.add_argument('-d', action = 'store', type=str, dest = 'output_file', required = True)

parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')

args = parser.parse_args()

if args.command == 'encode':
    print("[+] Encoding content..............................")
    print("")
    # Load data from a file
    input_file = args.input_file
    source_data = read_file(str(input_file))
    print(f"[+] Reading the following file:\n {os.path.basename(input_file)}")
    print("")
    print(f"[+] Reading plaintext string: {source_data}")
    source_data_ascii_bytes = source_data.encode("ascii")
    print(f"[+] Encoding plaintext string into ascii bytes:\n {source_data_ascii_bytes}")
    print("")
    source_data_base64_bytes = base64.b64encode(source_data_ascii_bytes)
    print(f"[+] Encoding ascii bytes into base64 btyes:\n {source_data_base64_bytes}")
    print("")
    source_data_base64_string = source_data_base64_bytes.decode("ascii")
    print(f"[+] Decoding base64 bytes into base64 string:\n {source_data_base64_string}")
    print("")


# https://github.com/Entity0x1A/QR-Code-Compromise
# https://www.onsecurity.io/blog/how-i-made-rapid7s-project-sonar-searchable/
# https://docs.umbrella.com/investigate/docs/passive-dns
# https://0xpatrik.com/project-sonar-guide/
