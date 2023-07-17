## Cycle 9: QRCode Inspector
### Tool Overview
QRCode Inspector is a tool that decodes URLs from QR Codes and runs URL checks against CTI databases.

### Why Should You Care
Adversaries are using QR Codes to deliver malicious URLs. Malware Analysts need a tool to analyze if URLs encoded in QR Codes are malicious.

### My Interest In The Tool
To build a proof of concept tool to decode URLs from QR Codes and run them against CTI databases.

### Three Main Ideas
1) QRCode Codes easily encode URLs.
2) Encoded URLs can be malicious a vector for delivering malware to endpoints.
3) Encoded URLs can be decoded and run against CTI databases to check if they are malicious

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
7) Download QRCode Courier and associated files (qrcode_inspector.py, image1.jpg) and from this GitHub repo
   
    sudo wget --no-proxy --no-cache https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle9_QRCode_Inspector/qrcode_inspector.py
   
    sudo wget --no-proxy --no-cache https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle9_QRCode_Inspector/image1.jpg
   
10) Run the tool with the help option to learn the usage
    
    python3 qrcode_inspector.py -h
12) Run the tool as demonstrated in the video demo below
   
### Usage
![image](https://github.com/kwafula/CSC-842/assets/95890992/829f68cb-30d5-49b2-8108-47235a91e652)

### Video Demo
The video demo and of my tool can be found at the youtube link below under "Cycle9_QRCode_Inspector" folder
   https://youtu.be/Dkazis82PJw

### Future Direction
1) Implement analysis for image that is directly downloaded a url
2) Implement analysis for images that is directly scraped from a website
   
### Additional Resources
1) Malicious QR Code: https://abc-7.com/news/2023/05/01/fbi-warns-of-qr-scamming-trend-on-the-rise/



