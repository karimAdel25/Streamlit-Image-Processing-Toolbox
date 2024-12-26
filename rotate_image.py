import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def rotate_image():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Rotate Image")
        
        # Ask the user for the angle to rotate
        angle = st.sidebar.number_input("Enter the angle to rotate (in degrees):", 
                                       min_value=-360, max_value=360, value=0)

        # Rotate when the user clicks the button
        if st.sidebar.button("Rotate"):
            # Get the dimensions of the image
            width, height = current_image.size
            center = (width // 2, height // 2)
            
            # Create the rotation matrix
            rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
            rotated_image = cv2.warpAffine(np.array(current_image), rotation_matrix, (width, height))
            
            # Convert the result back to an image and display it
            current_image = Image.fromarray(rotated_image)
            st.image(current_image, caption=f"Rotated Image - {angle}°", use_column_width=True)
