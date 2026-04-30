import hashlib
from Crypto.Cipher import AES
import base64
password = "Apple"
key = hashlib.sha256(password.encode()).digest()

def padding(text):
    textLength = 16 - (len(text) % 16)
    return (text + chr(textLength) * textLength)

def encrypt(plain_text, key):
    cipherObj = AES.new(key, AES.MODE_ECB)
    cipherText = cipherObj.encrypt(padding(plain_text).encode())
    return base64.b64encode(cipherText).decode()

def decrypt(encrypted_text, key):
    cipherObj = AES.new(key, AES.MODE_ECB)
    

text = input("Enter text: ")
output = encrypt(text, key)
print("Output: ", output)

