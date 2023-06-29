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
# 01 # Create QR Code
# 02 # Specify QR Code back color, fill color, box_size, and border
# 03 # Add logo to QR Code 
# 04 # Read text from file
# 05 # Obfuscate read text
# 06 # Add text to QR Code
# 07 # Name QR with a .ico extension
# 08 # Read obsfuscated text from QR Code
# 09 # Deobfuscate read text

def read_script(<filename>):
    with open(<filename>, mode="r", encoding="utf8") as script_obj:
        script_data = script_obj.read()
        # print(script_data)

# Load icon image
icon_image = '<add_icon_image.jpg>'
icon_image = icon.open(<add_icon_image.jpg>)

# taking base width
basewidth = 100
 
# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), image.ANTIALIAS)

