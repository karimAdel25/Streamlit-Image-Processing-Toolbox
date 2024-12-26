import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Assuming you have a way to load and store the current image
image_history = []

def gamma_correction():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = np.array(Image.open(file).convert('RGB'))
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(current_image.copy())  # Save a copy for undo
        
        st.sidebar.header("Gamma Correction")
        
        # Get the gamma value from the user
        gamma = st.sidebar.number_input(
            "Enter Gamma value (e.g., 1.0, 2.2):", min_value=0.1, value=1.0, step=0.1
        )

        # Apply gamma correction when the user clicks the button
        if st.sidebar.button("Apply Gamma Correction"):
            # Normalize and apply the gamma correction
            corrected_image = np.array(255 * (current_image / 255) ** gamma, dtype=np.uint8)
            
            # Display the corrected image
            st.image(corrected_image, caption="Gamma Corrected Image", use_column_width=True)

# Test if running directly
if __name__ == "__main__":
    st.title("Gamma Correction Tool")
    gamma_correction()
