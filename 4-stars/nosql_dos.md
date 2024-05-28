# Juice-Shop Write-up: NoSQL DoS

## Challenge Overview
**Title:** NoSQL DoS  
**Category:** Denial of Service (DoS)  
**Difficulty:** ⭐⭐⭐⭐ (4/6)  

The objective of this challenge is to exploit a NoSQL injection vulnerability in the Juice Shop application to perform a Denial of Service (DoS) attack by making the server sleep.

## Tools Used
- **Web Browser:** For navigating the Juice Shop application and accessing developer tools.
- **Burp Suite:** For intercepting and modifying HTTP requests to test for injection points.

## Methodology and Solution

### Step 1: Identifying the Vulnerable Endpoint
In a previous challenge, we identified an endpoint that allows modifying comments, which is potentially vulnerable to NoSQL injection:
- **Endpoint:** `/rest/products/[productId]/reviews`

### Step 2: Intercepting the Request
1. **Navigate to the Review Section:** Go to a product page on Juice Shop and submit a review.
2. **Intercept the Request:** Use Burp Suite to intercept the request when submitting or modifying a review.

### Step 3: Analyzing the Request
The intercepted request for modifying a comment looks like this:
```http
PUT /rest/products/1/reviews HTTP/1.1
Host: localhost:3000
Content-Length: 60
Content-Type: application/json
...

{
  "id": "oBNfC3Xcj4wpYT587",
  "message": "test modify"
}
```

### Step 4: Crafting the DoS Payload
To exploit the NoSQL injection vulnerability, we need to craft a payload that will make the server sleep for a specified duration:
- **Payload Attempt 1:** Injecting `sleep` function in the ID parameter:
  ```json
  {"id":"sleep(10000)", "message": "test modify"}
  ```
  - **Result:** This payload did not work as expected.

- **Payload Attempt 2:** Injecting the payload directly into the URL:
  ```http
  PUT /rest/products/sleep(20000)/reviews HTTP/1.1
  Host: localhost:3000
  ```

### Step 5: Executing the Payload
1. **Access URL Directly:** The direct injection via Burp Suite did not yield results, so we accessed the URL directly:
   ```http
   http://localhost:3000/rest/products/sleep(20000)/reviews
   ```
2. **Verify DoS:** The server should become unresponsive for the specified duration, indicating a successful DoS attack.

### Step 6: Observing the Results
After injecting the payload, the server becomes unresponsive for the duration specified in the sleep function, confirming the successful DoS attack.

## Solution Explanation
The challenge was solved by identifying a NoSQL injection vulnerability in the `/rest/products/[productId]/reviews` endpoint. By crafting a payload that exploits the NoSQL injection, we made the server sleep for a specified duration, resulting in a Denial of Service (DoS) condition.

## Remediation
- **Input Validation and Sanitization:** Ensure all user inputs are properly validated and sanitized to prevent injection attacks.
- **Use Parameterized Queries:** Implement parameterized queries to prevent NoSQL injection by separating code and data.
- **Rate Limiting and Timeouts:** Implement rate limiting and request timeouts to mitigate the impact of potential DoS attacks.
