# 🔐 Ransomware Simulator (Safe & Educational)

This Python script simulates ransomware behavior by encrypting and decrypting files in a folder using symmetric encryption.

## ⚙️ How It Works
- Encrypts or decrypts files inside the `sample_docs/` folder.
- Saves the key used for encryption in `secret.key`.
- Designed for learning, not malicious use.

## 🛠 Requirements
- Python 3.6+
- Install dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage
1. Create a folder named `sample_docs` in the same directory.
2. Add test files (e.g., `.txt`, `.jpg`, etc.) inside it.
3. Run the script:
```bash
python3 ransomware_simulator.py
```
4. Choose:
    - `e` to encrypt
    - `d` to decrypt (requires `secret.key`)

## ⚠️ Disclaimer
This project is for educational purposes only. Do **not** use this code to harm others.

---
Made by Collins Ajekwe