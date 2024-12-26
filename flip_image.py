import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def flip_image():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Flip Image")
        
        # Get flip direction from the user
        flip_option = st.sidebar.selectbox(
            "Select flip option:", ["Horizontal", "Vertical", "Both"]
        )

        # Flip when the user clicks the button
        if st.sidebar.button("Flip"):
            if flip_option == "Horizontal":
                flipped_image = cv2.flip(np.array(current_image), 1)
            elif flip_option == "Vertical":
                flipped_image = cv2.flip(np.array(current_image), 0)
            elif flip_option == "Both":
                flipped_image = cv2.flip(np.array(current_image), -1)
            else:
                st.error("Invalid flip option selected.")
                return

            # Convert the result back to an image and display it
            current_image = Image.fromarray(flipped_image)
            st.image(current_image, caption=f"Flipped Image - {flip_option}", use_column_width=True)
