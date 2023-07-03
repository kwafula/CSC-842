## Cycle 7: QRCode Courier
### Tool Overview 
QRCode Courier is a tool that obfuscates and encodes content in a QR Code and decodes and deobfuscates the same content from the QR Code.

### Why Should You Care 
Adversaries are using QR Codes to deliver malicious URLs and potentially deliver and auto-execute binaries. Since adversaries already employ content obfuscation to evade security controls at victim organizations, if not already documented in publicly published intrusion and/or data breach incidents, it is just a matter of time before they use QR Codes to covertly exfilter data or better yet deliver malicious code via second-stage post-exploitation malware droppers. Defensive cyber operators need to be aware of this and factor in appropriate detective measures in their  Defensive Cyber Operations (DCO).

### My Interest In The Tool
QR Codes are increasingly becoming a popular vector for delivering malware to mobile devices to establish Command Control (C2) present on compromised devices. Adversaries deliver set a QR Code with a malicious URL and trick users who scan it to access and perform an action on a malicious website thinking it is legitimate i.e. a malicious QR Code that has been placed over a legitimate payment QR Code on a restaurant table or street parking meter. Having watched a news story about this about a month ago (See link # 1 Additional Resources below}), read through the work of MattKC where he delivers and auto-executes a binary via a QR Code (See link # 2 Additional Resources below), and seen classmates Tony Diaz and Michael McFadden demonstrate steganography tools with picture images and pdf files respectively, I asked myself if QR Codes can be used to covertly hide and exfiltrate data undetected. I wanted to know how else can adversaries employ QR Codes.

### Three Main Ideas
1) QRCode Courier easily encodes obfuscated content in QR Codes.
2) Content obfuscation is a tactic employed by adversaries to evade detection by deployed content-based security controls.
3) QRCode Courier easily decodes obfuscated content in QR Codes.

### Technical Requirements
1) Ubuntu 22.04 VM
3) Python3
4) python3-pip
5) qrcode
6) pillow
7) opencv-python

### Installation Steps 
1) Deploy Ubuntu 22.04
2) sudo apt install python3-pip
3) sudo pip3 install qrcode
4) sudo pip3 install pillow
5) sudo pip3 install opencv-python
6) Download QRCode Courier (qrcode_courier.py) from this GitHub repo
   sudo wget --no-proxy --no-cache https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle7_QRCode_Courier/qrcode_courier.py
8) Run the tool with the help option to learn the usage
   sudo python3 qrcode_courier.py -h
9) Run the tool as demonstrated in the video demo below

### Usage

<img width="1144" alt="image" src="https://github.com/kwafula/CSC-842/assets/95890992/67358333-24ae-4711-a459-747ffd66d9dc">

### Video Demo
The video demo and of my tool can be found at the youtube link below
   - https://youtu.be/9aGJuPO7_C0

### Future Direction 
1) Implement complex content obfuscation
2) Implement content encryption/decryption
3) Implement content compression
4) Implement dependency check and resolution

### Additional Resources
1) Malicious QR Code       https://abc-7.com/news/2023/05/01/fbi-warns-of-qr-scamming-trend-on-the-rise/
2) Snake QR Code:          https://hackaday.com/2020/08/17/fitting-snake-into-a-qr-code/
