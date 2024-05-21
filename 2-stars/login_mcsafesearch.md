# Juice-Shop Write-up: Login MC SafeSearch

## Challenge Overview

**Title:** Login MC SafeSearch\
**Category:** Open Source Intelligence (OSINT)\
**Difficulty:** ⭐⭐ (2/6)

This challenge involves using OSINT techniques to uncover the password for the user account of MC SafeSearch. 

## Tools Used

- **Web Browser**: Essential for conducting online searches and accessing various social media and video platforms.
- **Search Engines**: Google and other search engines for finding relevant information and tracing the digital footprint of the username.

## Methodology and Solution

### Initial Clue Analysis

1. **Examine the Provided Information**:
   - The challenge provided a user comment which mentioned lyrics from the movie "Frozen." This initial clue, however, did not directly help in finding the password.

### OSINT Investigation

2. **Social Media and Content Search**:
   - An extensive search around the theme of "Frozen" does not produced signfificant results.
   - Search about username of the user led to discovering a video by a rapper who discusses passwords in his content. 
   - In the video, the rapper mentioned a unique naming convention for his password involving his dog named Mr. Noodles, with modifications to replace certain letters with numbers.

3. **Password Hypothesis and Testing**:
   - Based on the video, the password "Mr. N00dles" was hypothesized, replacing 'o' with '0' as commonly found in password creation strategies to add complexity.

4. **Attempt Login**:
   - Using the derived password "Mr. N00dles" to attempt a login successfully granted access to MC SafeSearch’s account.

### Solution Explanation

The challenge was successfully resolved by using publicly available video content to derive the password. 

## Remediation

To mitigate such vulnerabilities in real-world scenarios, consider the following strategies:

- **Stronger Password Policies**: Implement and enforce policies that discourage the use of easily guessable passwords, even if they include number substitutions for letters.
- **Education and Awareness**: Train users on the importance of using non-predictable passwords that do not relate directly to publicly known information about them, such as pet names, favorite movies, etc.
- **Use of Multi-Factor Authentication (MFA)**: Adding an additional layer of security with MFA can significantly reduce the risk of unauthorized access, even if a password is compromised or guessed.

