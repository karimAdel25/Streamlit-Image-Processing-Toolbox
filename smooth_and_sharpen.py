import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Assuming you have a way to load and store the current image
image_history = []

def smooth_and_sharpen():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo

        # Apply smoothing (Gaussian blur)
        smoothed_image = cv2.GaussianBlur(np.array(current_image), (5, 5), 0)

        # Sharpening kernel
        kernel = np.array([[-1, -1, -1],
                           [-1,  9, -1],
                           [-1, -1, -1]])

        # Apply the kernel to sharpen the smoothed image
        sharpened_image = cv2.filter2D(smoothed_image, -1, kernel)

        # Convert to PIL image and display
        sharpened_image = Image.fromarray(sharpened_image)
        st.image(sharpened_image, caption="Smoothed and Sharpened Image", use_column_width=True)

