#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import numpy as np
import time
import argparse
import os

#####Install Dependecies##
# sudo pip3 install qrcode
# And
# sudo pip3 install pillow
# OR
# sudo pip3 install "qrcode[pil]"
# sudo pip3 install opencv-python
# sudo pip3 install python-resize-image
# sudo apt install python3-pip


#####Product Backlog#####
# 00 # Install dependecies
# 01 # Create QR Code ***
# 02 # Specify QR Code back color, fill color, box_size, and border ****
# 03 # Add logo to QR Code 
# 04 # Read text from file ***
# 05 # Obfuscate read text
# 06 # Add text to QR Code ***
# 07 # Name QR with a .ico extension ***
# 08 # Deobfuscate read text
# 09 # Argpase ***
# 10 # Size the text content
# 11 # Remane to QR Code from .png to .ico after QR Code is generated

# Function to read data file
def read_file(file_name):
    with open(file_name, mode="r", encoding="utf8") as file_obj:
        file_data = file_obj.read()
        return file_data
        
# Function to resize image   
def resize_image(in_file, out_file, size):
    with open(in_file) as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)
    image.save(out_file)
    image.close()
    
# Function to load image file
def image_read(image_file):
    with Image.open(image_file) as image_obj:
        #return image_obj.crop((175, 90, 235, 150)) 
        return image_obj

# Function to write data file
def write_file(file_name, file_data):
    with open(file_name, mode="w", encoding="utf8") as file_obj:
        file_obj.write(file_data)
        return 

parser = argparse.ArgumentParser(formatter_class = argparse.RawTextHelpFormatter, description = 'QRCode Courier Usage Details:',\
                                 usage = 'sudo python3 qrcode_courier.py --encode -s <input_file> -i <image_file> -d <output_file>,\n'
                                 '       sudo python3 qrcode_courier.py --decode -i <image_file> -d <output_file>,\n')
subparser = parser.add_subparsers(dest = 'command')

encode = subparser.add_parser('encode', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Encode source data in a QRCode and generate an icon,\n'
                    'Usage Example: sudo python3 qrcode_courier.py --encode -s ./input-datafile.txt -i ./gihhub.png -d ./myapp.png \n\n')

decode = subparser.add_parser('decode', formatter_class = argparse.RawTextHelpFormatter, help = 'Description: Read the icon to decode and extract embedded data,\n'
                    'Usage Example: sudo python3 qrcode_courier.py --decode -i ./myapp.png -d ./output_datafile.txt \n\n')

encode.add_argument('-s', action = 'store', type=str, dest = 'input_file', required = True)
encode.add_argument('-i', action = 'store', type=str, dest = 'image_file', required = True)
encode.add_argument('-d', action = 'store', type=str, dest = 'output_file', required = True)

decode.add_argument('-i', action = 'store', type=str, dest = 'image_file', required = True)
decode.add_argument('-d', action = 'store', type=str, dest = 'output_file', required = True)

parser.add_argument('-v', '--version', action='version', version='%(prog)s v1.0')

args = parser.parse_args()

if args.command == 'encode':
    # Load data from a file
    input_file = args.input_file
    source_data = read_file(str(input_file))

    # Initialize data and QR Code
    qr_percel = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    print(source_data)
    print("")
    qr_percel.add_data(source_data)
    qr_percel.make(fit = True)
    
    # Print the QR Code image size (version)
    print('Size of the QR image(Version):')
    print(np.array(qr_percel.get_matrix()).shape)
    print("")

    # Encode data into QR Code
    icon = qr_percel.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))

    # Convert QR Code to RGBA
    icon = icon.convert('RGBA')

    """
    if logo and os.path.exists(logo):
        icon=Image.open(logo)
        # get size of QRCode image
        img_w,img_h=img.size

        factor=4
        size_w=int(img_w/factor)
        size_h=int(img_h/factor)

        # size of logo <= 1/4 * QRCode image
        icon_w,icon_h=icon.size
        if icon_w>size_w:
            icon_w=size_w
        if icon_h>size_h:
            icon_h=size_h
        icon=icon.resize((icon_w,icon_h),Image.LANCZOS)
        # see http://pillow.readthedocs.org/handbook/tutorial.html

        # compute the position of logo in output image
        w=int((img_w-icon_w)/2)
        h=int((img_h-icon_h)/2)
        icon=icon.convert("RGBA")
        # paste logo on the output image
        img.paste(icon,(w,h),icon)
        # see：http://pillow.readthedocs.org/reference/Image.html#PIL.Image.Image.paste

    # save QRCode image
    img.save(save)
    """
    # Get size of QR Code
    icon_w, icon_h = icon.size

    # Initialize logo image resize factor
    factor = 4
    size_w=int(icon_w/factor)
    size_h=int(icon_h/factor)
    
    # Load logo image 
    image_file = args.image_file
    icon_logo = image_read(image_file)

    # Get logo image size 
    icon_logo_w, icon__logo_h = icon_logo.size

    # Resize logo image
    if icon_logo_w > size_w:
        icon_logo_w = size_w
    if icon_logo_h > size_h:
        icon_logo_h = size_h
    icon_logo = icon_logo.resize((icon_logo_w,icon__logo_h), Image.LANCZOS)

    # Initialize logo image position on QR Code
    w = int((icon_w - icon_logo_w)/2)
    h = int((icon_h - icon_logo_h)/2)

    # Convert logo image to RGBA
    icon_logo = icon_logo.convert('RGBA')
    
    # Paste logo image on QR Code
    icon.paste(icon_logo,(w,h),icon_logo)
    
    #print(icon_logo)
    #print("")
    
    # Initialize position  on QR Code to pate logo
    #logo_x_position = (icon.size[0] - icon_logo.size[0]) // 2
    #logo_y_position = (icon.size[1] - icon_logo.size[1]) // 2
    #logo_position = (logo_x_position, logo_y_position)
    #logo_position = ((icon.size[0] - icon_logo.size[0]) // 2, (icon.size[1] - icon_logo.size[1]) // 2)
    
    # Paste logo image onto QR Code image
    #icon.paste(icon_logo, logo_position)
    
    # save QR code image/icon
    output_file = args.output_file
    icon.save(output_file)
    print('QR code generated!')
    print("")
    
elif args.command == 'decode':
    # Read QRCode. Replace with and input query
    image_file = args.image_file
    qr_image = cv2.imread(image_file)

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(qr_image)

    # if there is a QR code
    # print the data
    output_file = args.output_file
    if vertices_array is not None:
        print('QRCode data:')
        print(data)
        print('Writing file the following file to the following disk location: ', output_file)
        write_file(output_file, data)
    else:
        print('There was some error')
  
    #results = parser.parse_args()

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
# https://www.makeuseof.com/how-to-create-and-decode-a-qr-code-using-python/
