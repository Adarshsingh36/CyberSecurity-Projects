## 🔐 Cipher Fundamentals (Beginner Friendly)

### 🔹 Caesar Cipher – Fundamentals

The **Caesar Cipher** is one of the oldest encryption techniques.  
It is a **monoalphabetic substitution cipher**, meaning each letter in the plaintext
is replaced by another letter at a fixed distance in the alphabet.

#### Encryption Formula
E(x) = (x + k) mod 26


#### Decryption Formula
D(x) = (x − k) mod 26


Where:
- `x` is the numerical value of a letter (A = 0, B = 1, ..., Z = 25)
- `k` is the shift key

#### Example

Plaintext : HELLO
Key : 3
Ciphertext : KHOOR


#### Security Characteristics
- Very weak encryption
- Only 26 possible keys
- Easily broken using brute-force or frequency analysis

---

### 🔹 Vigenère Cipher – Fundamentals

The **Vigenère Cipher** is a **polyalphabetic substitution cipher**.
Instead of using a single key, it uses a **keyword**, which makes it more secure
than the Caesar cipher.

Each character of the plaintext is encrypted using a different shift derived
from the keyword.

#### Encryption Formula
E(x) = (x + kᵢ) mod 26

#### Decryption Formula
D(x) = (x − kᵢ) mod 26


Where:
- `x` is the plaintext character value
- `kᵢ` is the numerical value of the corresponding key character

#### Example
Plaintext : HELLO
Key : KEY
Expanded : KEYKE
Ciphertext: RIJVS



#### Security Characteristics
- More secure than Caesar cipher
- Resistant to simple frequency analysis
- Security depends on key length and randomness
- Vulnerable if the key is short or reused

---

## 🎓 Educational Purpose

This project is built **for learning purposes only**.  
It helps beginners understand:
- How classical encryption works
- Why simple ciphers are insecure
- How brute-force attacks are performed
- How to structure a real Python project

---

# 🔐 Classical Cryptography Toolkit

A Python-based cryptography toolkit that implements **classical encryption algorithms** with both  
**Command-Line Interface (CLI)** and **Graphical User Interface (GUI)** support.

This project is designed for **beginners in cyber security** to understand how classical ciphers work,
why they are insecure today, and how attacks such as brute force are performed.

---

## ✨ Features

### 🟢 Caesar Cipher
- Encrypt text using a fixed shift key
- Decrypt encrypted text using the same key
- Brute-force attack simulation (all 26 possible keys)

### 🟢 Vigenère Cipher
- Encrypt text using a keyword
- Decrypt text using a keyword
- Supports both uppercase and lowercase letters

### 🖥️ User Interfaces
- Command Line Interface (CLI)
- Graphical User Interface (GUI) built using **Tkinter**

---

## 📁 Project Structure

classical-cryptography-toolkit/
│
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

## ▶️ How to Run the Project

### 🔹 Run the GUI
```bash
python ui.py

---

## ▶️ How to Run the Project

### 🔹 Run the GUI
```bash
python ui.py



## ⚠️ Disclaimer

This project is **not intended for real-world secure communication**.  
Modern cryptography uses advanced algorithms such as **AES** and **RSA**.

