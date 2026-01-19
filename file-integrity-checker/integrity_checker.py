import hashlib
import os
import json

BASELINE_FILE = "baseline.json"

MONITOR_DIR = "test_files"

def calculate_hash(file_path):
  
    sha256 = hashlib.sha256()  # Create a SHA-256 hash object

    try:
        # Open the file in binary mode using the key word "rb" insted of w or r
        with open(file_path, "rb") as f:
    
            for block in iter(lambda: f.read(4096), b""):# Read the file in 4096-byte chunks in order to tacle the problem of large files
                sha256.update(block)
        return sha256.hexdigest()

    except FileNotFoundError:
        return None

def create_baseline():
    
    hashes = {} 
    for root, _, files in os.walk(MONITOR_DIR):# Traverse the monitored directory
        for file in files:
            # Construct full file path
            file_path = os.path.join(root, file)

            # Calculate and store hash for each file
            hashes[file_path] = calculate_hash(file_path)

    # Save the baseline hashes into a JSON file
    with open(BASELINE_FILE, "w") as f:
        json.dump(hashes, f, indent=4)

    print("[+] Baseline created successfully.")


def check_integrity():

    # Ensure baseline exists before checking integrity
    if not os.path.exists(BASELINE_FILE):
        print("[-] Baseline not found. Run baseline creation first.")
        return

    # Load the previously saved baseline hashes
    with open(BASELINE_FILE, "r") as f:
        old_hashes = json.load(f)

    current_hashes = {}  # Store current state hashes

    # Recalculate hashes for current files
    for root, _, files in os.walk(MONITOR_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            current_hashes[file_path] = calculate_hash(file_path)

    # Check for deleted or modified files
    for file, old_hash in old_hashes.items():
        if file not in current_hashes:
            print(f"[!] FILE DELETED: {file}")
        elif current_hashes[file] != old_hash:
            print(f"[!] FILE MODIFIED: {file}")

    # Check for newly added files
    for file in current_hashes:
        if file not in old_hashes:
            print(f"[!] NEW FILE ADDED: {file}")

    print("[+] Integrity check completed.")


def main():
    print("Integrity Checker")

    print("1. Create Baseline")
    print("2. Check Integrity")

    # Take user input to decide operation
    choice = input("Choose option (1/2): ")

    if choice == "1":
        create_baseline()
    elif choice == "2":
        check_integrity()
    else:
        print("Invalid option")


# This ensures the program runs only when executed directly
# and not when imported as a module
if __name__ == "__main__":
    main()
