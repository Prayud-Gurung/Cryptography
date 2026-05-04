from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import os

# Get directory for output files
output_dir = os.path.dirname(os.path.abspath(__file__))

print("=== RSA OAEP Encryption/Decryption ===\n")

# ENCRYPTION
print("--- ENCRYPTION ---")
plain_message = input("Enter message to encrypt: ")

private_key = RSA.generate(1024)
public_key = private_key.public_key()

# Encryption using public key
cipherObj = PKCS1_OAEP.new(public_key)
cipher_text = cipherObj.encrypt(plain_message.encode())
encrypted_text = base64.b64encode(cipher_text).decode()

# Export private key
exported_private_key = base64.b64encode(private_key.export_key(format="PEM")).decode()

# Save to files
with open(os.path.join(output_dir, "encrypted_message.txt"), "w") as f:
    f.write(encrypted_text)
    
with open(os.path.join(output_dir, "private_key.txt"), "w") as f:
    f.write(exported_private_key)

print(f"✓ Encrypted Text saved to: encrypted_message.txt")
print(f"✓ Private Key saved to: private_key.txt")
print(f"\nEncrypted message (first 50 chars): {encrypted_text[:50]}...")
print(f"Private key (first 50 chars): {exported_private_key[:50]}...\n")

# DECRYPTION
print("--- DECRYPTION ---")
try:
    # Read from files
    with open(os.path.join(output_dir, "encrypted_message.txt"), "r") as f:
        encrypted_message = f.read()
    
    with open(os.path.join(output_dir, "private_key.txt"), "r") as f:
        encrypted_private_key = f.read()
    
    # Decode and decrypt
    decoded_message = base64.b64decode(encrypted_message.encode())
    decoded_private_key = base64.b64decode(encrypted_private_key.encode())

    loaded_private_key = RSA.import_key(decoded_private_key)
    cipher = PKCS1_OAEP.new(loaded_private_key)
    decrypted_message = cipher.decrypt(decoded_message)
    
    print(f"✓ Decrypted Message: {decrypted_message.decode()}")
    print(f"\n✓ Encryption/Decryption successful!")
    
except Exception as e:
    print(f"✗ Error: {e}")
