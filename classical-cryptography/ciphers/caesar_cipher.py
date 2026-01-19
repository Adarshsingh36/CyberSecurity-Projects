def _shift_char(char, shift):
    if char.isalpha():
        base = ord('a') if char.islower() else ord('A')
        return chr((ord(char) - base + shift) % 26 + base)
    return char


def encrypt_caesar(text, key):
    result = ""
    key = key % 26
    for char in text:
        result += _shift_char(char, key)
    return result


def decrypt_caesar(text, key):
    result = ""
    key = key % 26
    for char in text:
        result += _shift_char(char, -key)
    return result


def brute_force(ciphertext):
    return {k: decrypt_caesar(ciphertext, k) for k in range(26)}
