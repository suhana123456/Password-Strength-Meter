import streamlit as st
import re
import random
import string

# Function to check password strength
def check_strength(password):
    length = len(password) >= 8
    upper = bool(re.search(r"[A-Z]", password))
    lower = bool(re.search(r"[a-z]", password))
    number = bool(re.search(r"[0-9]", password))
    special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))

    score = sum([length, upper, lower, number, special])

    if score == 5:
        return "🟢 Strong", "#2ECC71", "✅ Awesome! Your password is strong and secure."
    elif score >= 3:
        return "🟡 Medium", "#F1C40F", "⚠️ Your password is okay but could be stronger."
    else:
        return "🔴 Weak", "#E74C3C", "❌ Weak Password! Follow the tips below to strengthen it."

# Function to generate a strong password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return "".join(random.choice(chars) for _ in range(12))

# Main Heading with Lock Emoji
st.markdown("<h1 style='text-align: center; color: #3498DB;'>🔐 Password Strength Meter</h1>", unsafe_allow_html=True)


# Highlighted Subtext
st.markdown("<h4 style='text-align: center; color: #555;'>Check Your Password Strength & Make It Unbreakable! 🔐</h4>", unsafe_allow_html=True)

# Password Input
password = st.text_input("Enter your password:", type="password")

if password:
    strength, color, message = check_strength(password)

    # Strength Message
    st.markdown(f'<p style="color:{color}; font-size:18px; font-weight:bold;">{message}</p>', unsafe_allow_html=True)

    # Strength Bar
    progress = {"🔴 Weak": 0.3, "🟡 Medium": 0.6, "🟢 Strong": 1.0}[strength]
    st.progress(progress)

    # Improvement Suggestions
    st.markdown("💡 *Tips to Strengthen Your Password:*", unsafe_allow_html=True)
    suggestions = [
        ("🔴", "Password should be at least 8 characters long.", len(password) >= 8),
        ("🟠", "Include both uppercase and lowercase letters.", any(c.isupper() for c in password) and any(c.islower() for c in password)),
        ("🟡", "Add at least one number (0-9).", any(c.isdigit() for c in password)),
        ("🟢", "Include at least one special character (!@#$%^&).", any(c in "!@#$%^&()" for c in password)),
    ]

    for emoji, text, condition in suggestions:
        color = "🟢" if condition else emoji
        st.markdown(f"- {color} {text}", unsafe_allow_html=True)

# Generate Strong Password Button
if st.button("🔑 Generate Strong Password"):
    st.success(f"🔐 Try this: {generate_password()}")

# Custom Footer (Always Visible)
st.markdown(
    """
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #222;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 14px;
        }
        .footer a {
            color: #3498DB;
            text-decoration: none;
            font-weight: bold;
        }
        .footer a:hover {
            color: #1ABC9C;
        }
    </style>
    <div class="footer">
        ✨ Created by Suhana Khan | <a href="https://streamlit.io/" target="_blank">Hosted by Streamlit</a>
    </div>
    """,
    unsafe_allow_html=True
)
