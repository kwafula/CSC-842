#!/usr/bin/env python3
#coding:utf-8

# forked from http://www.cnblogs.com/babycool/p/4734819.html

'''
Python QRCode generator
- transform the input string to general QRCode image
- generate QRCode image with logo image
Depend on qrcode, please see https://pypi.python.org/pypi/qrcode
'''

__author__ = 'Xue'

import qrcode
from PIL import Image
import os

# generate general QRCode image
def make_qr(str,save):
    qr=qrcode.QRCode(
        version=4,  #size of QRCode image 1-40  1:21*21（21+(n-1)*4）
        error_correction=qrcode.constants.ERROR_CORRECT_M, #L:7% M:15% Q:25% H:30%
        box_size=10, # pixel size of every box
        border=2, # border width size
    )
    qr.add_data(str)
    qr.make(fit=True)

    img=qr.make_image()
    img.save(save)


# generate QRCode with logo image
def make_logo_qr(str,logo,save):
    qr=qrcode.QRCode(
        version=4,
        error_correction=qrcode.constants.ERROR_CORRECT_Q,
        box_size=8,
        border=2
    )

    # add string to transform
    qr.add_data(str)

    qr.make(fit=True)
    # generate QRCode
    img=qr.make_image()

    img=img.convert("RGBA")

    # add logo
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
        icon=icon.resize((icon_w,icon_h),Image.ANTIALIAS)
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


if __name__=='__main__':
    save_path='theqrcode.png' # saved to this file
    logo='logo.jpg'  # load logo image from local directory

    str=input('Please input your string：')
    # for python2, you can use `raw_input` to replace `input`

    #make_qr(str)

    make_logo_qr(str,logo,save_path)
