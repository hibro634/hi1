import streamlit as st

st.header('Supra')
st.write('Supra')

# Use a valid image URL
image_url = 'https://i.pinimg.com/736x/8e/eb/e1/8eebe11cec68e1d4732e71e3f0411cc2.jpg'

# Display the image with a caption
st.image(image_url, caption='Toyota Supra')

# You can also add alternative text for accessibility
# st.image(image_url, caption='Toyota Supra', alt='Toyota Supra Image')
