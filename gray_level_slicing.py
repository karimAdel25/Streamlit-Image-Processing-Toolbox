import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def gray_level_slicing():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Gray Level Slicing")

        # Get gray level slicing limits from the user
        lower_limit = st.sidebar.slider("Lower limit:", min_value=0, max_value=255, value=100)
        upper_limit = st.sidebar.slider("Upper limit:", min_value=0, max_value=255, value=200)

        # Apply gray level slicing when the user clicks the button
        if st.sidebar.button("Apply Gray Level Slicing"):
            # Apply gray level slicing using cv2.inRange()
            sliced_img = cv2.inRange(np.array(current_image), (lower_limit, lower_limit, lower_limit), (upper_limit, upper_limit, upper_limit))
            sliced_img = cv2.cvtColor(sliced_img, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels
            
            # Convert the result back to an image and display it
            current_image = Image.fromarray(sliced_img)
            st.image(current_image, caption="Gray Level Sliced Image", use_column_width=True)
