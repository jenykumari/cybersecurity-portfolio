import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

length = int(input("Enter password length: "))

use_numbers = input("Include numbers? (yes/no): ")
use_symbols = input("Include special characters? (yes/no): ")

characters = letters

if use_numbers.lower() == "yes":
 characters += numbers

if use_symbols.lower() == "yes":
 characters += symbols

password = ""

for i in range(length):
 password += random.choice(characters)

print("\n=== Password Security Report ===")
print("Generated Password:", password)

if length < 8:
 print("Strength: Weak")

elif length < 12:
 print("Strength: Medium")

else:
 print("Strength: Strong")

