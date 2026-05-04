from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_PSS
import base64

private_key = RSA.generate(1024)
public_key = private_key.public_key()

def encryption():
    message = input("Enter message: ")
    exported_private_key = private_key.export_key(format="PEM")

    encryption_obj = PKCS1_OAEP.new(public_key)
    encrypted_text = encryption_obj.encrypt(message.encode())

    print(base64.b64encode(encrypted_text).decode())
    print("Private key: ", base64.b64encode(exported_private_key).decode())

    message_hash = SHA256.new(message.encode())
    signature_obj = PKCS1_PSS.new(private_key)
    signature = signature_obj.sign(message_hash)
    exported_public_key = public_key.export_key(format="PEM")
    print("\nSignature")
    print("\nPublic key: ", base64.b64encode(exported_public_key).decode())
    print("\nSignature: ", base64.b64encode(signature).decode())

def decryption():
    message = input("Enter encrypted message: ")
    exported_private_key = input("Enter private key: ")
    imported_private_key = RSA.import_key(base64.b64decode(exported_private_key.encode()))
    decryption_obj = PKCS1_OAEP.new(imported_private_key)
    decrypted_message = decryption_obj.decrypt(base64.b64decode(message.encode()))
    print("Decrypted message: ", decrypted_message.decode())

    encoded_signature = input("Enter digital signature: ")
    exported_public_key = input("Enter public key: ")
    imported_public_key = RSA.import_key(base64.b64decode(exported_public_key.encode()))
    verifier = PKCS1_PSS.new(imported_public_key)
    message_hash = SHA256.new(decrypted_message)
    signature = base64.b64decode(encoded_signature.encode())
    if verifier.verify(message_hash, signature):
        print("Verified")
    else:
        print("Not verifies")
        return
    

encryption()
decryption()

