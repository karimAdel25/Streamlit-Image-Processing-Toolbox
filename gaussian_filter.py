import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def gaussian_filter():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Apply Gaussian Filter")

        # Slider to adjust the kernel size (odd number)
        kernel_size = st.sidebar.slider("Select kernel size:", min_value=3, max_value=15, step=2, value=5)

        # Apply Gaussian filter when the user clicks the button
        if st.sidebar.button("Apply Gaussian Filter"):
            # Apply the Gaussian filter with the selected kernel size
            filtered_image = cv2.GaussianBlur(np.array(current_image), (kernel_size, kernel_size), 0)
            
            # Convert the filtered image back to PIL and display it
            current_image = Image.fromarray(filtered_image)
            st.image(current_image, caption="Filtered Image", use_column_width=True)
