import streamlit as st
import random
import string
import re

def generate_strong_password(length=12):
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(all_chars) for _ in range(length))

def check_password_strength(password):
    score = 0
    messages = []

    common_passwords = ["password", "123456", "qwerty", "password123", "letmein"]

    if password.lower() in common_passwords:
        messages.append("This password is too common.")
        return (0, messages)
    # length check
    if len(password) >= 12:
        score += 2
        messages.append("✅ Great length(12+ characters.)")
    elif len(password) >= 8:
        score += 1
        messages.append("✅ Good length (8-11 characters.)")
    else:
        messages.append("Password should be at least 8 characters long.")

    # case check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
        messages.append("✅ Has both upper and lower case letters")
    else:
        messages.append("Include both upper and lower case letters.")

    # digit check
    if re.search(r"\d", password):
        score += 1
        messages.append("✅ Contains numbers")
    else:
        messages.append("Add at least one digit from (0-9)")
    
    # special characters check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
        messages.append("Contain special characters(!@#$%^&*)")
    else:
        messages.append("Include at least one special character (!@#$%^&*)")

    return (score, messages)
    
# streamlit UI
st.set_page_config(page_title="Password Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter Your Password", type="password")

if st.button("Check Strength"):
    score, feedback = check_password_strength(password)
    for msg in feedback:
        st.write(msg)

    st.markdown("**Score: **" + str(score) + "/6")
    if score >= 5:
        st.success("✅ Strong Password")
    elif score >= 3:
        st.warning("⚠️ Moderate Password.")
    else:
        st.error("❌ Weak Password")

if st.button("Generate Strong Password"):
    generated_pw = generate_strong_password()
    st.success(f"Suggested Password: {generate_strong_password}")
    st.code(generated_pw, language='')
    # if score == 4:
    #     print("✅ Strong Password")
    # elif score == 3:
    #     print("⚠️ Moderate Password")
    # else:
    #     print("Weak Password")

# password = input("Enter your password: ")
# check_password_strength(password)