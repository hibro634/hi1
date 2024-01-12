import streamlit as st

st.header('Supra Video')
st.write('Watch the Toyota Supra in action!')

# Use a valid video URL
video_url = 'https://www.youtube.com/shorts/bk19fJ2yzw8?app=desktop'

# Display the video
st.video(video_url)
