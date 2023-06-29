#!/usr/bin/env python3 

import qrcode
from PIL import icon

#####Install Dependecies##
# pip install qrcode
# And
# pip install pillow
# OR
# pip install "qrcode[pil]"

#####Product Backlog#####
# 00 # Install dependecies
# 01 # Create QR Code
# 02 # Specify QR Code back color, fill color, box_size, and border
# 03 # Add logo to QR Code 
# 04 # Read text from file
# 05 # Obfuscate read text
# 06 # Add text to QR Code
# 07 # Name QR with a .ico extension
# 08 # Read obsfuscated text from QR Code
# 09 # Deobfuscate read text

# File read
def read_script(file_name):
    with open(file_name, mode="r", encoding="utf8") as script_obj:
        script_data = script_obj.read()
        # print(script_data)
        return script_data

# Load icon image
icon_file = input("Enter the file name of the icon including the path i.e. /home/usernam/icon.jpg")
icon_image = icon_file
icon_image = icon.open(icon_file)

# Setting base width
basewidth = 100
 
# Adjust image size ## and revise the to standard size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), image.ANTIALIAS) 

# Load code from script
script_file = input("Enter the file name of the script including the path i.e. /home/usernam/script_code.py")
script_code = read_script(script_file)


