import re

password = input("Enter a password: ")

score = 0

# Length check
if len(password) >= 8:
    score += 1

# Uppercase check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase check
if re.search(r"[a-z]", password):
    score += 1

# Number check
if re.search(r"\d", password):
    score += 1

# Special character check
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

# Strength rating
if score <= 2:
    print("Password Strength: Weak")
elif score <= 4:
    print("Password Strength: Medium")
else:
    print("Password Strength: Strong")
