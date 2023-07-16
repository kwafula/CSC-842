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
