Python program with tkinter GUI

AES-CTR project

User can enter text and password to encrypt the text.
To decrypt the text user must enter the same password.
Also allows user to save the encrypted data in a file

While encrypting, a key is generated based on password for the file.
It uses SHA256 hash, although not secure enough, it does work for the demo
Also encorporates a bit of file handling

Possible upgrades to the project
1. Instead of user inputing the text, enabline them to load file and read line
2. Encrypting binary file, moving away from strings
3. Currently uses AES-CTR, can upgrade to AES-GCM for authenticated encryption
3. Using PBKDF2 in place of sha256 to generate keys
4. Improvement in proper error handling

AES-GCM project
User select file to be encrypted.
To decrypt user needs to provide username and password
User can then save the encrypted file
The application generates token that user must keep safe for decrypting

Uses PBKDF2 algorithm to generate key
Reads files in binary

Possible improvements
1. Menu tab to switch between encryption adn decryption
2. Label that shows the file or its filepath
3. Saving Decrypted object as txt, pdf, mp3, mp4, etc 
4. Use json to store metadata like tags, header, salt, nonce
