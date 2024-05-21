# Juice-Shop Write-Up: Reset Bjoern's Password

## Challenge Overview

**Title:** Reset Bjoern's Password\
**Category:** OSINT/Forensic\
**Difficulty:** ⭐⭐⭐⭐⭐ (5/6)

This challenge entails resetting the password for Bjoern Kimminich's account on the `juice-sh.op` platform by correctly answering his security question about a postal code. The challenge leverages open-source intelligence (OSINT) techniques to gather information from various personal and social media profiles to identify the correct postal code for password recovery.

## Tools Used

- **Web Browser**: For accessing and analyzing information on social media and personal websites.
- **OSINT Techniques**: Used to gather, correlate, and analyze publicly available information.

## Methodology and Solution

### Gathering Information

1. **Profile Analysis**:

   - Here is the security question : 

   <img src="../assets/difficulty5/reset_bjoern_password_1.png" alt="security question" width="500px">

   - Examine Bjoern Kimminich’s social media profiles and personal website to collect any publicly available information about his locations and related postal codes.

   Twitter : https://twitter.com/bkimminich?lang=fr
   Portfolio : https://bkimminich.github.io/
   Facebook : https://www.facebook.com/bjoern.kimminich/

   - Note significant life events, places of education, and employment which might be linked to specific postal codes :

   <img src="../assets/difficulty5/reset_bjoern_password_2.png" alt="facebook" width="500px">


   - Here is postals codes recovered : 

        -	25436
        -	65479
        -	25337



### Correlation and Hypothesis

2. **Historical Data on Postal Codes**:
   - We have identified the current postal code from Bjoern's profiles (25436 for Uetersen). This code is not working, but I read on a forum that Germany have made a major update in the way that they manage theirs postals codes.
   - So I had use a tool to find older postal code using newer one. The tool used is : `https://www.alte-postleitzahlen.de`, acknowledging that the security question might reference an outdated code.

### Testing Hypotheses

3. **Trial and Error**:
   - Test all gathered postal codes using the account recovery option to see which one successfully answers the security question.
   - Include both current and historical postal codes in the tests.

### Successful Reset

4. **Resetting the Password**:
   - Discover that the historical postal code "West-2082" (pre-reform code for Uetersen) is the correct answer to the security question, allowing for the password reset.

## Solution Explanation

The challenge was successfully solved by analyzing publicly available information to identify potential postal codes associated with Bjoern’s life and career. Recognizing that the security question might refer to an outdated postal code was key. This required correlating current information with historical data on postal codes to find the one that matched the security question's requirements.

## Remediation

To safeguard against similar attacks:

- **Complex Security Questions**: Choose security questions that are not easily answerable with publicly available information.
- **Limit Personal Data Exposure**: Be cautious about the amount of personal information shared publicly on social media and personal websites.
- **Remove Security QUestions**: Using security questions is not considered as secure, you rather may rely on an email sended to user that want to reset their password.