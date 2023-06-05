# VIDEO & FINAL CODE PENDING RESOLUTION TECHNICAL ISSUE - ETA 8:00 AM, Wednesday June 7, 2023. 

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
IPAM/ DHCP/Asset Management Database - (Authoritative Source IP Address-To-MAC Address Mapping)
Scapy
Ubuntu 22.0 OS Host
Python3

### Installation
See details on Github repo link below
https://github.com/kwafula/CSC-842/tree/main

### Video Demo & The  Tool
The video demo and the tool can be found at Github repo link below
https://github.com/kwafula/CSC-842/tree/main

### Future Direction
Add detections for DHCP attacks

### Additional Resources
1) ARP Spoofing - https://www.tutorialspoint.com/ethical_hacking/ethical_hacking_arp_poisoning.htm
2) Scapy - https://scapy.readthedocs.io/en/latest/api/scapy.layers.l2.html
3) Kea DHCP - https://kea.readthedocs.io/en/kea-2.2.0/
3) ARP Spoofing Host-based Intrusion Detection System (HIDS)
(a). https://github.com/inavedanjum/arp-spoof-detector/tree/main
(b). https://github.com/AzizKpln/ARP-SPOOF-DETECTOR/tree/master
(c). https://github.com/m0riya42/Cyber-Security/tree/main/Arp-Spoofing-Detection
(d). https://github.com/mustafadalga/ARP-Spoof-Detector/tree/master
(e). https://github.com/Ash-Shaun/ARPShield/tree/master
(f). https://github.com/yoelbassin/ARP-Spoofing-Detection/tree/main
(g). https://github.com/Tomer-Rubinstein/ARP-Watch/tree/master
