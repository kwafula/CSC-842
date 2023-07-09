# Example uses Letsencrypt
# # # Prerequisite
# 1. Set Letsencrypt environment

# # # # Objectives
# 1. Code provenance 
#   - Digital signature
# 2. Code integrity
#  - Hash code
# 3. Code confidentiality
#   - Encryption/ One-way obfuscation

# # # Product Backlog
# 1. Install dependencies
# 2. Display help menu *
# 3. HTTP ACME validation (Offline)
# 4. DNS ACME validation (Offline)
# 5. Create public-key and private-key pair *
# 6. Create hash *
# 7. Encrypt hash*
# 8. Encode digital signature and algorithm in QR Code*
# 9. Load QR Code *
# 11. Decrypt hash *
# 12. Verify hash * 

#  # # Setup/Installation
# 1. Install snapd (if not already installed)
#    - sudo apt-get update -y
#    - sudo apt-get snapd -y
# 2. Update Snapd
#    - sudo snap install core; sudo snap refresh core
# 3. Install Certbot
#    - sudo snap install --classic certbot
# 4. Initialize Certbot to ensure it can be run
#    - sudo ln /snap/bin/certbot /usr/bin/certbot
# 5. Setup the HTTP-01 Challenge Web Server directory
# 6. 

