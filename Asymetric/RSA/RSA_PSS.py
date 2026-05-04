from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
from Crypto.Signature import pss
import base64

#Signing
def sign():
    message = input("Enter message: ")
    private_key = RSA.generate(1024)
    public_key = private_key.public_key()
    message_hash= SHA256.new(message.encode())
    signature = pss.new(private_key).sign(message_hash)
    exported_public_key = public_key.export_key(format="DER")
    print("Public key: ", base64.b64encode(exported_public_key).decode())#DER in raw binary form
    print(message_hash.digest())
    print("Signature: ", base64.b64encode(signature).decode())#in raw binary form
    
def verify():
    print("Verify")
    message = input("Enter message: ")
    encoded_signature = input("Enter signature: ")
    signature = base64.b64decode(encoded_signature.encode())
    encoded_public_key = input("Enter public key: ")
    public_key = base64.b64decode(encoded_public_key.encode())
    
    message_hash = SHA256.new(message.encode())
    imported_public_key = RSA.import_key(public_key)#byte to byte object
    verifier = pss.new(imported_public_key)#byte object
    try:
        verifier.verify(message_hash, signature)
        print("Signature is authentic")
    except:
        print("Cannot verify")

while True:
    choice = input("s for signing and v for veryfing: ")
    match choice.lower():
        case "s":
            sign()
        case "v":
            verify()
        case _:
            print("Invalid choice")



