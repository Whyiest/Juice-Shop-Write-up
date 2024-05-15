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

# Challenge list

## Difficulty 1 Star (⭐)

- [Bonus Payload](1-star/Bonus%20Payload.md) - Cross-Site Scripting (XSS)
- [Confidential Document Challenge](1-star/Confidential%20Document%20Challenge.md) - Sensitive Data Exposure
- [DOM XSS](1-star/DOM%20XSS.md) - Cross-Site Scripting (XSS)
- [Exposed Metrics Challenge](1-star/Exposed%20Metrics%20Challenge.md) - Sensitive Data Exposure
- [Outdated Allowlist](1-star/Outdated%20Allowlist.md) - Unvalidated Redirects
- [Repetitive Registration Challenge](1-star/Repetitive%20Registration%20Challenge.md) - Improper Input Validation
- [Web3 Sandbox Challenge](1-star/Web3%20Sandbox%20Challenge.md) - Broken Access Control
- [Zero Stars Challenge](1-star/Zero%20Stars%20Challenge.md) - Improper Input Validation

## Difficulty 2 Stars (⭐⭐)

- [Admin Section](2-stars/Admin%20Section.md) - Broken Access Control
- [Deprecated Interface](2-stars/Deprecated%20Interface.md) - Security Misconfiguration
- [Empty User Registration](2-stars/Empty%20User%20Registration.md) - Improper Input Validation
- [Five-Star Feedback](2-stars/Five-Star%20Feedback.md) - Broken Access Control
- [Login Admin](2-stars/Login%20Admin.md) - SQL Injection
- [Login MC SafeSearch](2-stars/Login%20MC%20SafeSearch.md) - Open Source Intelligence (OSINT)
- [Meta Geo Stalking](2-stars/Meta%20Geo%20Stalking.md) - Sensitive Data Exposure
- [NFT Takeover](2-stars/NFT%20Takeover.md) - Sensitive Data Exposure
- [Password Strength](2-stars/Password%20Strength.md) - Broken Authentication
- [View Basket](2-stars/View%20Basket.md) - Broken Access Control
- [Visual Geo Stalking](2-stars/Visual%20Geo%20Stalking.md) - Sensitive Data Exposure
- [Weird Crypto](2-stars/Weird%20Crypto.md) - Cryptographic Issues
- [Locate Security Policy File](2-stars/Locate%20Security%20Policy%20File.md) - OSINT/Discovery

## Difficulty 3 Stars (⭐⭐⭐)

- [Admin Registration](3-stars/Admin%20Registration.md) - Improper Input Validation
- [Bjoern’s Favorite Pet](3-stars/Bjoerns%20Favorite%20Pet.md) - OSINT (Open Source Intelligence)
- [CAPTCHA Bypass](3-stars/CAPTCHA%20Bypass.md) - Broken Anti-Automation
- [CSRF](3-stars/CSRF.md) - Broken Access Control
- [Database Schema](3-stars/Database%20Schema.md) - Information Disclosure
- [Deluxe Fraud](3-stars/Deluxe%20Fraud.md) - Improper Input Validation
- [Forged Feedback Challenge](3-stars/Forged%20Feedback%20Challenge.md) - Broken Access Control
- [Forged Review Challenge](3-stars/Forged%20Review%20Challenge.md) - Broken Access Control
- [GDPR Data Erasure](3-stars/GDPR%20Data%20Erasure.md) - Broken Authentication
- [Login Amy](3-stars/Login%20Amy.md) - Brute Force / Cryptographic Issues
- [Login Bender Challenge](3-stars/Login%20Bender%20Challenge.md) - Injection Flaws
- [Login Jim](3-stars/Login%20Jim.md) - SQL Injection (SQLi)
- [Manipulate Basket](3-stars/Manipulate%20Basket.md) - Broken Access Control
- [Mint the Honey Pot](3-stars/Mint%20the%20Honey%20Pot.md) - Improper Input Validation
- [Payback Time Challenge](3-stars/Payback%20Time%20Challenge.md) - Business Logic Errors
- [Privacy Policy Inspection](3-stars/Privacy%20Policy%20Inspection.md) - Security through Obscurity
- [Product Tempering](3-stars/Product%20Tempering.md) - Broken Access Control
- [Reset Jim's Password](3-stars/Reset%20Jims%20Password.md) - OSINT
- [Upload Size](3-stars/Upload%20Size.md) - Improper Input Validation

## Difficulty 4 Stars (⭐⭐⭐⭐)

- [Access Log](4-stars/Access%20Log.md) - Sensitive Data Exposure
- [Allowlist Bypass](4-stars/Allowlist%20Bypass.md) - Broken Access Control
- [Christmas Offer](4-stars/Christmas%20Offer.md) - Injection
- [Find the Easter Egg](4-stars/Find%20the%20Easter%20Egg.md) - Broken Access Control
- [Ephemeral Accountant](4-stars/Ephemeral%20Accountant.md) - Injection
- [Expired Coupon](4-stars/Expired%20Coupon.md) - Improper Input Validation
- [Forgotten Sales Backup Challenge](4-stars/Forgotten%20Sales%20Backup%20Challenge.md) - Sensitive Data Exposure
- [GDPR Data Theft Challenge](4-stars/GDPR%20Data%20Theft%20Challenge.md) - Sensitive Data Exposure
- [Leaked Unsafe Product](4-stars/Leaked%20Unsafe%20Product.md) - Injection
- [Legacy Typosquatting](4-stars/Legacy%20Typosquatting.md) - Cryptographic Issues
- [Reset Bender's Password](4-stars/Reset%20Benders%20Password.md) - Broken Authentication
- [Bjoern Login](4-stars/Bjoern%20Login.md) - Broken Authentication
- [Login Uvogins](4-stars/Login%20Uvogins.md) - Broken Authentication
- [Nested Easter Egg](4-stars/Nested%20Easter%20Egg.md) - Cryptographic Issues
- [NoSQL Manipulation](4-stars/NoSQL%20Manipulation.md) - Injection
- [Steganography Challenge](4-stars/Steganography%20Challenge.md) - Security through Obscurity
- [Users Credentials](4-stars/Users%20Credentials.md) - Injection
- [Vulnerable Library](4-stars/Vulnerable%20Library.md) - Vulnerable Components

## Difficulty 5 Stars (⭐⭐⭐⭐⭐)

- [Blockchain Hype](5-stars/Blockchain%20Hype.md) - Security through Obscurity
- [Change Bender's Password](5-stars/Change%20Benders%20Password.md) - Broken Authentication
- [Cross-Site Imaging](5-stars/Cross-Site%20Imaging.md) - Cross-Site Request Forgery (CSRF)
- [Email Leak](5-stars/Email%20Leak.md) - Security Misconfiguration
- [Extra Languages](5-stars/Extra%20Languages.md) - Localization
- [Frontend Typosquatting](5-stars/Frontend%20Typosquatting.md) - Insecure Deserialization
- [Kill Chatbot](5-stars/Kill%20Chatbot.md) - Application Logic
- [Leaked Access Log](5-stars/Leaked%20Access%20Log.md) - Sensitive Data Exposure
- [Reset Morty's Password](5-stars/Reset%20Mortys%20Password.md) - Security Misconfiguration
- [Supply Chain Attack](5-stars/Supply%20Chain%20Attack.md) - Vulnerable Components
- [Two-Factor Authentication Bypass](5-stars/Two-Factor%20Authentication%20Bypass.md) - Broken Authentication
- [Unsigned JWT](5-stars/Unsigned%20JWT.md) - Broken Authentication

## Difficulty 6 Stars (⭐⭐⭐⭐⭐⭐)

- [Forged Coupon](6-stars/Forged%20Coupon.md) - Cryptography
- [Forged Signed JWT](6-stars/Forged%20Signed%20JWT.md) - Vulnerable Components
- [Imaginary Challenge](6-stars/Imaginary%20Challenge.md) - Cryptographic Issues
- [Login Support Team](6-stars/Login%20Support%20Team.md) - Security Misconfiguration
- [Multiple Likes](6-stars/Multiple%20Likes.md) - Broken Anti-Automation
- [Unlock Premium Challenge](6-stars/Unlock%20Premium%20Challenge.md) - Cryptographic Issues
- [SSRF (Server-Side Request Forgery)](6-stars/SSRF%20Server-Side%20Request%20Forgery.md) - Broken Access Control
- [Wallet Depletion](6-stars/Wallet%20Depletion.md) - Cryptographic Issues


## Contributing

Even if the vast majority of challenges are covered by trhis repository, some of them remain not completed due to some technical constraints. Contributions to improve the write-ups, scripts, or any other resources in this repository are welcome. Please submit pull requests with your suggested changes or enhancements.

This repository is maintained by the community and is not officially part of the OWASP Juice Shop project. It serves as a collaborative platform for security enthusiasts and professionals to share knowledge and improve their skills in web application security.

Happy hacking!