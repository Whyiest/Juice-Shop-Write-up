# Juice-Shop Write-up: Imaginary Challenge

## Challenge Overview

**Title:** Imaginary Challenge  
**Category:** Cryptographic Issues  
**Difficulty:** ⭐⭐⭐⭐⭐⭐ (6/6)

The "Imaginary Challenge" is a metaphorical challenge within OWASP Juice Shop, designed to emphasize understanding the environment and using creative problem-solving skills.

## IMPORTANT NOTE

**_This challenge is not well documented, please feel free to open a pull request if you have find a way to complete it in a proper manner._**

## Tools Used

- **Web Browser:** To interact with the Juice Shop application.
- **Code Review:** Analysis of the package.json and related scripts.

## Methodology and Solution

### Step 1: Initial Analysis

Given that the challenge hinted at its non-existence, I started by investigating the infrastructure of the Juice Shop, focusing on how challenges are typically resolved—specifically looking at the mechanics of "ContinueCodes" used to validate challenge completions.

### Step 2: Investigating `package.json`

Upon reviewing `package.json`, I discovered a dependency called `hashid`, which is used for encoding and decoding hash-like identifiers. This was a potential tool for generating or decoding `ContinueCodes`.

### Step 3: Research and External Write-up Consultation

Since no direct approach yielded results, I turned to existing community write-ups for insights. It was noted that the challenge initially depended on functionality provided by `hashid` which no longer existed in its original form. In fact, they have a website, and on this website, few years ago, they were displaying a link to a codepen that allow to test hashid. Actually, hashid was sell to another company, and the webpage was redesign, and the codepen removed. 

### Step 4: Theoretical Solution

The original solution would have been the following:
- Using the `hashid` demonstration to encode the number 999 with the specific salt by default givent by the demonstration.
- This would generate a `ContinueCode`.
- Applying this `ContinueCode` via a PUT request to:
  ```
  http://localhost:3000/rest/continue-code/apply/{ContinueCode}
  ```
  where `{ContinueCode}` would be the output from the `hashid` encoding.


## Solution Explanation

The challenges shows that it can be dangerous to keep default values of softwares, especially if they are use in a security context.

## Remediation

- **Default Values:** When using a tool, never use his defaults values.