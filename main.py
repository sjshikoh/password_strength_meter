import random
import string
import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        print("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        print("Include both upper and lower case letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        print("Add at least one digit from (0-9)")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        print("Include at least one special character (!@#$%^&*)")

    if score == 4:
        print("✅ Strong Password")
    elif score == 3:
        print("⚠️ Moderate Password")
    else:
        print("Weak Password")

password = input("Enter your password: ")
check_password_strength(password)