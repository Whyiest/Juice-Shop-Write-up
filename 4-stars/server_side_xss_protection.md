# Juice-Shop Write-up: Server-side XSS Protection

## Challenge Overview
**Title:** Server-side XSS Protection  
**Category:** Cross-Site Scripting (XSS)  
**Difficulty:** ⭐⭐⭐⭐ (4/6)  

The objective of this challenge is to perform a persisted XSS attack with `<iframe src="javascript:alert('xss')">` by bypassing a server-side security mechanism.

## Tools Used
- **Web Browser:** For navigating the Juice Shop application and accessing developer tools.
- **Burp Suite:** For intercepting and modifying HTTP requests to test for injection points.
- **Text Editor:** For crafting and testing payloads.

## Methodology and Solution

### Step 1: Identifying the Vulnerable Input
The challenge involves finding an input field that reflects user input on the server-side. The complaint page is a good candidate for this test:
1. **Navigate to Contact Page:** Go to `http://localhost:3000/#/complaints`.
2. **Submit a Test Message:** Enter a test message and intercept the request using Burp Suite to analyze the parameters.

### Step 2: Understanding Server-side Sanitization
The `package.json` file on the server, accessible at `http://localhost:3000/ftp/package.json`, reveals the use of the "sanitize-html" library version 1.4.2.

### Step 3: Identifying Vulnerability in "sanitize-html"
Researching the "sanitize-html" library, we found a vulnerability in issue #29 on GitHub (https://github.com/apostrophecms/sanitize-html/issues/29):
- **Vulnerability Description:** Sanitization is not applied recursively, allowing certain masking attacks to bypass the sanitization process.
- **Example from Issue:** 
  ```html
  I am not harmless: <<img src="csrf-attack"/>img src="csrf-attack"/> 
  ```
  is sanitized to:
  ```html
  I am not harmless: <img src="csrf-attack"/>
  ```

### Step 4: Crafting the XSS Payload
To exploit this vulnerability, we need to construct a payload that leverages the incomplete sanitization:
- **Payload:**
  ```html
  <<script>Foo</script>iframe src="javascript:alert('xss')">
  ```

### Step 5: Injecting the Payload
1. **Input Field:** Use the complaint form's message field to inject the payload.
3. **Submit Payload:** Ensure the payload is submitted successfully.

### Step 6: Verifying the XSS Execution
1. **Navigate to Reflected Input:** Visit the page where the input is reflected (e.g., admin view of contact messages).
2. **Observe Execution:** Verify if the alert box with `xss` appears, confirming the successful XSS attack.

## Solution Explanation
The challenge was solved by exploiting a vulnerability in the "sanitize-html" library, which does not sanitize HTML recursively. By crafting a payload that takes advantage of this, we bypassed the sanitization and executed a persisted XSS attack.

## Remediation
- **Update Library:** Use an updated version of "sanitize-html" that addresses recursive sanitization.
- **Input Validation and Sanitization:** Implement additional layers of input validation and sanitization to ensure all inputs are clean.
- **Output Encoding:** Always encode user inputs when rendering them on the page to prevent XSS.

