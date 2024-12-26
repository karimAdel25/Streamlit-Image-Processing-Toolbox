import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def laplacian_filter():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Apply Laplacian Filter")

        # Button to apply the Laplacian filter
        if st.sidebar.button("Apply Laplacian Filter"):
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_BGR2GRAY)

            # Apply the Laplacian filter
            laplacian = cv2.Laplacian(gray_image, cv2.CV_64F)
            laplacian = cv2.convertScaleAbs(laplacian)  # Convert to uint8
            
            # Convert the result back to a 3-channel image (for display purposes)
            current_image = cv2.cvtColor(laplacian, cv2.COLOR_GRAY2BGR)
            
            # Convert back to PIL Image and display
            current_image = Image.fromarray(current_image)
            st.image(current_image, caption="Filtered Image", use_column_width=True)
