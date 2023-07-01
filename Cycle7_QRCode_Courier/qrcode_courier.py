#!/usr/bin/env python3 

import qrcode
from PIL import Image
import cv2
import numpy as np
import time
import argparse

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
# 08 # Read obsfuscated text from QR Code
# 09 # Deobfuscate read text
# 09 # Argpase
# 10 # Size the text content

# Function to read file
def read_file(file_name):
    with open(file_name, mode="r", encoding="utf8") as file_obj:
        file_data = file_obj.read()
        print(file_data)
        return file_data
        
def resize_image(in_file, out_file, size):
    with open(in_file) as fd:
        image = resizeimage.resize_thumbnail(Image.open(fd), size)
    image.save(out_file)
    image.close()

def image_read(image_file):
    with Image.open(image_file) as image_obj:
        return image_obj 

parser = argparse.ArgumentParser()
subparser = parser.add_subparsers(dest = 'command')
encode = subparser.add_parser('encode')
decode = subparser.add_parser('decode')
create_lockbox = subparser.add_parser('create_lockbox', formatter_class=argparse.RawTextHelpFormatter, help='Function Description: Create a lockbox container,\n'
                                 'Arguments: --name <lockbox name>  --size <size> --type <normal | hidden>,\n' ## verify hidden argument value
                                 'Usage: python3 burner_lockbox.py create_lockbox --name lockboxA.vc --size 25M --type normal \n\n')

encode.add_argument('-s', '--source-file', action = 'store', dest = 'input_file', required = True, help = 'Input data file, including the path,\n'
                    'Example: /home/username/input-datafile.txt\n\n')
encode.add_argument('-i', '--image-file', action = 'store', dest = 'image_file', required = True, help = 'Image file, including the path,\n'
                    'Example: /home/username/input_image.png\n\n')
encode.add_argument('-d', '--dest-file', action = 'store', dest = 'output_file', required = True, help = 'Output image file, including the path,\n'
                    'Example: /home/username/myapp.ico\n\n')

decode.add_argument('-i', '--image-file', action = 'store', dest = 'image_file', required = True, help = 'Input image file including the path,\n'
                    'Example: /home/username/myapp.ico\n\n')
decode.add_argument('-d', '--destination-file', action = 'store', dest = 'output_file', required = True, help = 'Output data file, including the path,\n'
                    'Example: /home/username/output-datafile.txt\n\n')
# parser.add_argument('-v, '--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

if args.command == 'encode':
    # Load icon image
    # icon_file = input("Data file include the path i.e. /home/username/icon.jpg: ")
    # print("")
    icon_image = image_read(str(image_file))

    # Resize icon image
    # resize_image('foo.tif', 'foo_small.jpg', (256, 256))

    # Load content from a file
    # source_file = input("Enter the file name of the file you would like to encode, include the path i.e. /home/username/script_code.py: ")
    # print("")
    source_data = read_file(str(input_file))

    # Package Data
    qr_percel = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr_percel.add_data(source_data)
    qr_percel.make(fit = True)
    icon = qr_percel.make_image(back_color=(255, 195, 235), fill_color=(55, 95, 35))
    # print the image size (version)
    print('Size of the QR image(Version):')
    print(np.array(qr_percel.get_matrix()).shape)
    icon.save(output_file)
    print('QR code generated!')
    
elif args.command == 'decode':
    # img.save('MyQRCode2.png')
    # # set size of QR code
    #pos = ((QRimg.size[0] - icon.size[0]) // 2,
    #       (QRimg.size[1] - icon.size[1]) // 2)
    #QRimg.paste(ion, pos)
    # # save the QR code generated
    #QRimg.save('gfg_QR.png')

    # Temporary code will be removed when argparse is implemented, 
    # time.sleep(5)

    # Read QRCode. Replace with and input query
    qr_image = cv2.imread(image_file)

    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()

    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(qr_image)

    # if there is a QR code
    # print the data
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
        data.save(output_file)
    else:
        print("There was some error")
  
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
