from Crypto.PublicKey import ECC
from Crypto.Hash import SHA256
from Crypto.Protocol.KDF import HKDF
from Crypto.Cipher import AES

sender_key = ECC.generate(curve = "P-256")
sender_public_key = sender_key.public_key()
receiver_key = ECC.generate(curve = "P-256")
receiver_public_key = receiver_key.public_key()

sender_secret = sender_key.d * receiver_public_key.pointQ

receiver_secret = receiver_key.d * sender_public_key.pointQ

assert sender_secret == receiver_secret

sender_symetric_key = HKDF(master = sender_secret.x.to_bytes(), key_len=32, salt=b'', hashmod=SHA256)

receiver_symetric_key = HKDF(master = receiver_secret.x.to_bytes(), key_len=32, salt=b'', hashmod=SHA256)

assert sender_symetric_key == receiver_symetric_key

#Send
message = b"Hello Receiver! This is secret data."

cipher = AES.new(sender_symetric_key, AES.MODE_GCM)
ciphertext, tag = cipher.encrypt_and_digest(message)

nonce = cipher.nonce  # must be sent to receiver

print("\n--- SENDER SIDE ---")
print("Ciphertext:", ciphertext)
print("Nonce:", nonce)
print("Tag:", tag)

#Receive
cipher_dec = AES.new(receiver_symetric_key, AES.MODE_GCM, nonce=nonce)
plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)

print("\n--- RECEIVER SIDE ---")
print("Decrypted message:", plaintext.decode())