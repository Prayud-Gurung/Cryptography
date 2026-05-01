# Output feedback mode(OFB)

1. Encrypts IV with AES and generate keystream
2. XOR keystream with block/message to create ciphertext
3. Feed keystream back to the AES encryption function and produce next keystream
4. Used the generated keystream to encrypt next block