import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def bit_plane_slicing():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Bit Plane Slicing")

        # Ask the user to select the bit plane number (0 to 7)
        plane_num = st.sidebar.slider("Select bit plane number:", min_value=0, max_value=7, value=0)

        # Apply bit plane slicing when the user clicks the button
        if st.sidebar.button("Apply Bit Plane Slicing"):
            # Convert the image to grayscale if it's not already
            gray_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_RGB2GRAY)

            # Extract the selected bit plane
            bit_plane = (gray_image >> plane_num) & 1
            # Convert the bit plane to a 3-channel image (for display purposes)
            bit_plane = np.uint8(bit_plane * 255)  # Convert binary (0/1) to 0/255
            
            # Convert the result back to an image
            current_image = Image.fromarray(cv2.cvtColor(bit_plane, cv2.COLOR_GRAY2RGB))
            st.image(current_image, caption=f"Bit Plane {plane_num} Image", use_column_width=True)
