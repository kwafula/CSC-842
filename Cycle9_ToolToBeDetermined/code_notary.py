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
# 5. TLS ACME validation (Offline)
# 6. Create public-key and private-key pair *
# 7. Create hash *
# 8. Encrypt hash*
# 9. Encode digital signature and algorithm in QR Code*
# 11. Load QR Code *
# 12. Decrypt hash *
# 13. Verify hash * 

#  # # Setup/Installation
# 1. Install snapd (Ubuntu)
#    - sudo apt-get update y
#    - sudo apt-get snapd y
# 2. Update Snapd
#    - sudo snap install core; sudo snap refresh core
# 3. Install Certbot
#    - sudo snap install --classic certbot
# 4. Initialize Certbot to ensure it can be run
#    - sudo ln /snap/bin/certbot /usr/bin/certbot
# 5. 

