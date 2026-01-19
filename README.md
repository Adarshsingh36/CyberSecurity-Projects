# Classical Cryptography Toolkit 🔐

A Python-based cryptography toolkit that implements classical encryption algorithms with both **command-line** and **GUI** support.  
This project is built with a clean modular design and demonstrates core cyber security concepts.

---

# Features

# Caesar Cipher
- Encrypt text using a fixed shift key
- Decrypt encrypted text using the same key
- Brute-force attack simulation (all 26 possible keys)

# Vigenère Cipher
- Encrypt text using a keyword
- Decrypt text using a keyword
- Supports both uppercase and lowercase characters

# User Interfaces
- Command Line Interface (CLI)
- Graphical User Interface (GUI) using **Tkinter**

---

# Project Structure
├── cipher_toolkit/
│ ├── init.py
│ ├── caesar.py
│ └── vigenere.py
│
├── main.py # CLI version
├── ui.py # GUI version
├── README.md
└── .gitignore



---

How to Run the Project

## Run the GUI
```bash
python ui.py

#OR

python main.py


## 🔐 Cipher Fundamentals

### 🔹 Caesar Cipher – Fundamentals

The **Caesar Cipher** is a **monoalphabetic substitution cipher** in which each letter of the plaintext is shifted by a fixed number of positions in the alphabet.

**Encryption Formula:**
E(x) = (x + k) mod 26

**Decryption Formula:**
D(x) = (x − k) mod 26


Where:
- `x` represents the numerical value of a letter (A = 0, B = 1, …, Z = 25)
- `k` is the shift key

**Example:**
Plaintext : HELLO
Key : 3
Ciphertext : KHOOR


**Security Characteristics:**
- Very weak encryption
- Only 26 possible keys
- Easily broken using brute-force or frequency analysis

---

### 🔹 Vigenère Cipher – Fundamentals

The **Vigenère Cipher** is a **polyalphabetic substitution cipher** that uses a repeating keyword to apply different shifts to each character of the plaintext.

**Encryption Formula:**
E(x) = (x + kᵢ) mod 26

**Decryption Formula:**
D(x) = (x − kᵢ) mod 26

Where:
- `x` is the numerical value of the plaintext character
- `kᵢ` is the numerical value of the corresponding key character

**Example:**
Plaintext : HELLO
Key : KEY
Expanded : KEYKE
Ciphertext: RIJVS


**Security Characteristics:**
- More secure than Caesar cipher
- Resistant to simple frequency analysis
- Security depends on key length and randomness
- Vulnerable if the key is short or reused

---
