import streamlit as st
import time

def cyber_animated_login():
    st.title("Cyber Animated Login")

    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    login_button = st.button("Login")

    if login_button:
        st.info("Logging in...")
        time.sleep(2)  # Simulating login process
        st.success(f"Welcome, {username}!")

if __name__ == "__main__":
    cyber_animated_login()
