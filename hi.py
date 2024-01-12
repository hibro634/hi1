import streamlit as st

# Mock user credentials (replace this with your actual authentication logic)
valid_username = "user"
valid_password = "password"

# Streamlit app
def main():
    st.title("Login Form")

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

def authenticate(username, password):
    # Replace this with your actual authentication logic
    return username == valid_username and password == valid_password

def show_app_content():
    st.header('Supra Video Upload')
    st.write('Upload a video of the Toyota Supra')

    # Rest of your Streamlit app content goes here
    # ...

if __name__ == "__main__":
    main()
