import hashlib
from Crypto.Cipher import AES
import base64

secret = "apple"
key = hashlib.sha256(secret.encode()).digest()

def encrypt(plain_text, key):
    text_b64 = plain_text.encode()
    cipherObj = AES.new(key, AES.MODE_OFB)
    cipher_text = cipherObj.encrypt(text_b64)
    iv = base64.b64encode(cipherObj.iv).decode()
    encrypted_text = base64.b64encode(cipher_text).decode()

    encrypted_data = encrypted_text + ":" + iv
    return encrypted_data

def decrypt(encrypted_data, key):
    encrypted_text, encrypted_iv = encrypted_data.split(":")

    encrypted_b64 = base64.b64decode(encrypted_text.encode())
    iv_b64 = base64.b64decode(encrypted_iv.encode())

    cipherObj = AES.new(key, AES.MODE_OFB, iv=iv_b64)
    decrypted_text = cipherObj.decrypt(encrypted_b64)
    return decrypted_text.decode()

text = input("Enter Text: ")

try:
    output = decrypt(text, key)
    print(output)
except:
    output = encrypt(text, key)
    print(output)