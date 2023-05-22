# DSU Course CSC-842: Security Tool Development

## General infomation
- **Project Author:**  Kevin Wafula
- **Course Title:** Security Tool Development
- **Course Number:** CSC-842-DT1
- **Course Professor:** Dr. Cody Welu
- **Degree Program:** PhD in Cyber Operations
- **Degree Institution:** Dakota State University  
- **Project Description:** In fulfillment of the course CSC-842: Security Tool Development
- **Version Control:** Draft revision 1.0

## Cycle 1:  WebApp Attack Vector Enumerator
### Tool Overview
WebApp Attack Vector Enumerator is an interactive python tool that facilitates the maping surface area of attack of a web application. The tool acheives this by scanning a web application to enumerate services that are running and openly accessible, queriying the National Vulnerability Database (NVD) to identify Common Vulnerabilities and Exposures (CVE) associated with enumerated services, and finally qeuriying ExploitDB to map the CVEs to exploits. The tool provides two workflows, manual step by step interactive and one step automated execution.
### Why Should You Care
During an adversarial or non-adversarial Offensive Cyber Operations (OCO) engagement, several strategies are employed during the weaponization stage of the cyber kill chain to map the surface area of attack of target web applications. Among them is identifying open services that are running on the web application hosts that have exploitable vulnerabilities. The weaponization stage requires a significant level of effort to research and validate vulnerabilities, select the appropriate exploits and against the vulnerabilities, and then pair the exploits with the appropriate backdoors to create an exploit payload. Timely and accurate identification of vulnerabilities that can be explioted successfully is critical to an effective and efficient execution of the weaponization stage and the overall OCO engagement. Leveraging a tool like WebApp Attack Vector Enumerator facilitate fast research, reviews, and selection best-fit vulnerabilities and associated exploits.
### Three Main Ideas
1. Not all vulnerabilities are expliotable. Some vulnerabilities are only theoritical, they do not have known exploit in the wild. Quick identification and elimination of such vulnerabilities from consideration is critical to efficiency.
2. Not all exploitable vulnerabilities are best candidate for selection in an OCO engagement. Some exploitable vulnerabilities have system configuration dependencies that must be true for a successfuly exploitation condition to exist. Knowledge and validation of dependent system configuration is critical for effectiveness and efficiency.
3. Not all exploitable vulnerabilities are best candidate for selection in an OCO engagement. Some exploitable vulnerabilities can trigger a system failure and foil the engagement.
### Technical Requirements
 1. Nmap scanner
 2. ExploitDB Searchsploit
 3. NVD
 4. Ubuntu 22.0 OS
### Installation
1. Install Nmap Scanner
2. Download ExploitDB repo and configure Searchsploit
3. Download and run WebApp Attack Vector Enumerator
### Video Demo

### Future Direction
Further research should be done to map the vulnerabilites and exploits to the MITRE ATT&CK framework to enumerate APT groups that have leveraged identified vulnerabilities and exploits, and enumerate associated TTPs and IoCs. This can facilitate adversary emulation assessment exercises to test organization cyber resilliency postures.

### Additional Resources
1. NVD API - https://nvd.nist.gov/developers/vulnerabilities
2. ExploitDB Repo - https://gitlab.com/exploit-database/exploitdb
3. NMAP - https://nmap.org/
## Cycle 2:
