# DSU Course CSC-842: Security Tool Development

## General infomation
- **Project Author:**  Kevin Wafula
- **Course Title:** Security Tool Development
- **Course Number:** CSC-842-DT1
- **Course Professor:** Dr. Cody Welu
- **Degree Program:** PhD in Cyber Operations
- **Degree Institution:** Dakota State University  
- **Project Description:** In fulfillment of the course CSC-842: Security Tool Development

## Cycle 1:  WebApp Attack Vector Enumerator
### Tool Overview
WebApp Attack Vector Enumerator is an interactive python tool that facilitates the mapping surface area of attack of a web application. The tool achieves this by scanning a web application to enumerate services that are running and openly accessible, querying the National Vulnerability Database (NVD) to identify Common Vulnerabilities and Exposures (CVE) associated with enumerated services, and finally querying ExploitDB to map the CVEs to exploits. The tool provides two workflows, manual step by step interactive and one step automated execution.

### Why Should You Care
During an adversarial or non-adversarial Offensive Cyber Operations (OCO) engagement, several strategies are employed during the weaponization stage of the cyber kill chain to map the surface area of attack of target web applications. Among them is identifying open services that are running on the web application hosts that have exploitable vulnerabilities. The weaponization stage requires a significant level of effort to research and validate vulnerabilities, select the appropriate exploits and against the vulnerabilities, and then pair the exploits with the appropriate backdoors to create an exploit payload. Timely and accurate identification of vulnerabilities that can be exploited successfully is critical to an effective and efficient execution of the weaponization stage and the overall OCO engagement. Leveraging a tool like WebApp Attack Vector Enumerator facilitate fast research, reviews, and selection best-fit vulnerabilities and associated exploits.

### Three Main Ideas
1. Not all vulnerabilities are exploitable. Some vulnerabilities are only theoretical, they do not have known exploit in the wild. Quick identification and elimination of such vulnerabilities from consideration is critical to efficiency.
2. Not all exploitable vulnerabilities are best candidate for selection in an OCO engagement. Some exploitable vulnerabilities have system configuration dependencies that must be true for a successfully exploitation condition to exist. Knowledge and validation of dependent system configuration is critical for effectiveness and efficiency.
3. Not all exploitable vulnerabilities are best candidate for selection in an OCO engagement. Some exploitable vulnerabilities can trigger a system failure and foil the engagement.

### Technical Requirements
 1. NMap scanner
 2. libxml2-utils
 3. National Vulnerability Database (NVD)
 4. ExploitDB 
 6. Ubuntu 22.0 OS Host
 7. Python3
 8. Python3-pip
 9. nvdlib-0.7.4
 
### Installation
1. Install Nmap Scanner
   - sudo apt-get install nmap -y
   - sudo apt-get install libxml2-utils -y
3. Download ExploitDB repo and configure Searchsploit
   - cd /opt
   - sudo git clone https://gitlab.com/exploit-database/exploitdb.git /opt/exploitdb
   - sudo cp /opt/exploitdb/.searchsploit_rc ~/
   - sudo ln -sf /opt/exploitdb/searchsploit /usr/local/bin/searchsploit
   - sudo apt-get install curl
   - sudo apt-get install python3-pip
   - sudo pip install nvdlib
   - sudo mkdir /opt/csc-842
   - sudo mkdir /opt/csc-842/01-attacl-surface-enumerator
5. Download WebApp Attack Vector Enumerator
6. Update the NVD API Key
- Excerpt:
   - Line 30: #Replace the NVD API key value ='aaaaaa-aaaaaaa-aaaaaa-aaaaa--aaaaa-aaaa' with a ligitimate key, 'aaaaaa-aaaaaaa-aaaaaa-aaaaa--aaaaa-aaaa' is a dummy entry
   - Line 31: #subscribe for a key @ https://nvd.nist.gov/developers/request-an-api-key
   - Line 32: cve_list = nvdlib.cve.searchCVE(keywordExactMatch=True, keywordSearch= srvc_prod_name, key='aaaaaa-aaaaaaa-aaaaaa-aaaaa--aaaaa-aaaa')
8. Run WeApp Attack Vector Enumerator with sudo

### Video Demo
The following is the link to the vidoe demonstration of the tool.
https://youtu.be/EVDXDJkA83U

### Future Direction
Further research should be done to map the vulnerabilities and exploits to the MITRE ATT&amp;CK framework to enumerate APT groups that have leveraged identified vulnerabilities and exploits, and enumerate associated TTPs and IoCs. This can facilitate adversary emulation assessment exercises to test organization cyber resiliency postures.

### Additional Resources
1. NVD API - https://nvd.nist.gov/developers/vulnerabilities
2. ExploitDB Repo - https://gitlab.com/exploit-database/exploitdb
3. NMAP - https://nmap.org/
4. NVDLIB - https://nvdlib.com/en/latest/v1/v1.html

## Cycle 2:
