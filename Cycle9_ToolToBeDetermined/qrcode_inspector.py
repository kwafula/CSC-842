#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import numpy as np
import time
import argparse
import os
import base64

# # # Product Backlog: QR Code Inspector
# 1. Install dependencies
# 2. Load image file from the file system
# 3. Download image file from the internet
# 4. Scrap image file from a webpage
# 5. Check if image file is QR Code Code
# 6. Decode QR Code into a buffer
# 7.a. Check if decoded buffer content is URL
# 7.b. Check URL and domain against VirusTotal
# 8.a. Check if decoded buffer content is a binary file
# 8.b. Hash the file from the buffer if possible or from disk
# 8.c. Check the hash against VirusTotal
# 9.a. If decoded buffer content is a script or obfuscated
# 9.b. Dump to disk for further offline analysis with other tools





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

    # Initialize data and QR Code
    qr_percel = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    print("[+] Initializing QR Code..............................................")
    print("")
    qr_percel.add_data(source_data_base64_string)
    qr_percel.make(fit = True)
    print("[+] Encoding base64 string into QR Codes..............................................")
    print("")
    
    ### Troubleshooting code
    # Print the QR Code image size (version)
    # print('Size of the QR image(Version):')
    # print(np.array(qr_percel.get_matrix()).shape)
    # print("")

    # Encode data into QR Code
    #icon = qr_percel.make_image(back_color = (255, 195, 235), fill_color=(55, 95, 35))  # (21, 18, 29), fill_color=(0, 0, 0)) , (36, 31, 49), fill_color=(0, 0, 0)), (255, 255, 255), fill_color=(0, 0, 0))
    icon = qr_percel.make_image(back_color = (255, 255, 255), fill_color=(0, 0, 0))
    print("[+] Creating QR Code..............................................")
    print("")

    # Convert QR Code to RGBA
    icon = icon.convert('RGBA')
    
    ### Testing code for QR Code without logo
    icon_test = icon 
    icon_test.save('./myapp-no-logo.png') 
    
    # Load logo image test
    image_file = args.image_file
    # icon_logo = image_read(image_file) # image_read() function not used, PIL library closes pointer as soon as the function call exits with AttributeError: 'NoneType' object has no attribute 'seek'
    # Making direct call
    icon_logo = Image.open(image_file)
    print(f"[+] Reading the following file:\n {os.path.basename(image_file)}")
    print("")
