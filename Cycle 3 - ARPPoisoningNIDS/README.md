
## ARP Spoofing/Man-In-The-Middle Network-Based Intrusion Detection System (NIDS)

### Tool Overview
ARP Spoofing/MITM NIDS is a Python tool designed to be deployed in a secure network to detect IPv4 ARP-based MITM attacks at the network level. The tool integrates with an IPAM solution or DHCP server to build up a list of valid IP Address leases/reservations and uses the list as an authoritative source of IP Address to MAC Address mappings. The tool assumes that all IP Addresses are managed by reservation via an IPAM Tool or DHCP Server. The tool sniffs IPv4 ARP traffic and detects a malicious host that is staging a MITM attack via IPv4 ARP spoofing. 

### Why Should You Care
Among the tactics/techniques of staging a MITM is ARP Spoofing. IPv4 ARP is a protocol that lacks security to authenticate the source of IPv4 ARP messages. As such attackers can spoof an IP Address of a legitimate host and perform a MITM attack to capture, copy/read, and forward messages of a sensitive/critical target host. 

### My Interest The Tool
When researching how IPv4 ARP MITM attacks are orchestrated, I observed that all sample open-source IPv4 ARP proof of concept tools that were available on the internet HIDS-based. I decided to research and implement a NIDS-based tool that can provide great coverage to all hosts deployed in a given network. The tool provided me with the opportunity to understand the basics of MITM attacks at the protocol level.

### Three Main Ideas
IPv4 is still in use today with many enterprises deploying dual-stack IPv4/IPv6. IPv4 ARP lacks security against IP Address spoofing. Attackers can stage a MITM attack and gain access to sensitive information
Network-based defense against MITM is more robust than the host-based approach.
Integrating an authoritative source of IP Address leases mapped to MAC Address provides stronger security control than relying on a host-based agent detector on the victim machine to validate IP Address-To-MAC Address mapping.

### Technical Requirements
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
### Technical Requirements
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
21) Follow the instruction in the following video to execut an ARP Man-In-The-Middle (MITM) attack using ettercap and observe the results. 
    - Note: you will need to configure ip forwarding before executing MITM 
      - sudo sysctl net.ipv4.ip_forward
      - sudo sysctl net.ipv4.ip_forward=1 // no space between net.ipv4.ip_forward, equal sign, and 1 
      - sudo sysctl net.ipv4.ip_forward
    - https://www.youtube.com/watch?v=cVTUeEoJgEg 

### Video Demo & The  Tool
The video demo and the tool can be found at Github repo link below
https://github.com/kwafula/CSC-842/tree/main

### Future Direction
Add detections for DHCP attacks

### Additional Resources
1) ARP Spoofing - https://www.tutorialspoint.com/ethical_hacking/ethical_hacking_arp_poisoning.htm
2) Scapy - https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html
3) Kea DHCP - https://kea.readthedocs.io/en/kea-2.2.0/
4) ARP Spoofing Host-based Intrusion Detection System (HIDS)
(a). https://github.com/inavedanjum/arp-spoof-detector/tree/main
(b). https://github.com/AzizKpln/ARP-SPOOF-DETECTOR/tree/master
(c). https://github.com/m0riya42/Cyber-Security/tree/main/Arp-Spoofing-Detection
(d). https://github.com/mustafadalga/ARP-Spoof-Detector/tree/master
(e). https://github.com/Ash-Shaun/ARPShield/tree/master
(f). https://github.com/yoelbassin/ARP-Spoofing-Detection/tree/main
(g). https://github.com/Tomer-Rubinstein/ARP-Watch/tree/master
5) https://www.youtube.com/watch?v=cVTUeEoJgEg
