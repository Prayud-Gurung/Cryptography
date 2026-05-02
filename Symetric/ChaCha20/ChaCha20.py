import hashlib
from Crypto.Cipher import ChaCha20
import base64

secret = "Apple"
key = hashlib.sha256(secret.encode()).digest()

def encrypt(plain_text, key):
    byte_data = plain_text.encode()
    cipherObj = ChaCha20.new(key = key)
    cipher_text = cipherObj.encrypt(byte_data)
    nonce = cipherObj.nonce
    encoded_String = base64.b64encode(cipher_text).decode()
    encoded_nonce = base64.b64encode(nonce).decode()
    return encoded_String, encoded_nonce

text = input("Enter Text: ")


def decrypt(encrypted_text, key, nonce):
    byte_text = base64.b64decode(encrypted_text)
    nonce_byte = base64.b64decode(nonce)
    cipher = ChaCha20.new(key=key, nonce=nonce_byte)
    decrypted_text = cipher.decrypt(byte_text)

    return decrypted_text.decode()

try:
    output = decrypt(text.encode(), key, "QINewJGVeZg=")
    print(output)
except:
    output = encrypt(text, key)
    print(output)