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


https://snyk.io/advisor/python/script-sandbox
https://pypi.org/project/sandboxapi/
https://bahamas10.github.io/binary-to-qrcode/
https://www.kitploit.com/2023/03/qrexfiltrate-tool-that-allows-you-to.html
https://pypi.org/project/sandboxapi/

FACTS
QR Codes file forms come in JPEG,PNG, SVG, EPS, and PDF,  and so are the file magic signatures
  https://www.qr-code-generator.com/guides/download-qr-codes-into-different-file-formats/#:~:text=QR%20Codes%20can%20then%20be,with%20QR%20Code%20Generator%20software.
QR Codes have 

Question
Does the file type influence the storage capacity?
  https://www.qrcode.com/en/about/version.html
  https://www.qrcode.com/en/about/version.html#versionPageMixed
  https://www.qrcode.com/en/about/error_correction.html
Are there file format markers that can identify a QR Code without the visual checkered-like pattern?
Forensically, how can we differentiate a QR Code file from a Non-QR Code file
  https://note.nkmk.me/en/python-opencv-qrcode/
Can you overlay a transparent image on a QR Code and have it still work?
How does the logo size pasted on a QR Code influence its readability?
When a QR Code has a logo of a size that OpenCV cannot detect, why do smartphone cameras still detect it?
How can in specify the version number of the QR code I ma creating i.e. 40?
What are the components that make up a QR Code?
  https://www.turing.com/kb/creating-qr-code-using-js
What is teh QR Code standard>
  https://www.qrcode.com/en/about/standards.html
What types of QR Code exits
  https://www.qrcode.com/en/index.html
  https://www.qrcode.com/en/codes/
  SQRC: https://www.denso-wave.com/en/system/qr/product/sqrc.html
  FrameQR: https://www.denso-wave.com/en/system/qr/product/frame.html
  https://www.qrcode.com/en/index.html
QR Code Data Types
https://www.freecodecamp.org/news/how-to-create-stunning-qr-codes-with-python/
https://medium.com/pythoniq/make-beautiful-qr-codes-in-python-ef083fb38550
https://segno.readthedocs.io/en/latest/
Geo:
WIFI:
TEXT:
URL: 
vCard:
MeCard:
EPC QR:
Email

Other Related Topics
https://www.youtube.com/watch?v=nAl0MIQBWmY
https://trailofbits.github.io/ctf/forensics/
https://pypi.org/project/qrtools/

https://github.com/Dvd848/CTFs/blob/master/2019_MITRE_CTF/QvR_Code.md
https://www.sciencedirect.com/science/article/abs/pii/S0167739X17324160
https://github.com/primetang/qrtools
