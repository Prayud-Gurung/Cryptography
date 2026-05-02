#AES CTR MODE
import hashlib
from Crypto.Cipher import AES
import base64

secret = "Appel"
key = hashlib.sha256(secret.encode()).digest()

def encrypt(plain_text, key):
    byte_text = plain_text.encode()
    cipherObj = AES.new(key, AES.MODE_CTR)
    cipher_text = cipherObj.encrypt(byte_text)
    encrypted_string = base64.b64encode(cipher_text).decode()
    nonce = base64.b64encode(cipherObj.nonce).decode()

    encrypted_data = encrypted_string + ":" + nonce
    return encrypted_data

def decrypt(encrypted_data, key):
    encrypted_text, encrypted_nonce = encrypted_data.split(":")
    text_b64 = base64.b64decode(encrypted_text.encode())
    nonce_b64 = base64.b64decode(encrypted_nonce)

    cipherObj = AES.new(key, AES.MODE_CTR, nonce=nonce_b64)
    decrypted_text = cipherObj.decrypt(text_b64)
    return decrypted_text.decode()

text = input("Enter text: ")

try:
    output = decrypt(text, key)
    print(output)
except:
    output = encrypt(text, key)
    print(output)
