# Juice-Shop Write-up: Login Jim

## Challenge Overview

**Title:** Login Jim\
**Category:** SQL Injection (SQLi)\
**Difficulty:** ⭐⭐⭐ (3/6)

The "Login Jim" challenge needs exploiting an SQL Injection vulnerability to bypass login mechanisms and gain unauthorized access to a user account, specifically Jim's. 

## Tools Used

- **Web Browser**: For interacting with the login interface of the application.

## Methodology and Solution

### Identifying the Vulnerability

1. **Initial Login Attempt**:
   - Like the previous admin account challenge, the first step involves checking the login form for SQL Injection vulnerabilities. Input fields where user credentials are entered are common points of exploitation.

### Executing the SQL Injection

2. **Crafting the Injection Query**:
   - Input a crafted SQL command into the username or password field that alters the backend SQL query to always return true. Common SQLi payloads involve using `' OR '1'='1' --` to manipulate the SQL query.
   - For Jim, the payload would be entered in the username or password field: `' OR '1'='1' --`. This payload effectively makes the SQL query behind the authentication form return true, bypassing the need for a correct username and password.

   <img src="image.png" alt="sql injection" width="500px">

### Gaining Access

3. **Accessing Jim’s Account**:
   - After submitting the SQLi payload through the login form, the application processes the altered SQL query, which incorrectly authenticates the session as Jim due to the query returning a true value.
   - Successfully bypass the authentication, granting access to Jim’s account without knowing the actual credentials.

### Solution Explanation

The challenge was completed by exploiting a SQL Injection vulnerability within the login process. This type of vulnerability arises when inputs are not properly sanitized, allowing an attacker to inject malicious SQL code. 

## Remediation

To prevent such vulnerabilities in real-world applications:

- **Use Prepared Statements and Parameterized Queries**: These are much safer than constructing queries directly from user input, as they automatically handle the necessary escaping of inputs, thus preventing SQL injection.
- **Regular Security Audits and Testing**: Conduct vulnerability assessments and security audits regularly. Use tools and techniques to detect SQL injection vulnerabilities before attackers do.
- **Error Handling**: Do not display database error messages to users. Use generic error messages to avoid giving attackers hints about the database structure.
