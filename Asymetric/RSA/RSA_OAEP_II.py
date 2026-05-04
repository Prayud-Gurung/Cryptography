from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
import json

plain_message = input("Enter message to encrypt: ")

private_key = RSA.generate(1024) #2048 minimum, 3072, 4096, for demo 1024 for faster encryption
public_key = private_key.public_key()

#Encryption using public key
cipherObj = PKCS1_OAEP.new(public_key)
cipher_text = cipherObj.encrypt(plain_message.encode())
encrypted_text = base64.b64encode(cipher_text).decode()
print("\nEncrypted Text: ", encrypted_text)
# Export public key for sharing
# exported_public_key = public_key.export_key(format="PEM")
# print(exported_public_key.decode())

#For this demo export private key, to test in CLI
# exported_private_key = private_key.export_key(format="PEM")#byte object
exported_private_key = private_key.export_key(format="PEM").decode()
key = {"private_key" : exported_private_key}
with open("/Users/prayudgurung/Desktop/CyberSecurity/Cryptography/Asymetric/RSA/key.json", "w") as file:
    json.dump(key, file)
print(key)

#Decryption using private key
print("Decryption")
encrypted_message = input("\nEnter the encrypted message: ")
try:
    decoded_message = base64.b64decode(encrypted_message.encode())
    with open("/Users/prayudgurung/Desktop/CyberSecurity/Cryptography/Asymetric/RSA/key.json", "r") as file:
        imported_private_key = json.load(file)
    
    loaded_private_key = RSA.import_key(imported_private_key["private_key"])
    cipher = PKCS1_OAEP.new(loaded_private_key)

    decrypted_message = cipher.decrypt(decoded_message)
    print("\n Decrypted text: ", decrypted_message.decode())
except Exception as e:
    print("Error:", e)
