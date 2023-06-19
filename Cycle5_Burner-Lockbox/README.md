
## BurnerLockbox

### Tool Overview 
Burner Lockbox is an offensive security post-exploitation tool that easily facilitates shipping in additional post-exploitation tools and shipping out captured data/information while keeping both secure throughout the cyber terrain of operation. The tool leverages Veracrypt to create an encrypted password-protected file container that hosts other tools and data, it can be mounted/dismounted and accessed as a volume, it can be copied across the internet and mounted on a different system, and it can be deleted (burned) or locked (lockbox) to prevent its contents from falling in the defender's hands. Hence its name, "BurnerLockbox", like burner cellphones and safe deposit lockboxes.

### Why Should You Care 
As an offensive practitioner who has built some post-exploitation tools that give you a competitive advantage, you don't want your secret tools to fall into the wrong hands or spill over the internet. However, you must have the ability to ship those tools in and out of your target environments. Also, when your captured data/information is traversing the public cyber terrain i.e. file share servers, you want to maintain the confidentiality, integrity, and availability of the data/information.

### My Interest The Tool
My interest in this tool was sparked by the 2016/2017 case where the NSA lost control of a stash of tools that were later spilled over the internet by the group known as Shadow Broker. Among the tools was EternalBlue, a lethal tool that up to that point was only in the hands of the NSA. Maintaining exclusive control of one's tools, especially those that give you a competitive advantage, is key to one's sustained success. Up to the point when EnternalBlue was leaked out, only NSA had the advantage of using it on a Microsoft Windows SMBv1 vulnerability that it had known for years but had not shared with Microsoft nor disclosed to the public, effectively making the combination of EnternalBlue and the SMBv1 vulnerability a backdoor on millions of Microsoft Windows computers across the globe. Proprietary tools are an intellectual property and competitive advantage, their chain of custody should remain in the authorized hands. BurnerLockbox is a proof-of-concept implementation toward such a chain of custody.

### Three Main Ideas
1) BunerLockbox easily downloads/uploads post-exploitation tools or captured data/information in an encrypted file container thus protecting the tools from detection/mitigation by IDS/IPS systems.
2) BurnerLockbox easily deletes (Burns) post-exploitation tools or captured data/information at the target infrastructure in the event that an offensive security mission needs to be aborted.
3) BurnerLockbox easily secures (Lockbox) post-exploitation tools or captured data/information throughout the cyber terrain of operation, be it command control infrastructure, public internet, or the target infrastructure.

### Technical Requirements
1) Ubuntu 22.04 VM
2) Pfsense 2.6 VM - Router/Firewall/IDS
3) Python3 
4) curl-7.88.1
5) libwxgtk3.0-gtk3-0v5
6) exfat-fuse
7) exfatprogs
8) veracrypt

### Lab Setup Steps 
1) Deploy Ubuntu 22.04 VMs and Pfsense2.6 VM as a Firewall/Router and Snort IDS as shown in the following topology
   
   ![burner_lockbox](https://github.com/kwafula/CSC-842/assets/95890992/19d101b8-b82d-461f-86f7-28696dc7a08b)

3) Follow the instruction in the link below in "Additional Resources" to install curl-7.88.1, curl-7.88.0, and below throws an error
4) Download BurnerLockbox (burner_lockbox.py) from this GitHub repo.
   
   sudo curl -H 'Cache-Control: no-cache, no-store' https://raw.githubusercontent.com/kwafula/CSC-842/main/Cycle5_Burner-Lockbox/burner_lockbox.py --output burner_lockbox.py
6) Run the tool with the resolve_dependincies option, the tool has the capability to install libwxgtk3.0-gtk3-0v5, exfat-fuse, exfatprogs, and veracrypt, if not already installed.
7) Run the tool as demonstrated in the video demo below

### Video Demo
The video demo and of my tool can be found at the youtube link below


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
1) EternalBlue:            https://www.wired.com/story/nsa-leak-reveals-agency-list-enemy-hackers/
2) SMBv1 Vulnerability:    https://scholarship.law.umn.edu/cgi/viewcontent.cgi?article=1450&context=mjlst
3) Install Curl-7.88.1:    https://stackoverflow.com/questions/72627218/openssl-error-messages-error0a000126ssl-routinesunexpected-eof-while-readin
4) Veracrypt:              https://documentation.help/VeraCrypt/Command%20Line%20Usage.html 
5) Veracrypt:              https://kifarunix.com/how-to-use-veracrypt-on-command-line-to-encrypt-drives-on-ubuntu/


