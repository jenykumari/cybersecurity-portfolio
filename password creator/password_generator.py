import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

length = int(input("Enter password length: "))

password = ""

for i in range(length):
    password = password + random.choice(characters)

print("Generated Password:", password)
