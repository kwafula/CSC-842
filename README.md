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
 2. ExploitDB 
 3. NVD
 4. Ubuntu 22.0 OS Host
 5. Python3
 6. Python3-pip
 7. nvdlib-0.7.4
 
### Installation
1. Install Nmap Scanner
2. Download ExploitDB repo and configure Searchsploit
3. Download and run WebApp Attack Vector Enumerator

### Video Demo
The following is the link to the vidoe demonstration of the tool.
Video and code will be postedtoday 5/22/2023 evening

### Future Direction
Further research should be done to map the vulnerabilities and exploits to the MITRE ATT&amp;CK framework to enumerate APT groups that have leveraged identified vulnerabilities and exploits, and enumerate associated TTPs and IoCs. This can facilitate adversary emulation assessment exercises to test organization cyber resiliency postures.

### Additional Resources
1. NVD API - https://nvd.nist.gov/developers/vulnerabilities
2. ExploitDB Repo - https://gitlab.com/exploit-database/exploitdb
3. NMAP - https://nmap.org/
4. NVDLIB - https://nvdlib.com/en/latest/v1/v1.html

## Cycle 2:
