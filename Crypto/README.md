Python program with tkinter GUI

User can enter text and password to encrypt the text.
To decrypt the text user must enter the same password.
Also allows user to save the encrypted data in a file

This project
While encrypting, a key is generated based on password for the file.
It uses SHA256 hash, although not secure enough, it does work for the demo
Also encorporates a bit of file handling

Possible upgrades to the project
1. Instead of user inputing the text, enabline them to load file and read line
2. Encrypting binary file, moving away from strings
3. Currently uses AES-CTR, can upgrade to AES-GCM for authenticated encryption
3. Using PBKDF2 in place of sha256 to generate keys
4. Improvement in proper error handling


