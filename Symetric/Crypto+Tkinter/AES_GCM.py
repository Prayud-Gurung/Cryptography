import tkinter as tk
import tkinter.filedialog
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256
import base64

root = tk.Tk()
root.title("AES-GCM")
root.geometry("1000x500")
content = b''
encrypted_data = b''

def encrypt(data):
    global encrypted_data
    byte_header = user.get().encode()
    secret = password.get()
    byte_salt = get_random_bytes(16)
    key = PBKDF2(secret.encode(), byte_salt, 32, 100000, hmac_hash_module=SHA256)

    cipherObj = AES.new(key, AES.MODE_GCM)
    cipherObj.update(byte_header)
    cipher_file, b64_tag = cipherObj.encrypt_and_digest(data)
    b64_nonce = cipherObj.nonce

    salt = base64.b64encode(byte_salt).decode()
    header = base64.b64encode(byte_header).decode()
    nonce = base64.b64encode(b64_nonce).decode()
    tag = base64.b64encode(b64_tag).decode()
    token = salt + "|" + header + "|" + nonce + "|" + tag
    encrypted_data = cipher_file
    print(encrypted_data)
    print("Token: ",token)
    tkinter.messagebox.showinfo(title="Encrypted", message=f"Save this token for decryption \n {token}")

def Decrypt(content):
    tkn = token.get()
    secret = password.get()
    salt, header, nonce, tag = tkn.split("|")
    b64_salt = base64.b64decode(salt.encode())
    b64_header = base64.b64decode(header.encode())
    b64_nonce = base64.b64decode(nonce.encode())
    b64_tag = base64.b64decode(tag.encode())
    try:
        key = PBKDF2(secret, b64_salt, 32, 100000, hmac_hash_module=SHA256)
        cipherObj = AES.new(key, AES.MODE_GCM, nonce=b64_nonce)
        cipherObj.update(b64_header)
        decrypted_text = cipherObj.decrypt_and_verify(content, b64_tag)
        print(decrypted_text)
        return decrypted_text#/decode()
    except:
        print("Error decoding")

    pass
def Open():
    global content
    file_path = tkinter.filedialog.askopenfilename()
    with open(file_path, "rb") as file:
        content = file.read()

def save():
    if not encrypted_data:
        return
    else:
        file_path = tkinter.filedialog.asksaveasfilename()
        with open(file_path, "wb") as file:
            file.write(encrypted_data)

label = tk.Label(root, text="Encnryption AES-GCM")
button = tk.Button(root, text = "Open file", command = Open)
label_user = tk.Label(root, text = "Username")
user = tk.Entry(root, background="#5f5f5f")
label_password = tk.Label(root, text = "Password")
password = tk.Entry(root, background="#5f5f5f")
btn_encrypt = tk.Button(root, text = "Encrypt", command = lambda: encrypt(content))
label_token = tk.Label(root, text = "Token: ")
token = tk.Entry(root, background="#5f5f5f")
btn_decrypt = tk.Button(root, text = "Decrypt", command = lambda: Decrypt(content))

btn_save = tk.Button(root, text = "Save file", command = save)

label.pack()
button.pack()
label_user.pack()
user.pack()
label_password.pack()
password.pack()
btn_encrypt.pack()
btn_save.pack()
label_token.pack()
token.pack()
btn_decrypt.pack()

root.mainloop()