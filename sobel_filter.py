import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def sobel_filter():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Apply Sobel Filter")

        # Button to apply the Sobel filter
        if st.sidebar.button("Apply Sobel Filter"):
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_BGR2GRAY)

            # Sobel filter in the x and y direction
            sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
            sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)

            # Combine the two Sobel filters to get the gradient magnitude
            sobel_mag = cv2.magnitude(sobel_x, sobel_y)
            sobel_mag = cv2.convertScaleAbs(sobel_mag)  # Convert to uint8

            # Convert the result back to a 3-channel image (for display purposes)
            current_image = cv2.cvtColor(sobel_mag, cv2.COLOR_GRAY2BGR)
            
            # Convert back to PIL Image and display
            current_image = Image.fromarray(current_image)
            st.image(current_image, caption="Filtered Image", use_column_width=True)
