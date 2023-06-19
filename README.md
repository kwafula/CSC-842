# DSU Course CSC-842: Security Tool Development

## General infomation
- **Project Author:**  Kevin Wafula
- **Course Title:** Security Tool Development
- **Course Number:** CSC-842-DT1
- **Course Professor:** Dr. Cody Welu
- **Degree Program:** PhD in Cyber Operations
- **Degree Institution:** Dakota State University  
- **Project Description:** In fulfillment of the course CSC-842: Security Tool Development
- **Semester:** Summer 2023

## Repo Overview
The repo is structured by sprint cycle folders, to review a tool for a given sprint cycle, browse the cycle folder above i.e. Cycle 1 - WebAttackVectorEnumerator. Below is an overview of each tool in this repo.

### Cycle 1 Tool Overview:  WebApp Attack Vector Enumerator
WebApp Attack Vector Enumerator is an interactive python tool that facilitates the mapping surface area of attack of a web application. The tool achieves this by scanning a web application to enumerate services that are running and openly accessible, querying the National Vulnerability Database (NVD) to identify Common Vulnerabilities and Exposures (CVE) associated with enumerated services, and finally querying ExploitDB to map the CVEs to exploits. The tool provides two workflows, manual step-by-step interactive and one-step automated execution.

### Cycle 3 Tool Overview: ARP Spoofing/Man-In-The-Middle Network-Based Intrusion Detection System (NIDS) 
ARP Spoofing/MITM NIDS is a Python tool designed to be deployed in a secure network to detect IPv4 ARP-based MITM attacks at the network level. The tool integrates with an IPAM solution or DHCP server to build up a list of valid IP Address leases/reservations and uses the list as an authoritative source of IP Address to MAC Address mappings. The tool assumes that all IP Addresses are managed by reservation via an IPAM Tool or DHCP Server. The tool sniffs IPv4 ARP traffic and detects a malicious host that is staging a MITM attack via IPv4 ARP spoofing.

### Cycle 5 Tool Overview: BurnerLockbox
Burner Lockbox is an offensive security post-exploitation tool that easily facilitates shipping in additional post-exploitation tools and shipping out captured data/information while keeping both secure throughout the cyber terrain of operation. The tool leverages Veracrypt to create an encrypted password-protected file container that hosts other tools and data, it can be mounted/dismounted and accessed as a volume, it can be copied across the internet and mounted on a different system, and it can be deleted (burned) or locked (lockbox) to prevent its contents from falling in the defender's hands. Hence its name, "BurnerLockbox", like burner cellphones and safe deposit lockboxes.

### Cycle 7 Tool Overview: TBD


### Cycle 9 Tool Overview: TBD
