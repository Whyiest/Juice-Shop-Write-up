# Juice-Shop Write-up: Reset Bender's Password

## Challenge Overview

**Title:** Reset Bender's Password  
**Category:** Broken Authentication  
**Difficulty:** ⭐⭐⭐⭐ (4/6)

This challenge ask us to reset the password for the user "Bender" using the "Forgot Password" mechanism by answering his security question correctly.

## Tools Used

- **Web Browser**: For accessing the Juice Shop web application and its password reset functionality.

## Methodology and Solution

### Step 1: Gathering Initial Information

1. **Identifying User Details**:
   - The email for Bender is identified as `bender@juice-sh.op`.
   - Security question revealed: “Company you first work as adult”.

### Step 2: Answering the Security Question

2. **Initial Attempts**:
   - Based on OSINT and known details from the "Futurama" series, Bender's original employment at "Suicide Booth Incorporation" was tried first, which did not succeed.

### Step 3: OSINT and Cross-referencing Show Details

3. **Finding the Correct Answer**:
   - After re-evaluating the series details and additional OSINT, it was found that the nickname used for Bender's company in the series was “Stop’n’drop”.
   - Upon entering "Stop'n'drop" as the answer to the security question, the password reset was successfully triggered.

## Solution Explanation

The successful reset was achieved by using the known nickname of Bender's first employer from the "Futurama" series, demonstrating the potential security flaw in using easily guessable or widely known facts as security question answers.

### Security Recommendations

- **Use Strong Security Questions**: Avoid questions that can be answered through public or easily accessible information. Instead, use questions that have subjective or less predictable answers.
- **Don't use Security Questions**: Best security practice is to not use security questions for ressettings password, but rather send an email to user to confirm that he want to change his password.
- **Multi-Factor Authentication**: Implement multi-factor authentication (MFA) to strengthen the account recovery process, reducing reliance on security questions alone.
