import hashlib
from Crypto.Cipher import AES
import base64
secret = "apple"
key = hashlib.sha256(secret.encode()).digest()

def encrypt(plain_text, key):
    text_b64 = plain_text.encode()
    cipherObj = AES.new(key, AES.MODE_CFB)
    cipher_text = cipherObj.encrypt(text_b64)
    iv = base64.b64encode(cipherObj.iv).decode()
    encrypted_text = base64.b64encode(cipher_text).decode()

    return encrypted_text, iv

def decrypt(encrypted_text, key, iv):
    encrypted_b64 = base64.b64decode(encrypted_text.encode())
    iv_b64 = base64.b64decode(iv.encode())
    cipherObj = AES.new(key, AES.MODE_CFB, iv=iv_b64)
    decrypted_text = cipherObj.decrypt(encrypted_b64)

    return decrypted_text.decode()
    

text = input("Enter text")
try:
    output = decrypt(text, key, "fp0YMrFaG7qbpxmhgNBPKQ==")
    print(output)
except:
    output, iv = encrypt(text, key) #x/0TRzk=
    print("Output: ", output)
    print("IV: ", iv)