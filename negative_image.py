import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def negative_image():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Negative Image")

        # Apply negative transformation when the user clicks the button
        if st.sidebar.button("Apply Negative"):
            # Perform the negative effect using bitwise NOT
            negative = cv2.bitwise_not(np.array(current_image))
            
            # Convert the result back to an image and display it
            current_image = Image.fromarray(negative)
            st.image(current_image, caption="Negative Image", use_column_width=True)
