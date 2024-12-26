import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Assuming you have a way to load and store the current image
image_history = []

def resize_image():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = np.array(Image.open(file).convert('RGB'))
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(current_image.copy())  # Save a copy for undo
        
        st.sidebar.header("Resize Image")
        
        # Get new dimensions from the user
        height, width, _ = current_image.shape
        new_width = st.sidebar.number_input(
            "Enter new width:", min_value=1, max_value=2000, value=width
        )
        new_height = st.sidebar.number_input(
            "Enter new height:", min_value=1, max_value=2000, value=height
        )

        # Resize when the user clicks the button
        if st.sidebar.button("Resize"):
            resized_image = cv2.resize(current_image, (new_width, new_height))
            
            # Display the resized image
            st.image(resized_image, caption="Resized Image", use_column_width=True)