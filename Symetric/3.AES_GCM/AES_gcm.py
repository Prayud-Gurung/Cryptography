from Crypto.Cipher import AES
import base64
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256

secret = "Apple"
# key = hashlib.sha256(secret.encode()).digest()

salt = get_random_bytes(16)
key = PBKDF2(secret, salt, 32, 1000000, hmac_hash_module=SHA256)#PBKDF2 standard and secure way to generate key

header = b'header'

def encrypt(plain_text, key):
    byte_text = plain_text.encode()

    cipherObj = AES.new(key, AES.MODE_GCM)
    cipherObj.update(header)
    cipher_text, tag = cipherObj.encrypt_and_digest(byte_text)
    nonce = cipherObj.nonce
    
    return {
        "encrypted_text": base64.b64encode(cipher_text).decode(),
        "tag": base64.b64encode(tag).decode(),
        "header": base64.b64encode(header).decode(),
        "nonce": base64.b64encode(nonce).decode()
    }

def decrypt(encrypted_text, key, nonce, header, tag):
    try:
        cipherObj = AES.new(key, AES.MODE_GCM, base64.b64decode(nonce))
        cipherObj.update(base64.b64decode(header))
        decrypted_text = cipherObj.decrypt_and_verify(base64.b64decode(encrypted_text), base64.b64decode(tag))
        return decrypted_text.decode()
    except Exception as error:
        return f"Decryption failed: {str(error)}"

# output = encrypt(text, key)
# print(f"Encrypted text: {output[0]} \n tag: {output[1]} \n header: {output[2]} \n nonce: {output[3]}")
# print(output)

# (encrypted, tag, header, nonce) = ('V4bIUSY=', 'a3mkYMdrjBI9BXiE0fbGFA==', 'aGVhZGVy', 'Qlx3JJYI/cYD+0FY6HaJeA==')
# output = decrypt(encrypted, key, nonce, header, tag)
# print(output)


while True:
    choice = input("Enter e for encryption and d for decryption: ")
    match choice:
        case "e":
            print("Encryption\n")
            text = input("Enter text: ")
            output = encrypt(text, key)
            print(f"\nencrypted text: {output["encrypted_text"]} \ntag: {output["tag"]} \nheader: {output["header"]} \nnonce: {output["nonce"]}")
        case "d":
            print("Decryption\n")
            encrypted = input("Enter encrypted text: ")
            tag = input("Enter authenticaiton tag: ")
            header = input("Enter authentication header: ")
            nonce = input("Enter nonce value: ")
            output = decrypt(encrypted, key, nonce, header, tag)
            print(output)
        case _:
            print("Not valid choice")