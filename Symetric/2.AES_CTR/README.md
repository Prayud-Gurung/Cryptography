# Counter mode (CTR)
1. Counts the block and uses keystream for AES encryption
2. Key stream is generated from counter value and nonce
3. Encrypts by XORing block with keystream
4. Increases the counter and repeat the operation