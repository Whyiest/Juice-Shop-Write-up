# Juice-Shop Write-up: Bonus Payload

## Challenge Overview

**Title:** Bonus Payload\
**Category:** Cross-Site Scripting (XSS)\
**Difficulty:** ⭐ (1/6)

Following the previous DOM XSS challenge, this "Bonus Payload" challenge requires to inject a more complex XSS payload involving an iframe that embeds a SoundCloud player. 

## Tools Used

- **Web Browser**: For executing the attack and observing its effects.

## Methodology and Solution

### Understanding the Payload

The given payload is an iframe designed to embed a SoundCloud music player into the application's DOM dynamically. This payload, while not malicious in nature, illustrates the potential for embedding arbitrary third-party content via XSS, which could lead to phishing attacks, unwanted advertisements, or malicious scripts.

### Steps Taken to Solve the Challenge

1. **Craft and Encode the Payload**:
   - The provided iframe code was URL-encoded to ensure it would be processed correctly by the web browser when passed as a query parameter.
   - The complete URL with the injected payload looked like this: `http://127.0.0.1:3000/#/search?q=%3Ciframe%20width%3D%22100%25%22%20height%3D%22166%22%20scrolling%3D%22no%22%20frameborder%3D%22no%22%20allow%3D%22autoplay%22%20src%3D%22https:%2F%2Fw.soundcloud.com%2Fplayer%2F%3Furl%3Dhttps%253A%2F%2Fapi.soundcloud.com%2Ftracks%2F771984076%26color%3D%2523ff5500%26auto_play%3Dtrue%26hide_related%3Dfalse%26show_comments%3Dtrue%26show_user%3Dtrue%26show_reposts%3Dfalse%26show_teaser%3Dtrue%22%3E%3C%2Fiframe%3E`

2. **Execute the Attack**:
   - By navigating to the manipulated URL, the iframe successfully rendered within the web application, embedding the SoundCloud player as intended.

### Solution Explanation

The challenge was completed by demonstrating that it was possible to inject a complex iframe element into the web application via an XSS vulnerability. The iframe, in this case, embedded a SoundCloud player, showing how attackers could utilize XSS to insert almost any content into a vulnerable web application.

## Remediation

To protect against such XSS attacks, particularly those involving complex payloads like the one used in this challenge, follow these recommendations:

- **Content Security Policy (CSP)**: Implement a CSP that restricts the sources from which scripts and iframes can be loaded. This policy helps prevent the execution of unauthorized scripts and embedding of undesired external content.
- **Input Sanitization**: Ensure all user inputs are sanitized before being included in the DOM. This includes encoding or stripping out HTML elements from user inputs.
