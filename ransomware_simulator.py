import os
from cryptography.fernet import Fernet

# === CONFIGURATION ===
TARGET_DIR = "sample_docs"  # folder containing files to encrypt/decrypt
KEY_FILE = "secret.key"


# === FUNCTION: Generate and store key ===
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved.")
    return key


# === FUNCTION: Load existing key ===
def load_key():
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


# === FUNCTION: Encrypt files ===
def encrypt_files(key):
    fernet = Fernet(key)
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            with open(path, "rb") as original:
                data = original.read()
            encrypted = fernet.encrypt(data)
            with open(path, "wb") as encrypted_file:
                encrypted_file.write(encrypted)
            print(f"[+] Encrypted: {path}")


# === FUNCTION: Decrypt files ===
def decrypt_files(key):
    fernet = Fernet(key)
    for root, _, files in os.walk(TARGET_DIR):
        for file in files:
            path = os.path.join(root, file)
            with open(path, "rb") as encrypted:
                data = encrypted.read()
            decrypted = fernet.decrypt(data)
            with open(path, "wb") as decrypted_file:
                decrypted_file.write(decrypted)
            print(f"[+] Decrypted: {path}")


# === MAIN ===
if __name__ == "__main__":
    action = input("[?] Encrypt or Decrypt? (e/d): ").lower()

    if action == "e":
        key = generate_key()
        encrypt_files(key)
    elif action == "d":
        if not os.path.exists(KEY_FILE):
            print("[!] Key file not found. Cannot decrypt.")
        else:
            key = load_key()
            decrypt_files(key)
    else:
        print("[!] Invalid option. Use 'e' to encrypt or 'd' to decrypt.")