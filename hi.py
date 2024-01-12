import streamlit as st

st.header('Supra Video')
st.write('Watch the Toyota Supra in action!')

# Use a valid video URL
video_url = 'https://youtu.be/96fWYzQK4XA?si=_QZELkSNquRzJpD_'

# Display the video
st.video(video_url)
