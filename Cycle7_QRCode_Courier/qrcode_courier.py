#!/usr/bin/env python3 

#### Resources
# https://me-qr.com/qr-code-generator/
# https://qrcoderaptor.com/
# https://www.geeksforgeeks.org/generate-qr-code-using-qrcode-in-python/
# https://pypi.org/project/qrcode/
# https://www.geeksforgeeks.org/how-to-generate-qr-codes-with-a-custom-logo-using-python/
# https://pypi.org/project/deopy/
# https://gist.github.com/ctokheim/6c34dc1d672afca0676a
# https://medium.com/geekculture/python-source-code-obfuscation-6b97f88a460d
# https://therenegadecoder.com/code/how-to-obfuscate-code-in-python/
# https://github.com/QQuick/Opy
# https://liftoff.github.io/pyminifier/index.html
# https://pypi.org/project/python-minifier/
# https://github.com/Hnfull/Intensio-Obfuscator/blob/master/src/intensio_obfuscator/obfuscation_examples/python/basic/output/basicRAT-example/basicRAT_client.py
# https://towardsdatascience.com/create-and-read-qr-code-using-python-9fc73376a8f9
# https://github.com/3CORESec/testmynids.org

import qrcode
from PIL import icon
import cv2

#####Install Dependecies##
# pip install qrcode
# And
# pip install pillow
# OR
# pip install "qrcode[pil]"
# pip install cv2

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
icon = icon.resize((basewidth, hsize), image.ANTIALIAS) 

# Load code from script
script_file = input("Enter the file name of the script including the path i.e. /home/usernam/script_code.py")
script_code = read_script(script_file)

# qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
 
# Adding data to the instance 'qr'
# qr.add_data(data)
# qr.make(fit = True)
# qr.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
# img = qr.make_image(fill_color = 'red', back_color = 'white')
# img.save('MyQRCode2.png')
# # set size of QR code
pos = ((QRimg.size[0] - icon.size[0]) // 2,
       (QRimg.size[1] - icon.size[1]) // 2)
QRimg.paste(ion, pos)
 
# save the QR code generated
QRimg.save('gfg_QR.png')
 
print('QR code generated!')
