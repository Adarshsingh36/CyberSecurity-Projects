import tkinter as tk
from tkinter import ttk, messagebox

from cipher_toolkit import (
    encrypt_caesar,
    decrypt_caesar,
    brute_force,
    encrypt_vigenere,
    decrypt_vigenere
)

# Functions /conditons to handle UI logic

def update_ui(*args):
    cipher = cipher_choice.get()
    action = action_choice.get()

    if cipher == "Vigenere":
        action_box["values"] = ["Encrypt", "Decrypt"]
        if action == "Brute Force":
            action_choice.set("Encrypt")
        key_entry.config(state="normal")

    else:  
        action_box["values"] = ["Encrypt", "Decrypt", "Brute Force"]
        if action == "Brute Force":
            key_entry.delete(0, tk.END)
            key_entry.config(state="disabled")
        else:
            key_entry.config(state="normal")


def run_cipher():
    text = text_input.get("1.0", tk.END).strip()
    cipher = cipher_choice.get()
    action = action_choice.get()
    key = key_entry.get()

    try:
        if cipher == "Caesar":
            if action == "Brute Force":
                result = "\n".join(
                    f"{k}: {v}" for k, v in brute_force(text).items()
                )
            else:
                key = int(key)
                if action == "Encrypt":
                    result = encrypt_caesar(text, key)
                else:
                    result = decrypt_caesar(text, key)

        else:  # Vigenere
            if not key:
                messagebox.showerror("Error", "Key is required for Vigenère cipher")
                return

            if action == "Encrypt":
                result = encrypt_vigenere(text, key)
            else:
                result = decrypt_vigenere(text, key)

        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, result)

    except ValueError:
        messagebox.showerror("Error", "Key must be an integer for Caesar cipher")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- UI ----------

root = tk.Tk()
root.title("Classical Cryptography Toolkit")
root.geometry("600x520")

cipher_choice = tk.StringVar(value="Caesar")
action_choice = tk.StringVar(value="Encrypt")

cipher_choice.trace_add("write", update_ui)
action_choice.trace_add("write", update_ui)

# Cipher selection
ttk.Label(root, text="Cipher").pack()
cipher_box = ttk.Combobox(
    root,
    textvariable=cipher_choice,
    values=["Caesar", "Vigenere"],
    state="readonly"
)
cipher_box.pack()

# Action selection
ttk.Label(root, text="Action").pack()
action_box = ttk.Combobox(
    root,
    textvariable=action_choice,
    values=["Encrypt", "Decrypt", "Brute Force"],
    state="readonly"
)
action_box.pack()

# Key input
ttk.Label(root, text="Key").pack()
key_entry = ttk.Entry(root)
key_entry.pack(fill="x", padx=20)

# Input text
ttk.Label(root, text="Input Text").pack()
text_input = tk.Text(root, height=6)
text_input.pack(fill="both", padx=20)

# Run button
ttk.Button(root, text="Run", command=run_cipher).pack(pady=10)

# Output
ttk.Label(root, text="Output").pack()
output_box = tk.Text(root, height=8)
output_box.pack(fill="both", padx=20)

update_ui()
root.mainloop()
