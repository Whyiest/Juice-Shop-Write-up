# Juice-Shop Write-up: Login Bender Challenge

## Challenge Overview

**Title:** Login Bender\
**Category:** Injection Flaws\
**Difficulty:** ⭐⭐⭐ (3/6)

This challenge focuses on exploiting an SQL injection vulnerability to bypass authentication mechanisms and gain unauthorized access to a user's account, specifically targeting the account associated with "Bender" in the application.

## Tools Used

- Web browser

## Methodology and Solution

### Locating Target Information

1. **Identify Bender's Email**:
   - Logged into the application as an admin to access administrative functionalities.
   - Located Bender's email (`bender@juice-sh.op`) within the admin panel :

   <img src="../assets/difficulty3/login_bender_1.png" alt="bender username from administration panel" width="500px">

### Performing SQL Injection

2. **Attempt to Login as Bender**:
   - Navigated to the login page of the application.
   - Entered Bender's email in the email field.
   
3. **Constructing the SQL Injection**:
   - Modified the entry in the email input field to include an SQL injection payload: `bender@juice-sh.op' AND '1'='1' --`.
   - This payload attempts to manipulate the SQL query behind the login form by closing off the email string (with a single quote), adding a condition that always evaluates to true (`AND '1'='1'`), and then commenting out the remainder of the SQL command with `--`.

### Observing the Outcome

4. **Observe Authentication Bypass**:
   - With the payload submitted, the SQL query altered by the injection would incorrectly authenticate the session as Bender without requiring a password.
   - Successfully logged in as Bender, demonstrating the exploitation of the SQL injection vulnerability.

   <img src="../assets/difficulty3/login_bender_2.png" alt="login proof" width="500px">

## Solution Explanation

This challenge was resolved by exploiting a classic SQL injection vulnerability in the login form's email field. The specific vulnerability allowed for manipulation of the underlying SQL query, enabling unauthorized access to Bender's account by always making the conditional part of the query true and bypassing password verification.

## Remediation

To prevent such vulnerabilities in real applications:
- **Use Prepared Statements**: Implement prepared statements with parameterized queries to handle SQL commands. This practice prevents SQL injection by separating SQL logic from data.
- **Employ Proper Input Validation**: Ensure that all user inputs are properly validated and sanitized to prevent malicious data from affecting SQL commands.
