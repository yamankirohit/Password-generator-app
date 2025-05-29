import streamlit as st
import random
import string

# --- Streamlit page config ---
st.set_page_config(page_title="Password Generator", layout="centered")
st.title("🔐 Password Generator")

# --- Password generator function ---
def generate_password(length, strength):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    if strength == "Weak":
        all_chars = lowercase
    elif strength == "Medium":
        all_chars = lowercase + uppercase + digits
    elif strength == "Strong":
        all_chars = lowercase + uppercase + digits + symbols
    else:
        return "Invalid strength option selected."

    # Ensure at least one character from each needed category
    password = []

    if strength == "Weak":
        password.append(random.choice(lowercase))
    elif strength == "Medium":
        password += [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits)
        ]
    elif strength == "Strong":
        password += [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]

    remaining_length = max(0, length - len(password))
    password += random.choices(all_chars, k=remaining_length)

    random.shuffle(password)
    return ''.join(password)

# --- User Inputs ---
strength = st.selectbox("Select Password Strength", ["Weak", "Medium", "Strong"])
length = st.slider("Select Password Length", min_value=4, max_value=50, value=12)

# --- Generate Button ---
if st.button("Generate Password"):
    pwd = generate_password(length, strength)
    st.success(f"Generated {strength} Password: `{pwd}`")
