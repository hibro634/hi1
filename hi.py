import streamlit as st
from datetime import datetime
import time

def cute_beautiful_clock():
    st.title("Cute and Beautiful Clock")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        st.markdown(
            f'<div style="font-size: 48px; color: #ff69b4; text-align: center;">{current_time}</div>',
            unsafe_allow_html=True
        )
        time.sleep(1)
        st.empty()

if __name__ == "__main__":
    cute_beautiful_clock()
