import streamlit as st

html_code = """
<style>
    body {
        font-family: 'Helvetica Neue', sans-serif;
        background: #333;
    }

    .container {
        display: flex;
        justify-content: space-around;
        align-items: center;
        height: 100vh;
    }

    .login {
        text-align: center;
        color: white;
    }

    .login-content {
        margin-top: 20px;
    }

    label {
        display: block;
        margin: 10px 0;
        font-size: 14px;
    }

    input {
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        box-sizing: border-box;
    }

    a {
        color: #7db8c8;
        text-decoration: none;
        margin-right: 10px;
    }

    input[type="submit"] {
        background: #7db8c8;
        color: white;
        padding: 10px;
        cursor: pointer;
        border: none;
    }

    .message {
        text-align: center;
        color: white;
    }

    .message span {
        display: block;
        font-size: 36px;
        margin-top: 10px;
    }

    .first {
        color: #ffcc00;
    }

    .second {
        color: #ff69b4;
    }

    .third {
        color: #7db8c8;
    }
</style>

<section class="container">
    <div class="span-6">
        <div class="login">
            <h1>Greetings!</h1>
            <div class="login-content">
                <label id="emailLabel">Please enter a valid email</label>
                <input id="email" placeholder="Email" />
                <label id="passwordLabel">Please enter your password</label>
                <input type="password" id="password" placeholder="Password" /><br>
                <a href="#">Forgot Username </a>&#x2022<a href="#"> Forgot Password</a><br>
                <input type="submit" value="Login">
            </div>
        </div>
    </div>
    <div class="span-6">
        <div class="message">
            <span class="first">Design</span>
            <span class="second">is</span>
            <span class="third">Everywhere</span>
        </div>
    </div>
</section>
"""

st.markdown(html_code, unsafe_allow_html=True)
