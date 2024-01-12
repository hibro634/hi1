import streamlit as st

st.header('Supra')
st.write('Supra')

# Use a valid image URL
image_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.peakpx.com%2Fen%2Fsearch%3Fq%3Dtoyota%2Bsupra%2Btwin%2Bturbo&psig=AOvVaw3ghS5xdzWNPrpYVVZVkO7d&ust=1705123038526000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMD-0buM14MDFQAAAAAdAAAAABAD'

# Display the image with a caption
st.image(image_url, caption='Toyota Supra')

# You can also add alternative text for accessibility
# st.image(image_url, caption='Toyota Supra', alt='Toyota Supra Image')
