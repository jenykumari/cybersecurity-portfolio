import hashlib

file_name = input("Enter file name: ")

try:
    with open(file_name, "rb") as file:
        content = file.read()

    first_hash = hashlib.sha256(content).hexdigest()

    print("\n--- Initial Scan Complete ---")
    print("File Hash:", first_hash)

    input("\nPress Enter to verify the file again...")

    with open(file_name, "rb") as file:
        content = file.read()

    second_hash = hashlib.sha256(content).hexdigest()

    print("\n--- Verification Result ---")

    if first_hash == second_hash:
        print("Status: SAFE")
        print("File has not been modified.")
    else:
        print("Status: ALERT")
        print("File integrity check failed.")

except FileNotFoundError:
    print("File not found.")
