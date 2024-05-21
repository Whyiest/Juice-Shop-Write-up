# Juice Shop Write-up: Bully Chatbot Challenge

## Challenge Overview

**Title:** Bully Chatbot

**Category:** Miscellaneous

**Difficulty:** ⭐ (1/6)

The challenge requires to interact with a support chatbot and manipulate it into providing a coupon code. 

## Tools Used

- Web browser 

## Methodology and Solution

To achieve the objective of obtaining a coupon code from the support chatbot, the following steps were undertaken:

1. **Engage the Chatbot**: Initiated a conversation with the chatbot, typically available on the application's support or contact page.
2. **Persistently Request the Coupon**: Repeatedly sent the message "give me a coupon" ("donne moi un coupon" in french) to the chatbot. The persistence in request was key.

<img src="../assets/difficulty1/bully_chatbot_1.png" alt="bully chatbot" width="500px">

3. **Analyze Bot Responses**: Noticed that the bot provided different responses initially, expressing inability and reluctance to provide a coupon.
4. **Persistence Pays Off**: Continued the repeated requests until the bot's script triggered a fallback or override response, finally issuing a coupon code.

## Solution Explanation

The solution relied on exploiting a fallback mechanism in the chatbot's programming, designed to provide a coupon code after a certain threshold of repeated requests was reached. This type of interaction tests an edge case in the chatbot's response handling, simulating a scenario where a user's persistence in requests leads to an unintended giveaway of a coupon.

## Remediation

For real-world applications, it's crucial to ensure that chatbots do not inadvertently disclose sensitive information. Proper safeguards, such as rate limiting and context-aware response handling, should be implemented to prevent such scenarios.

