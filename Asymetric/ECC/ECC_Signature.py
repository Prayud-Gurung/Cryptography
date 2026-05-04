from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Signature import DSS
import base64


def sign():
    private_key = ECC.generate(curve="P-256")
    public_key = private_key.public_key()
    exported_public_key = public_key.export_key(format="DER")
    message = input("Enter message")

    message_hash = SHA256.new(message.encode())

    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(message_hash)
    print("\nSign")
    print("Signature: ", base64.b64encode(signature).decode())
    print("Public key: ", base64.b64encode(exported_public_key).decode())

def verify():
    print("\n Verify")
    message = input("Enter Message: ")
    encoded_signature = input("Enter signature: ")
    encoded_public_key = input("Enter public key: ")
    
    message_hash = SHA256.new(message.encode())
    signature = base64.b64decode(encoded_signature.encode())
    public_key = ECC.import_key(base64.b64decode(encoded_public_key.encode()))

    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(message_hash, signature)
        print("Signature is valid!")
    except ValueError:
        print("Signature is invalid!")
        
sign()
verify()