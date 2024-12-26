import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def thresholding():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo

        # Ask for threshold value via a slider
        threshold_value = st.slider("Select Threshold Value", 0, 255, 128)

        # Apply thresholding when the button is pressed
        if st.button('Apply Thresholding'):
            # Convert image to grayscale
            gray_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_RGB2GRAY)
            
            # Apply thresholding
            _, thresholded_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
            
            # Convert back to BGR format for display
            thresholded_image = cv2.cvtColor(thresholded_image, cv2.COLOR_GRAY2BGR)
            
            # Convert to PIL image and display
            thresholded_image = Image.fromarray(thresholded_image)
            st.image(thresholded_image, caption="Thresholded Image", use_column_width=True)
