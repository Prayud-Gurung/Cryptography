import hashlib
from Crypto.Cipher import AES
import base64

secret= "Apple"
key = hashlib.sha256(secret.encode()).digest()

def encrypt(plain_text, key):
    cipherObj = AES.new(key, AES.MODE_CTR)
    cipher_text = cipherObj.encrypt(plain_text.encode()) #b'Apple' ---------> b'\x15=E7\xad'
    nonce = cipherObj.nonce
    encoded = base64.b64encode(cipher_text).decode()#b'FT1FN60=' -------------> FT1FN60=
    return encoded, nonce

def decrypt(encrypted_text, key, nonce):
    byte_text = base64.b64decode(encrypted_text.encode())#FT1FN60= ---------------> b'FT1FN60='
    cipherObj = AES.new(key, AES.MODE_CTR, nonce = nonce)
    decrypted_text = cipherObj.decrypt(byte_text)#b'FT1FN60=' --------------> b'Apple
    return decrypted_text.decode()#b'Apple --------------> Apple

text = input("Enter text: ")

try:
    output = decrypt(text, key, b'\xaf\xb2\x8c\xc1+I\xa3\xa8')
    print("Deocded: ", output)
except:
    output, nonce = encrypt(text, key)
    print(f"Type: {type(output)}, Output: {output}") #FT1FN60=
    print(f"Type: {type(nonce)}, Output: {nonce}") #b'\xaf\xb2\x8c\xc1+I\xa3\xa8'