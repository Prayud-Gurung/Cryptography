import hashlib
from Crypto.Cipher import AES
import base64

password = "Apple"
key = hashlib.sha256(password.encode()).digest()

def padding(text):
    textLength = 16 - (len(text) % 16)
    return (text + chr(textLength) * textLength)

def remove_padding(text):
    lastvalue = text[len(text)-1]
    padding_length = ord(lastvalue)
    return text[0: -padding_length]

def encrypt(plain_text, key):
    cipherObj = AES.new(key, AES.MODE_ECB)
    cipher_text = cipherObj.encrypt(padding(plain_text).encode())
    return base64.b64encode(cipher_text).decode()

def decrypt(encrypted_text, key):
    cipher_bytes = base64.b64decode((encrypted_text).encode())
    cipherObj = AES.new(key, AES.MODE_ECB)
    decrypted_text = cipherObj.decrypt(cipher_bytes).decode()

    return remove_padding(decrypted_text)


text = input("Enter text: ")

try:
    decrypedText = decrypt(text, key)
    print(decrypedText)
except Exception:
    output = encrypt(text, key)
    print(output)
'''print("Type: ", type(output))
print("Output: ", output)'''

