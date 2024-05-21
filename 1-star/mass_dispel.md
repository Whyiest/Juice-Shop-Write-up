# Juice Shop Write-up: Mass Dispel Challenge

## Challenge Overview

**Title:** Mass Dispel\
**Category:** Miscellaneous\
**Difficulty:** ⭐ (1/6)

The "Mass Dispel" challenge requires participants to close multiple "Challenge solved" notifications in a single action. This challenge tests the ability to navigate and utilize application features efficiently, based on the documentation provided.

## Tools Used

- Web browser
- OWASP Juice Shop Companion Guide (Documentation)

## Methodology and Solution

To solve this challenge, the following steps were taken:

1. **Access the Companion Guide**: Visited the official OWASP Juice Shop companion guide available at the provided URL (https://pwning.owasp-juice.shop/companion-guide/latest/part1/challenges.html). This guide contains extensive documentation on the application, including how to interact with various features.

<img src="../assets/difficulty1/difficulty1/mass_dispel_1.png" alt="link to documentation" width="500px">
  
2. **Review the Documentation**: Located the section in the guide that describes handling multiple notifications. The documentation indicated that multiple notifications could be closed simultaneously by holding the `Shift` key and clicking the close button on one of the notifications.

<img src="../assets/difficulty1/difficulty1/mass_dispel_2.png" alt="documentation" width="500px">

3. **Apply the Technique**: Opened the OWASP Juice Shop web interface, completed several challenges to generate multiple "Challenge solved" notifications, then used the `Shift` click method to close all notifications at once as described in the guide.

## Solution Explanation

The solution leverages a documented feature of the OWASP Juice Shop application that allows users to manage their interface more efficiently. By using the `Shift` key while closing a notification, the application is programmed to close all visible notifications simultaneously. 

## Remediation

No remediation is necessary as this challenge is designed to teach the user about specific features of the Juice Shop application rather than expose a security vulnerability. However, understanding and utilizing documentation effectively is a critical skill in both CTF contexts and real-world application usage.
