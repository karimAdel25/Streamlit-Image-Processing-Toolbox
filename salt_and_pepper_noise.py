import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def salt_and_pepper_noise():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Add Salt and Pepper Noise")

        # Get noise percentage from user input
        noise_percentage = st.sidebar.slider("Noise Percentage", 0, 100, 5, help="Higher values will make the image less visible")

        if st.sidebar.button("Apply Salt & Pepper Noise"):
            # Convert the image to a NumPy array for manipulation
            noisy_image = np.array(current_image)
            noise_pixels = int(noisy_image.size * (noise_percentage / 100))
            
            # Add Salt and Pepper noise
            for _ in range(noise_pixels // 2):
                # Add salt (white pixels)
                x, y = np.random.randint(0, noisy_image.shape[1]), np.random.randint(0, noisy_image.shape[0])
                noisy_image[y, x] = [255, 255, 255]  # Salt

                # Add pepper (black pixels)
                x, y = np.random.randint(0, noisy_image.shape[1]), np.random.randint(0, noisy_image.shape[0])
                noisy_image[y, x] = [0, 0, 0]  # Pepper

            # Convert back to a PIL image and display it
            noisy_image = Image.fromarray(noisy_image)
            st.image(noisy_image, caption="Image with Salt and Pepper Noise", use_column_width=True)

