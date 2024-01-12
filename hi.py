import streamlit as st
import time
import numpy as np
import math
from PIL import Image, ImageDraw

def draw_clock(hour, minute, second):
    # Calculate angles for clock hands
    second_angle = math.radians(second * 6)
    minute_angle = math.radians(minute * 6 + second * 0.1)
    hour_angle = math.radians((hour % 12) * 30 + minute * 0.5)

    # Create an image with a transparent background
    img = Image.new("RGBA", (200, 200), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)

    # Draw clock hands
    draw.line((100, 100, 100 + 80 * math.sin(second_angle), 100 - 80 * math.cos(second_angle)), fill=(255, 105, 180), width=2)
    draw.line((100, 100, 100 + 60 * math.sin(minute_angle), 100 - 60 * math.cos(minute_angle)), fill=(0, 0, 0), width=4)
    draw.line((100, 100, 100 + 40 * math.sin(hour_angle), 100 - 40 * math.cos(hour_angle)), fill=(0, 0, 0), width=6)

    return img

def cute_analog_clock():
    st.title("Cute Analog Clock")

    while True:
        current_time = time.localtime()
        clock_img = draw_clock(current_time.tm_hour, current_time.tm_min, current_time.t
