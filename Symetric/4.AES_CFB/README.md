# Cipher Feedback mode (CFB)

1. Uses Encrypts IV with AES to generate keystream
2. XOR keystream with block/message to create ciphertext
3. Feed ciphertext back to the AEX encryption function to produce next keystream
4. Used the generated keystream to encrypt next block