import streamlit as st
import time
import numpy as np
import math

def draw_clock(hour, minute, second):
    # Calculate angles for clock hands
    second_angle = math.radians(second * 6)
    minute_angle = math.radians(minute * 6 + second * 0.1)
    hour_angle = math.radians((hour % 12) * 30 + minute * 0.5)

    # Calculate hand lengths
    second_length = 80
    minute_length = 60
    hour_length = 40

    # Calculate hand positions
    second_x = int(second_length * math.sin(second_angle))
    second_y = int(second_length * math.cos(second_angle))

    minute_x = int(minute_length * math.sin(minute_angle))
    minute_y = int(minute_length * math.cos(minute_angle))

    hour_x = int(hour_length * math.sin(hour_angle))
    hour_y = int(hour_length * math.cos(hour_angle))

    # Draw clock hands
    st.markdown(
        f"""
        <canvas id="clockCanvas" width="200" height="200" style="background-color: #f8f8f8; border-radius: 50%; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
        </canvas>
        <script>
            var canvas = document.getElementById("clockCanvas");
            var ctx = canvas.getContext("2d");
            var centerX = canvas.width / 2;
            var centerY = canvas.height / 2;

            // Draw second hand
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(centerX + {second_x}, centerY - {second_y});
            ctx.strokeStyle = "#ff69b4";
            ctx.lineWidth = 2;
            ctx.stroke();

            // Draw minute hand
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(centerX + {minute_x}, centerY - {minute_y});
            ctx.strokeStyle = "#333";
            ctx.lineWidth = 4;
            ctx.stroke();

            // Draw hour hand
            ctx.beginPath();
            ctx.moveTo(centerX, centerY);
            ctx.lineTo(centerX + {hour_x}, centerY - {hour_y});
            ctx.strokeStyle = "#333";
            ctx.lineWidth = 6;
            ctx.stroke();
        </script>
        """,
        unsafe_allow_html=True
    )

def cute_analog_clock():
    st.title("Cute Analog Clock")

    while True:
        current_time = time.localtime()
        draw_clock(current_time.tm_hour, current_time.tm_min, current_time.tm_sec)
        time.sleep(1)
        st.empty()

if __name__ == "__main__":
    cute_analog_clock()
