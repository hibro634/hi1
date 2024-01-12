import streamlit as st
import time
from datetime import datetime

# Mock user credentials (replace this with your actual authentication logic)
valid_username = "user"
valid_password = "password"

# Streamlit app
def main():
    st.title("Login Form with Clock Animation")

    # Username and password input
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # Login button
    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful!")
            show_app_content()
        else:
            st.error("Invalid credentials. Please try again.")

    # Clock animation
    st.sidebar.text(get_current_time().strftime("%H:%M:%S"))
    st.sidebar.text("Refreshing every second...")
    animate_clock()

def authenticate(username, password):
    # Replace this with your actual authentication logic
    return username == valid_username and password == valid_password

def show_app_content():
    st.header('Supra Video Upload')
    st.write('Upload a video of the Toyota Supra')

    # Rest of your Streamlit app content goes here
    # ...

def get_current_time():
    return datetime.now()

def animate_clock():
    while True:
        st.sidebar.text(get_current_time().strftime("%H:%M:%S"))
        time.sleep(1)

if __name__ == "__main__":
    main()
