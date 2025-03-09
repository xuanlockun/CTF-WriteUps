* When I downloaded the challenge files, I noticed there were two registry files: HKCU and HKLM/Software. Based on the name of the challenge "Persist", I immediately thought about Malware Persistence on Windows, which often leverages the Windows registry to maintain persistence.
* First, I used the reglookup tool to analyze the HKCU file and saved the output for easier searching
`reglookup HKCU > output.txt`
![alt text](image.webp)

* From experience, I know that suspicious registry entries are often located in paths like:
`Software\Microsoft\Windows\CurrentVersion\Explorer`

* After spending some time searching through the registry keys, I found a suspicious Base64-encoded string located in this path
`/Software/Microsoft/Windows/CurrentVersion/Explorer/ComDlg32/`

* Next, I used dcode.fr (online) to decode this Base64 string. The result was a decoded string, but it was still encrypted

![alt text](image0.png)

* To identify the type of encryption, I attempted to analyze the string using various online tools. After some testing, I discovered that the string was encrypted using the Vigenere Cipher

![alt text](image1.png)

* Then i successfully decrypted it with Vigenere and obtained the final flag
  
![alt text](image2.png)

### Flag

* `VISHWACTF{b3l1ef_in_r3g_p0wer}`
