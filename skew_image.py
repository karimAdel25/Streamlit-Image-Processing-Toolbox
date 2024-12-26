import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def skew_image():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Skew Image")
        
        # Get skew factors for X (horizontal) and Y (vertical) from the user
        skew_x = st.sidebar.number_input("Enter skew factor for X (horizontal):", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)
        skew_y = st.sidebar.number_input("Enter skew factor for Y (vertical):", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)

        # Skew when the user clicks the button
        if st.sidebar.button("Skew"):
            # Get the dimensions of the image
            width, height = current_image.size
            M = np.float32([[1, skew_x, 0], [skew_y, 1, 0]])  # Affine transformation matrix

            # Apply the affine transformation (skew)
            skewed_image = cv2.warpAffine(np.array(current_image), M, (width, height))
            
            # Convert the result back to an image and display it
            current_image = Image.fromarray(skewed_image)
            st.image(current_image, caption=f"Skewed Image - X: {skew_x}, Y: {skew_y}", use_column_width=True)
