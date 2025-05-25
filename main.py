import re

def check_password_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        print("Password should be at least 8 characters long.")

    if 