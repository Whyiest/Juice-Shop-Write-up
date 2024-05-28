# OWASP Juice Shop Write-Up 

<img src="./assets/public/logo.png" width="400">

Welcome to the GitHub repository dedicated to providing comprehensive write-ups for the OWASP Juice Shop CTF challenges. OWASP Juice Shop is an intentionally insecure web application designed for training, demonstrating, and testing security tools and techniques. This repository aims to offer step-by-step solutions, detailed descriptions of vulnerabilities exploited, and recommended remediations for each challenge.

## Table of Contents
- [Repository Structure](#repository-structure)
- [Challenge Levels](#challenge-levels)
- [Recommendations](#recommendations)
- [Contributing](#contributing)
- [Challenge List](#challenge-list)

## Repository Structure

- **Challenges**: Solutions are organized into folders based on their difficulty level, ranging from 1 to 6 stars (⭐-⭐⭐⭐⭐⭐⭐). Each challenge's folder contains a detailed write-up that walks through the approach taken to exploit vulnerabilities and secure the application.
- **Tools**: This folder contains all scripts and automation tools developed and used to solve the Juice Shop challenges.
- **Assets**: All images used in the individual challenge write-ups are stored in this folder. These images illustrate the steps, results, and important concepts discussed in the write-ups.
- **Files**: Contains all files downloaded from the Juice Shop website during the challenges. These files were obtained as part of solving various challenges. You can use theses files to gain some time during the completion of the CTF.
- **Achievements Backup**: The `all_achievements.json`, located inside the `Tools` folder, is a backup of the progression state in the Juice Shop CTF, which, when applied, automatically validates most of the challenges. It is provided for reference and learning purposes.

## Challenge Levels

Navigate to each folder to explore the challenges and solutions specific to that difficulty level:

- [⭐ 1-Star Challenges](https://github.com/whyiest/juice-shop-write-up/tree/main/1-star)
- [⭐⭐ 2-Star Challenges](https://github.com/whyiest/juice-shop-write-up/tree/main/2-stars)
- [⭐⭐⭐ 3-Star Challenges](https://github.com/whyiest/juice-shop-write-up/tree/main/3-stars)
- [⭐⭐⭐⭐ 4-Star Challenges](https://github.com/whyiest/juice-shop-write-up/tree/main/4-stars)
- [⭐⭐⭐⭐⭐ 5-Star Challenges](https://github.com/whyiest/juice-shop-write-up/tree/main/5-stars)
- [⭐⭐⭐⭐⭐⭐ 6-Star Challenges](https://github.com/whyiest/juice-shop-write-up/tree/main/6-stars)

## Recommendations

- **Companion Guide**: We highly recommend following along with the [official OWASP Juice Shop companion guide](https://pwning.owasp-juice.shop/companion-guide/latest/) for additional context and explanations that complement these write-ups.
- **Self-Attempt Before Reference**: While this repository is a valuable resource, we encourage you to attempt solving the challenges on your own before consulting the write-ups. This approach will maximize your learning experience and understanding of web application security.
- **Workflow**: To use this repository effectively, navigate to the challenge folder corresponding to your current challenge, read the write-up to understand the vulnerability and the remediation steps, and refer to the scripts or files as needed.

**Note**: For some challenges, not all screenshots are included in the write up, but if you need a more visual assistance, you can check inside the `assets` folder : there is chances that you find others screenshots for the current challenge.

## Challenge list

# Table of Contents

### ➤ Difficulty 1 Star (⭐)

- [Bonus Payload](1-star/bonus_payload.md) - Cross-Site Scripting (XSS)
- [Bully Chatbot](1-star/bully_chatbot.md) - Application Logic
- [Confidential Document](1-star/confidential_document.md) - Sensitive Data Exposure
- [DOM XSS](1-star/dom_xss.md) - Cross-Site Scripting (XSS)
- [Error Handling](1-star/error_handling.md) - Error Handling
- [Exposed Metrics](1-star/exposed_metrics.md) - Sensitive Data Exposure
- [Mass Dispel](1-star/mass_dispel.md) - Improper Input Validation
- [Missing Encoding](1-star/missing_encoding.md) - Improper Input Validation
- [Outdated Allowlist](1-star/outdated_allowlist.md) - Unvalidated Redirects
- [Privacy Policy](1-star/privacy_policy.md) - Information Disclosure
- [Repetitive Registration](1-star/repetitive_registration.md) - Improper Input Validation
- [Scoreboard](1-star/scoreboard.md) - Information Disclosure
- [Web3 Interface](1-star/web3_interface.md) - Broken Access Control
- [Zero Star](1-star/zero_star.md) - Improper Input Validation

### ➤ Difficulty 2 Stars (⭐⭐)

- [Admin Section](2-stars/admin_section.md) - Broken Access Control
- [Deprecated Interface](2-stars/deprected_interface.md) - Security Misconfiguration
- [Empty User Registration](2-stars/empty_user_registration.md) - Improper Input Validation
- [Five-Star Feedback](2-stars/five_star_feedback.md) - Broken Access Control
- [Login Admin](2-stars/login_admin.md) - SQL Injection
- [Login MC SafeSearch](2-stars/login_mc_safesearch.md) - Open Source Intelligence (OSINT)
- [Meta GeoStaking](2-stars/meta_geostaking.md) - Sensitive Data Exposure
- [NFT Takeover](2-stars/nft_takeover.md) - Sensitive Data Exposure
- [Password Strength](2-stars/password_strength.md) - Broken Authentication
- [View Basket](2-stars/view_basket.md) - Broken Access Control
- [Visual GeoStaking](2-stars/visual_geostaking.md) - Sensitive Data Exposure
- [Weird Crypto](2-stars/weird_crypto.md) - Cryptographic Issues
- [White Hat](2-stars/white_hat.md) - Open Source Intelligence (OSINT)
- [Reflected XSS](2-stars/reflected_xss.md) - Cross-Site Scripting (XSS)


### ➤ Difficulty 3 Stars (⭐⭐⭐)

- [Admin Registration](3-stars/admin_registration.md) - Improper Input Validation
- [Bjoern’s Favorite Pet](3-stars/bjoern_favorite_pet.md) - OSINT (Open Source Intelligence)
- [CAPTCHA Bypass](3-stars/captcha_bypass.md) - Broken Anti-Automation
- [CSRF](3-stars/csrf.md) - Broken Access Control
- [Database Schema](3-stars/database_schema.md) - Information Disclosure
- [Deluxe Fraud](3-stars/deluxe_fraud.md) - Improper Input Validation
- [Forged Feedback](3-stars/forged_feedback.md) - Broken Access Control
- [Forged Review](3-stars/forged_review.md) - Broken Access Control
- [GDPR Data Erasure](3-stars/gdpr_data_erasure.md) - Broken Authentication
- [Login Amy](3-stars/login_amy.md) - Brute Force / Cryptographic Issues
- [Login Bender](3-stars/login_bender.md) - Injection Flaws
- [Login Jim](3-stars/login_jim.md) - SQL Injection (SQLi)
- [Manipulate Basket](3-stars/manipulate_basket.md) - Broken Access Control
- [Mint the Honey Pot](3-stars/mint_the_honey_pot.md) - Improper Input Validation
- [Payback Time](3-stars/payback_time.md) - Business Logic Errors
- [Privacy Policy Inspection](3-stars/privacy_policy_inspection.md) - Security through Obscurity
- [Product Tempering](3-stars/product_tampering.md) - Broken Access Control
- [Reset Jim's Password](3-stars/reset_jim_password.md) - OSINT
- [Upload Size](3-stars/upload_size.md) - Improper Input Validation

### ➤ Difficulty 4 Stars (⭐⭐⭐⭐)

- [Access Log](4-stars/access_log.md) - Sensitive Data Exposure
- [Allowlist Bypass](4-stars/allowlist_bypass.md) - Broken Access Control
- [Christmas Special](4-stars/christmas_special.md) - Injection
- [Easter Egg](4-stars/easter_egg.md) - Broken Access Control
- [Ephemeral Accountant](4-stars/ephemeral_accountant.md) - Injection
- [Expired Coupon](4-stars/expired_coupon.md) - Improper Input Validation
- [Forgotten Sales Backup](4-stars/forgotten_sales_backup.md) - Sensitive Data Exposure
- [GDPR Data Theft](4-stars/gdpr_data_theft.md) - Sensitive Data Exposure
- [Leaked Unsafe Product](4-stars/leaked_unsafe_product.md) - Injection
- [Legacy Typosquatting](4-stars/legacy_typosquatting.md) - Cryptographic Issues
- [Login Bender](4-stars/login_bender.md) - Broken Authentication
- [Login Bjoern](4-stars/login_bjoern.md) - Broken Authentication
- [Login Uvogin](4-stars/login_uvogin.md) - Broken Authentication
- [Nested Easter Egg](4-stars/nested_easter_egg.md) - Cryptographic Issues
- [NoSQL Manipulation](4-stars/nosql_manipulation.md) - Injection
- [Poison Null Bytes](4-stars/poison_null_bytes.md) - Injection
- [Steganography](4-stars/steganography.md) - Security through Obscurity
- [User Credentials](4-stars/user_credentials.md) - Injection
- [Vulnerable Library](4-stars/vulnerable_library.md) - Vulnerable Components
- [Server Side XSS Protection](4-stars/server_side_xss_protection.md) - Cross-Site Scripting (XSS) 
- [NoSQL Dos](4-stars/nosql_dos.md) - NoSQL Injection / Denial of Service (DoS) 
- [X-Header XSS](4-stars/x_header_xss.md) - Cross-Site Scripting (XSS) 



### ➤ Difficulty 5 Stars (⭐⭐⭐⭐⭐)

- [Blockchain Hype](5-stars/blockchain_hype.md) - Security through Obscurity
- [Change Bender's Password](5-stars/change_bender_password.md) - Broken Authentication
- [Cross-Site Imaging](5-stars/cross_site_imaging.md) - Cross-Site Request Forgery (CSRF)
- [Email Leak](5-stars/email_leak.md) - Security Misconfiguration
- [Extra Language](5-stars/extra_language.md) - Localization
- [Frontend Typosquatting](5-stars/frontend_typosquatting.md) - Insecure Deserialization
- [Kill Chatbot](5-stars/kill_chatbot.md) - Application Logic
- [Leaked Access Log](5-stars/leaked_access_log.md) - Sensitive Data Exposure
- [Reset Bjoern's Password](5-stars/reset_bjoern_password.md) - Broken Authentication
- [Reset Morty's Password](5-stars/reset_morty_password.md) - Security Misconfiguration
- [Retrieve Blowprint](5-stars/retrieve_blowprint.md) - Information Disclosure
- [Supply Chain Attack](5-stars/supply_chain_attack.md) - Vulnerable Components
- [Two-Factor Authentication Bypass](5-stars/two_factor_authentification.md) - Broken Authentication
- [Unsigned JWT](5-stars/unsigned_jwt.md) - Broken Authentication
- [Local File Read](5-stars/local_file_read.md) - Server-Side Injection 
- [NoSQL Exfiltration](5-stars/nosql_exfiltration.md) - NoSQL Injection  
- [Blocked RCE Dos](5-stars/blocked_rce_dos.md) - Insecure Deserialization


### ➤ Difficulty 6 Stars (⭐⭐⭐⭐⭐⭐)

- [Forged Coupon](6-stars/forged_coupon.md) - Cryptography
- [Forged Signed JWT](6-stars/forged_signed_jwt.md) - Vulnerable Components
- [Imaginary Challenge](6-stars/imaginary_challenge.md) - Cryptographic Issues
- [Login Support Team](6-stars/login_support_team.md) - Security Misconfiguration
- [Multiples Likes](6-stars/multiples_likes.md) - Broken Anti-Automation
- [Premium Paywall](6-stars/premium_paywall.md) - Access Control
- [SSRF](6-stars/ssrf.md) - Server-Side Request Forgery
- [SSTi](6-stars/ssti.md) - Server-Side Template Injection
- [Wallet Depletion](6-stars/wallet_depletion.md) - Cryptographic Issues
- [Video XSS](6-stars/video_xss.md) - Cross-Site Scripting (XSS)
- [Arbitrary File Write](6-stars/arbitrary_file_write.md) - Vulnerable Components 
- [Successful Rce Dos](6-stars/successful_rce_dos.md) - Remote Code Execution (RCE) / Denial of Service (DoS)  




## Contributing

Even if the vast majority of challenges are covered by trhis repository, some of them remain not completed due to some technical constraints. Contributions to improve the write-ups, scripts, or any other resources in this repository are welcome. Please submit pull requests with your suggested changes or enhancements.

This repository is maintained by the community and is not officially part of the OWASP Juice Shop project. It serves as a collaborative platform for security enthusiasts and professionals to share knowledge and improve their skills in web application security.

Happy hacking!