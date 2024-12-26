import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def averaging_filter():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Apply Averaging Filter")

        # Button to apply the averaging filter
        if st.sidebar.button("Apply Averaging Filter"):
            # Apply averaging (mean) filter with a 5x5 kernel
            filtered_image = cv2.blur(np.array(current_image), (5, 5))
            
            # Convert the filtered image back to PIL and display it
            current_image = Image.fromarray(filtered_image)
            st.image(current_image, caption="Filtered Image", use_column_width=True)
