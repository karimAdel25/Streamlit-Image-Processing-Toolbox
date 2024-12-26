import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def edge_detection():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        # Apply Edge Detection when the button is pressed
        if st.button('Apply Edge Detection'):
            # Convert the image to grayscale
            gray_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_RGB2GRAY)
            
            # Apply Canny edge detection
            edges = cv2.Canny(gray_image, 100, 200)
            
            # Convert edges to BGR format
            edge_image = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

            # Convert to PIL image and display
            edge_image = Image.fromarray(edge_image)
            st.image(edge_image, caption="Edge Detected Image", use_column_width=True)
