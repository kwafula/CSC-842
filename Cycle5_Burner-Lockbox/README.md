
## Burner Lockbox

### Tool Overview 
Burner Lockbox is an offensive security post-exploitation tool that easily facilitates shipping in additional post-exploitation tools and shipping out captured data/information while keeping both secure throughout the cyber terrain of operation. The tool leverages Veracrypt to create an encrypted password-protected file container that hosts other tools and data, it can be mounted/dismounted and accessed as a volume, it can be copied across the internet and mounted on a different system, and it can be deleted (burned) or locked (lockbox) to prevent its contents from falling in the defender's hands. Hence its name, "Burner Lockbox", like burner cellphones and safe deposit lockboxes.

### Why Should You Care 
As an offensive practitioner who has built some post-exploitation tools that give you a competitive advantage, you don't want your secret tools to fall into the wrong hands or spill over the internet. However, you must have the ability to ship those tools in and out of your target environments. Also, when your captured data/information is traversing the public cyber terrain i.e. file share servers, you want to maintain the confidentiality, integrity, and availability of the data/information.

### My Interest The Tool
My interest in this tool was sparked by the 2016/2017 case where the NSA lost control of a stash of tools that were later spilled over the internet by the group known as Shadow Broker. Among the tools was EternalBlue, a lethal tool that up to that point was only in the hands of the NSA. Maintaining exclusive control of one's tools, especially those that give you a competitive advantage, is key to one's sustained success. Up to the point when EnternalBlue was leaked out, only NSA had the advantage of using it on a Microsoft Windows SMBv1 vulnerability that it had known for years but had not shared with Microsoft nor disclosed to the public, effectively making the combination of EnternalBlue and the SMBv1 vulnerability a backdoor on millions of Microsoft Windows computers across the globe. Proprietary tools are an intellectual property and competitive advantage, their chain of custody should remain in the authorized hands. Burner Lockbox is a proof-of-concept implementation toward such a chain of custody.

### Three Main Ideas
1) IPv4 is still in use today with many enterprises deploying dual-stack IPv4/IPv6. IPv4 ARP lacks security against IP Address spoofing. Attackers can stage a MITM attack and gain access to sensitive information
2) Network-based defense against MITM is more robust than the host-based approach.
3) Integrating an authoritative source of IP Address leases mapped to MAC Address provides stronger security control than relying on a host-based agent detector on the victim machine to validate IP Address-To-MAC Address mapping.

### Technical Requirements (Change Me)
See details on Github repo link below
1) Ubuntu 22.04 VM - For DHCP Server/ ARP NIDS
2) Ubuntu 22.04 VM - For Vitcim Server
3) Pfsense 2.6 VM - Router/Firewall
4) Kali Linx VM - Compromise/Attack VM
5) Virtualbox 7.0 ( VMware Fusin 12/13 will not work on Mac) VC
6) Python3 on Ubuntu (Installed by defualt)
7) Kea DHCP4 Server
8) Kea DHCP Control Agent
9) Scapy
10) Git
11) Ettercap ( on Kali Linux)
12) Linux net-tools
### Lab Setup Steps (Change Me)
1) Deploy Ubuntu 22.04 VM (ARP NIDS)
2) Deploy Ubuntu 22.04 VM (Vitcim Host)
3) Deploy Pfsense (Firewall/Router)
4) Deploy Kali Linux (Attack Host)
7)  Configure Virtual box to represent the following topology show below

    <img width="853" alt="image" src="https://github.com/kwafula/CSC-842/assets/95890992/e34d1061-8aa7-487e-a1b2-17e5bb073505">

 
3) Install Linux net-tools on the ARP NIDS Server
   - sudo apt-get update
   - sudo apt-get install net-tools -y
5) Install Kea DHCP4 Server on the ARP NIDS Server
   - sudo apt-get update
   - sudo apt-get install kea-dhcp4-server -y
6) Install Kea DHCP Control Agent on the ARP NIDS Server
   - sudo apt-get install kea-ctrl-agent -y
7) Install Scapy on the ARP NIDS Server
   - sudo apt-get install scapy -y
8) Install Git on the ARP NIDS Server
   - sudo apt-get install git -y
9) Download CSC-842 Repo on the ARP NIDS Server
   - sudo git clone https://github/com/kwafula/CSC-842.git
10) Change directory to into the CSC-842/Cylce 3/ARPPoisoningNIDS
   - cd "CSC-842/Cylce 3/ARPPoisoningNIDS/"
11) Backup the Kea DHCP config file kea-dhcp4.conf in /etc/kea/ and copy the one in the downloaded git repo to that location
   - sudo mv /etc/kea/kea-dhcp4.conf /etc/kea/kea-dhcp4.conf.bak
   - sudo cp kea-dhcp4.conf /etc/kea/kea-dhcp4.conf
   - sudo mv /etc/kea/keactrl.conf /etc/kea/keactrl.conf.bak
   - sudo cp keactrl.conf /etc/kea/keactrl.conf
   - sudo mv /etc/kea/kea-ctrl-agent.conf /etc/kea/kea-ctrl-agent.conf.bak
   - sudo cp kea-ctrl-agent.conf /etc/kea/kea-ctrl-agent.conf
13) Update the /etc/kea/kea-dhcp4.conf file with DHCP listening network interface -  
    "interfaces-config": {
        "interfaces": ["enp0s3"]
     }
14) Start Kea DHCP Server ( Before performing this step, disable the DHCP Server on the Pfsense Firewall Router is you have running)
   - sudo keactrl status
   - sudo keactrl stop && keactrl status
   - sudo keactrl stop && keactrl start
15) Check the /var/lib/kea/kea-lease4.csv file to make sure the DHCP leasing is working, your should see list of leases bas
   - cat /var/lib/kea/kea-leases4.csv
17) Configure IP Addresses and MAC Address as follows and reboot the system starting with the DHCP Server/ARP NIDS 
   - Pfsense (Firewall/Router)
      -  DHCP IP Address Reservation: 192.168.2.1 *** change this using the Pfsense GUI under -> Interfaces -> LAN -> Change from Static to DHCP -> and then reboot
      -  MAC Address 00:50:56:01:7A:E2
   - Ubuntu 22.04 VM (Vitcim Host)
      -  DHCP IP Address Reservation : 192.168.2.2
      -  MAC Address 00:50:56:01:7A:CD
    - Kali Linux (Attack Host)
      -  Static IP Address: 192.168.2.4
      -  MAC Address 00:50:56:01:7A:CE
    - Ubuntu 22.04 VM (ARP NIDS)
      -  DHCP IP Address Reservation : 192.168.2.4
      -  MAC Address 00:50:56:01:58:78
    - If your configurations are different, update DHCP reservations in the /etc/kea/kea-dhcp4.conf
18) Update the ARP NIDS python script (arp_poisoning_nids.py) with the correct monitoring interface 
    def get_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--interface", dest = "interface", default = "enp0s3", help = "Monitored Interface") //this line
        args = parser.parse_args()
    return args
20) Run the ARP NIDS python script
    - sudo python3 arp_poisoning_nids.py
21) For guidence on how to execute an ARP Man-In-The-Middle (MITM) attack using Ettercap. Clink on video link# 5 under "Additional Resources". 
    - Note: you will need to configure ip forwarding before executing MITM 
      - sudo sysctl net.ipv4.ip_forward
      - sudo sysctl net.ipv4.ip_forward=1 // no space between net.ipv4.ip_forward, equal sign, and 1 
      - sudo sysctl net.ipv4.ip_forward
### ARP Spoofing MITM Demo Video (Change Me)
The video demo and of my tool can be found at youtube link below
https://youtu.be/Yr-PxUJEAAM

### Future Direction (Change Me)
Add detections for DHCP attacks

### Additional Resources
1) EternalBlue: https://www.wired.com/story/nsa-leak-reveals-agency-list-enemy-hackers/
2) SMBv1 Vulnerability: https://scholarship.law.umn.edu/cgi/viewcontent.cgi?article=1450&context=mjlst
3) Scapy - https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html
4) Kea DHCP - https://kea.readthedocs.io/en/kea-2.2.0/
5) ARP Spoofing Host-based Intrusion Detection System (HIDS)



