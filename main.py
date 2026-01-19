from cipher_toolkit import (
    encrypt_caesar,
    decrypt_caesar,
    brute_force,
    encrypt_vigenere,
    decrypt_vigenere
)

print(encrypt_caesar("Hello", 3))
print(decrypt_caesar("Khoor", 3))

print(encrypt_vigenere("Hello World", "KEY"))
print(decrypt_vigenere("Rijvs Uyvjn", "KEY"))
