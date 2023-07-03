## Cycle 7: QRCode Courier
### Tool Overview 
QRCode Courer is tool for 

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
4) curl-7.88.1
5) libwxgtk3.0-gtk3-0v5
6) exfat-fuse
7) exfatprogs
8) veracrypt

### Lab Setup Steps 
1) Deploy Ubuntu 22.04 VMs and Pfsense2.6 VM as a Firewall/Router and Snort IDS as shown in the following topology
   
   ![burner_lockbox](https://github.com/kwafula/CSC-842/assets/95890992/19d101b8-b82d-461f-86f7-28696dc7a08b)

3) Follow the instruction in the link below in "Additional Resources" to install curl-7.88.1, curl-7.81.0 and below throws an SSL error
   
   - sudo apt remove curl
   - sudo apt purge curl
   - sudo apt-get update
   - sudo apt-get install -y libssl-dev autoconf libtool make
   - cd /usr/local/src
   - sudo wget https://curl.haxx.se/download/curl-7.88.1.zip
   - sudo unzip curl-7.88.1.zip
   - cd curl-7.88.1
   - sudo ./buildconf
   - sudo ./configure --with-ssl 
   - sudo make
   - sudo make install
   - sudo cp /usr/local/bin/curl /usr/bin/curl
   - sudo ldconfig
   - curl -V
   
5) Download BurnerLockbox (burner_lockbox.py) from this GitHub repo.
   
   - sudo curl -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle5_Burner-Lockbox/burner_lockbox.py --output burner_lockbox.py
   
7) Run the tool with the resolve_dependincies option, the tool has the capability to install libwxgtk3.0-gtk3-0v5, exfat-fuse, exfatprogs, and veracrypt, if not already installed.
8) Run the tool as demonstrated in the video demo below

### Usage

<img width="1451" alt="image" src="https://github.com/kwafula/CSC-842/assets/95890992/b52ead7c-893c-4395-9158-89c86847ddcb">

### Video Demo
The video demo and of my tool can be found at the youtube link below
   - https://youtu.be/9aGJuPO7_C0

### Future Direction 
1) Fix issue with interactive shell hanging in the background of subprocess when you enter the wrong passsword during lockbox mount operation
2) Lockbox timer or auto-lock on exit or independent auto-lock memory resident code
3) Detect memory dump routine and trigger Lockbox auto-lock to protect against memory-based attacks 
4) Detect VM snapshot routine and trigger Lockbox auto-lock to  protect against memory-based attacks 
5) Generate PE install package for Windows install package windows
6) Generate DMG install package for Mac
7) Generate RPM install package for CentOS/Redhat
8) Generate Deb install package for Ubuntu/Debian

### Additional Resources
1) Malicious QR Code       https://abc-7.com/news/2023/05/01/fbi-warns-of-qr-scamming-trend-on-the-rise/
2) Snake QR Code:          https://hackaday.com/2020/08/17/fitting-snake-into-a-qr-code/
3) Install Curl-7.88.1:    https://stackoverflow.com/questions/72627218/openssl-error-messages-error0a000126ssl-routinesunexpected-eof-while-readin
4) Veracrypt:              https://documentation.help/VeraCrypt/Command%20Line%20Usage.html 
5) Veracrypt:              https://kifarunix.com/how-to-use-veracrypt-on-command-line-to-encrypt-drives-on-ubuntu/


