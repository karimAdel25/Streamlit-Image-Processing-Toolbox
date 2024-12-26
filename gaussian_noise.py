import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def gaussian_noise():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Add Gaussian Noise")

        # Get noise parameters from user input
        mean = st.sidebar.slider("Mean", -255, 255, 0, help="The mean of the Gaussian noise (typically 0 for no bias)")
        stddev = st.sidebar.slider("Standard Deviation", 0.1, 255, 25, help="The standard deviation of the Gaussian noise")

        if st.sidebar.button("Apply Gaussian Noise"):
            # Generate Gaussian noise
            gaussian_noise = np.random.normal(mean, stddev, current_image.size).reshape(current_image.size[::-1] + (3,))
            
            # Convert to uint8 and add Gaussian noise
            gaussian_noise = np.uint8(gaussian_noise)

            # Add Gaussian noise to the image
            noisy_image = cv2.add(np.array(current_image), gaussian_noise)

            # Convert noisy image back to a PIL image and display
            noisy_image = Image.fromarray(noisy_image)
            st.image(noisy_image, caption="Image with Gaussian Noise", use_column_width=True)
