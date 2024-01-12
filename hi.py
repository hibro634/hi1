import streamlit as st
from datetime import datetime
import time

def cute_beautiful_clock():
    st.title("Cute and Beautiful Clock")

    while True:
        current_time = datetime.now().strftime("%H:%M:%S")
        
        # CSS for circular clock
        clock_style = """
            <style>
                .clock {
                    width: 200px;
                    height: 200px;
                    background-color: #f8f8f8;
                    border-radius: 50%;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-size: 24px;
                    color: #ff69b4;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                }
            </style>
        """

        # HTML for circular clock
        clock_html = f"""
            <div class="clock">
                {current_time}
            </div>
        """

        # Display clock
        st.markdown(clock_style, unsafe_allow_html=True)
        st.markdown(clock_html, unsafe_allow_html=True)

        time.sleep(1)
        st.empty()

if __name__ == "__main__":
    cute_beautiful_clock()
