import streamlit as st

st.header('Supra')
st.write('Supra')

# Use a valid image URL
image_url = 'https://www.ronbrooks.co.uk/wp-content/uploads/2020/03/Toyota-Supra-1.jpg'

# Display the image with a caption
st.image(image_url, caption='Toyota Supra')

# You can also add alternative text for accessibility
# st.image(image_url, caption='Toyota Supra', alt='Toyota Supra Image')
