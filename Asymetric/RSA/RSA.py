from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_PSS
from Crypto.Hash import SHA256
import base64

private_key = RSA.generate(1024)
public_key = private_key.public_key()

def encryption():
    message = input("Enter message: ")
    encryption_obj = PKCS1_OAEP.new(public_key)
    cipher_text = encryption_obj.encrypt(message.encode())
    encrypted_message = base64.b64encode(cipher_text)

    exported_public_key = public_key.export_key(format = "PEM")#Usually DER for signature

    exported_private_key = private_key.export_key(format = "PEM")
    print("Encrypted message: ", encrypted_message.decode())
    print("\nPrivate key: ", base64.b64encode(exported_private_key).decode())

    message_hash = SHA256.new(cipher_text)
    signing_obj = PKCS1_PSS.new(private_key)
    signature = signing_obj.sign(message_hash)
    encoded_signature = base64.b64encode(signature).decode()
    print("\nSignature")
    print("Public key: ", base64.b64encode(exported_public_key).decode())
    print("\nSignature: ", encoded_signature)

def decryption():
    encrypted_message = input("Enter encrypted message:")
    exported_private_key = input("Enter private key: ")
    decoded_message = base64.b64decode(encrypted_message.encode())
    decoded_private_key = base64.b64decode(exported_private_key.encode())

    exported_public_key = input("Enter public key: ")
    encoded_signature = input("Enter digital signature: ")
    decoded_public_key = base64.b64decode(exported_public_key.encode())
    signature = base64.b64decode(encoded_signature.encode())

    message_hash = SHA256.new(decoded_message)
    imported_public_key = RSA.import_key(decoded_public_key)
    verifier = PKCS1_PSS.new(imported_public_key)

    if verifier.verify(message_hash, signature):
        print("verified")
    else:
        print("Cannot verify")
        return

    imported_private_key = RSA.import_key(decoded_private_key)
    encryption_obj = PKCS1_OAEP.new(imported_private_key)
    decrypted_message = encryption_obj.decrypt(decoded_message)
    print("Message: ", decrypted_message.decode())

encryption()
decryption()


# LS0tLS1CRUdJTiBQVUJMSUMgS0VZLS0tLS0KTUlHZk1BMEdDU3FHU0liM0RRRUJBUVVBQTRHTkFEQ0JpUUtCZ1FDYzAyYWMvVWtmZzkvdk5YbjJodnBvb2lQNQpHNy9FSVhGekVJVjhDWnp0cU9vWDFWMmhPVHM4UFREckloVFgyM3I5WVN5SW1tVkwzaDZwVEZtY3liZW5ZS1lzCm8wQ2dNbStocFFDU0VJcmNBdjU5SFdaZUNYNDhXZXAzc3ZyU2F1VG1MRGt1WjN4bWtrbm5jc0h5Y1R2SSsxU0YKRHIvcUMzYW9RYnR6ZDlLRmR3SURBUUFCCi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLQ==