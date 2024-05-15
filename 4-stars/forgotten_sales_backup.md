# Juice-Shop Write-up: Forgotten Sales Backup Challenge

## Challenge Overview

**Title:** Forgotten Sales Backup\
**Category:** Sensitive Data Exposure\
**Difficulty:** ⭐⭐⭐⭐ (4/6)

This challenge involves accessing a backup file left forgotten on a vendor's server. The task highlights the risk of sensitive data exposure due to improperly secured backup files accessible via a public interface.

## Tools Used

- Web browser

## Methodology and Solution

To successfully complete the "Forgotten Sales Backup" challenge, the following steps were taken:

1. **Access the FTP Server**: Navigated to the FTP server directory listing at `127.0.0.1:3000/ftp`, which was discovered in a previous challenge (Privacy Policy). This server hosted various files, including backups and configuration files.

2. **Identify the Target File**: Scanned through the list of files and identified `coupons_2013.md.bak` as a likely candidate for containing sensitive sales data due to its naming convention indicating it's a backup file.

<img src="../assets/difficulty4/forgotten_sales_backup.png" alt="ftp" width="500px">

3. **Exploit NULL Byte Injection**: Utilized a NULL byte injection technique to access the backup file. Many web applications do not properly sanitize input, allowing for directory traversal or file inclusion attacks if the application is improperly handling file names.
   - **Construct the URL**: Appended a NULL byte character, represented in URL encoding as `%00`, to the file request to potentially bypass any restrictions or parsing issues by the server. This was tried because older or misconfigured servers might treat the NULL byte as a string terminator, thus ignoring any file extension checks or other controls.
   - **Request the File**: Accessed the URL `http://127.0.0.1:3000/ftp/coupons_2013.md.bak%00.md` in a browser.

4. **Review the Data**: Upon successful retrieval, reviewed the content of `coupons_2013.md.bak` for any sensitive information, confirming the exposure of sales data or discount coupons that should not have been publicly accessible.

## Solution Explanation

The challenge demonstrated an exposure of sensitive data due to a misconfigured FTP server that allowed public access to backup files. The use of NULL byte injection to access the file underscored a common vulnerability in how servers handle file paths and extensions, particularly in systems not properly sanitizing user inputs or correctly handling file strings.

## Remediation

- **Proper Access Controls**: Ensure that backup files are not stored in publicly accessible directories. Use proper access control mechanisms to restrict access.
- **Regular Audits and Cleanups**: Perform regular audits of storage locations and cleanup legacy or unused files to prevent accidental exposure.
- **Input Sanitization**: Enhance security measures to sanitize user inputs, especially in file retrieval functionalities, to prevent directory traversal or file inclusion attacks.

