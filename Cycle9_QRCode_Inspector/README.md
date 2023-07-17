## Cycle 7: QRCode Inspector
### Tool Overview
QRCode Courier is a tool that obfuscates and encodes content in a QR Code and decodes and deobfuscates the same content from the QR Code.

### Why Should You Care
Adversaries are using QR Codes to deliver malicious URLs. Malware Analysts need a tool analyze analyze if URLs encoded in QR Codes are malicious.

### My Interest In The Tool
To build a proof of concept tool to decode URLs from QR Codes and run them againts CTI databases.

### Three Main Ideas
1) QRCode Codes easily encodes URLs.
2) Encoded URLs can be malicious and vector for delivering malware to endpoints.
3) Encoded URLs decoded and run against CTI databases.

### Technical Requirements
1) Ubuntu 22.04 VM
2) Python3
3) python3-pip python library
4) qrcode python library
5) pillow python library
6) opencv-python python library
7) requests python library
8) urllib.parse python library
9) json python library
   
# Installation Steps
1) Deploy Ubuntu 22.04
2) sudo apt install python3-pip
3) sudo pip3 install qrcode
4) sudo pip3 install pillow
5) sudo pip3 install opencv-python
6) sudo pip3 install request
7) Download QRCode Courier and associated files (qrcode_courier.py, backdoorstager, minepanda.jpeg) and from this GitHub repo
   a) sudo wget --no-proxy --no-cache https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle9_QRCode_Inspector/qrcode_inspector.py
   b) sudo wget --no-proxy --no-cache https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle9_QRCode_Inspector/image1.jpg
8) Run the tool with the help option to learn the usage sudo python3 qrcode_inspector.py -h
9) Run the tool as demonstrated in the video demo below
   
### Usage
<img width="931" alt="image" src="https://github.com/kwafula/CSC-842/assets/95890992/fcd98b3e-75b6-4377-975c-03f78a47d686">

### Video Demo
The video demo and of my tool can be found at the youtube link below under "Cycle9_QRCode_Inspector" folder
   https://youtu.be/Dkazis82PJw

### Future Direction
1) Implement analysis for image that is directly downloaded a url
2) Implement analysis for images that is directly scraped from a website
   
### Additional Resources
1) Malicious QR Code: https://abc-7.com/news/2023/05/01/fbi-warns-of-qr-scamming-trend-on-the-rise/



