# Juice-Shop Write-up: Nested Easter Egg

## Challenge Overview

**Title:** Nested Easter Egg  
**Category:** Cryptographic Issues  
**Difficulty:** ⭐⭐⭐⭐ (4/6)

This challenge ask us to decrypt a hidden message located within another Easter egg, emphasizing advanced cryptographic analysis to uncover the real Easter egg within the application.

## Tools Used

- **Base64 Decoder**: Used to decode encoded strings.
- **ROT13 Cipher Tool**: Employed to decrypt messages encoded with the ROT13 substitution cipher.

## Methodology and Solution

### Step 1: Decoding Base64

1. **Initial Decoding**:
   - The Easter Egg challenge provided a Base64 encoded string `L2d1ci9xcmlmL25lci9mYi9zaGFhbC9ndXJsL3V2cS9uYS9ybmZncmUvcnR0L2p2Z3V2YS9ndXIvcm5mZ3JlL3J0dA==`.
   - Decode this string using a Base64 decoder to reveal another obscured message: `/gur/qrif/ner/fb/shaal/gurl/uvq/na/rnfgre/rtt/jvguva/gur/rnfgre/rtt`.

### Step 2: Applying ROT13 Cipher

2. **ROT13 Decryption**:
   - Recognize that the decoded message appears to be gibberish, suggesting the use of a simple cipher.
   - Apply the most common cipher, ROT13 cipher, which shifts letters by 13 positions in the alphabet, to the decoded message.
   - The resulting plaintext reads: `/the/devs/are/so/funny/they/hid/an/easter/egg/within/the/easter/egg`.

### Step 3: Accessing the Nested Easter Egg

3. **Finding the Nested Easter Egg**:
   - Use the decrypted path to navigate to `127.0.0.1:3000/the/devs/are/so/funny/they/hid/an/easter/egg/within/the/easter/egg` in a web browser.

   <img src="../assets/difficulty4/nested_easter_egg_1.png" alt="nested easter egg" width="500px">

   - Successfully access the true nested Easter egg, fulfilling the challenge’s objective.

## Solution Explanation

The Nested Easter Egg challenge was an exercise in decryption that required both technical and creative thinking. Starting with a Base64 encoded string, we first had to decode it to a seemingly nonsensical message, which then needed further decryption using the ROT13 cipher, a simple but common text transformation.

This challenge exemplifies the use of multi-layered security measures where information is obscured through more than one method, increasing the difficulty of unauthorized access. 

## Remediation

To protect against unauthorized data decryption:
- **Multi-factor Encryption**: Use multiple encryption layers with different keys or methods to enhance security.
- **Encryption Best Practices**: Regularly update encryption methods and use strong, non-standard algorithms where possible.
