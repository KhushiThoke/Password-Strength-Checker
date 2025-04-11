import streamlit as st
import string

def check_strength(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_special])
    length_ok = len(password) >= 8

    if score <= 2 or not length_ok:
        return "Weak 😬", "red"
    elif score == 3:
        return "Moderate 🙂", "orange"
    else:
        return "Strong 🔐", "green"

# --- Streamlit UI ---
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, color = check_strength(password)
    st.markdown(f"### <span style='color:{color}'>Password Strength: {strength}</span>", unsafe_allow_html=True)
