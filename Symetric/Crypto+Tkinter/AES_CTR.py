import tkinter as tk
import tkinter.filedialog
import hashlib
from Crypto.Cipher import AES
import base64

root = tk.Tk(className="Crypto")
root.geometry("1000x500")
label = tk.Label(root, text="Cryptography")
label.pack()

msg_label = tk.Label(root, text="Message")
msg_label.pack()
msg_input = tk.Entry(root, background="#5f5f5f")
msg_input.pack()

pw_label = tk.Label(root, text="Password")
pw_label.pack()
pw_input = tk.Entry(root, background="#5f5f5f")
pw_input.pack()

encrypted_data = ""

def encrypt():
    global encrypted_data
    msg  = msg_input.get()
    pw = pw_input.get()
    key = hashlib.sha256(pw.encode()).digest()

    cipherObj = AES.new(key, AES.MODE_CTR)
    cipher_text = cipherObj.encrypt(msg.encode())
    nonce = base64.b64encode(cipherObj.nonce).decode()
    encrypted_text = base64.b64encode(cipher_text).decode()
    encrypted_data = nonce + ":" + encrypted_text
    print(encrypted_data)

    msg_input.delete(0, tk.END)
    msg_input.insert(0, encrypted_data)

def decrypt():
    msg  = msg_input.get()
    pw = pw_input.get()
    key = hashlib.sha256(pw.encode()).digest()

    nonce_b64, cipher_b64 = msg.split(":")
    cipher_text = base64.b64decode(cipher_b64.encode())
    nonce = base64.b64decode(nonce_b64.encode())

    cipherObj = AES.new(key, AES.MODE_CTR, nonce = nonce)
    byte_text = cipherObj.decrypt(cipher_text)
    result = byte_text.decode()

    msg_input.delete(0, tk.END)
    msg_input.insert(0, result)

def save_file():
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".txt")

    if file_path and encrypted_data:
        with open(file_path, "w") as file:
            file.write(encrypted_data)

encrypt_btn = tk.Button(root, text="Encrypt", command=encrypt)
decrypt_btn = tk.Button(root, text="Decrypt", command=decrypt)
save_btn = tk.Button(root, text="Save", command=save_file)
save_btn.pack()
encrypt_btn.pack()
decrypt_btn.pack()

root.mainloop()