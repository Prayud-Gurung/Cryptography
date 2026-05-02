# AES with Galosis counter mode (AES-GCM)
Counter mode: Uses CTR mode for confidentiality/encryption
Galosis field authenticaiton: for integrity and authentication

Provides encryption with authentication
Generates encrypted data with tag
Nonce to randomize the encrypted data
1. Generates keystream (nonce + Counter)
2. XOR keystream with plaintext to create ciphertext

3. Using Additional Authentication Data, it generates authentication tag that verifies everything

Decryption
1. Regenerate keystream
2. Recompute authentication tag using ciphertext and AAD
3. Compare tags, if matched then the data is valid else it has been tapered with