import streamlit as st

st.header('Supra Video')
st.write('Watch the Toyota Supra in action!')

# Use a valid video URL
video_url = 'https://youtu.be/ZtkgNfC9exI?si=Nexa5W62_TqvD4PV'

# Display the video
st.video(video_url)
