from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

plain_message = input("Enter message to encrypt: ")

private_key = RSA.generate(1024) #2048 minimum, 3072, 4096, for demo 1024 for faster encryption
public_key = private_key.public_key()

#Encryption using public key
cipherObj = PKCS1_OAEP.new(public_key)
cipher_text = cipherObj.encrypt(plain_message.encode())
encrypted_text = base64.b64encode(cipher_text).decode()
print("Encrypted Text: ", encrypted_text)
# Export public key for sharing
# exported_public_key = public_key.export_key(format="PEM")
# print(exported_public_key.decode())

#For this demo export private key, to test in CLI
# exported_private_key = private_key.export_key(format="PEM")#byte object
exported_private_key = private_key.export_key(format="PEM")
with open("/Users/prayudgurung/Desktop/CyberSecurity/Cryptography/Asymetric/RSA/pk.PEM", "wb") as file:
    file.write(exported_private_key)

#Decryption using private key
print("Decryption")
encrypted_message = input("Enter the encrypted message: ")
try:
    decoded_message = base64.b64decode(encrypted_message.encode())

    with open("/Users/prayudgurung/Desktop/CyberSecurity/Cryptography/Asymetric/RSA/pk.PEM", "rb") as file:
        imported_private_key = file.read()
    
    loaded_private_key = RSA.import_key(imported_private_key)
    cipher = PKCS1_OAEP.new(loaded_private_key)

    decrypted_message = cipher.decrypt(decoded_message)
    print(decrypted_message.decode())
except Exception as e:
    print("Error:", e)
