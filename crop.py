import streamlit as st
import numpy as np
from PIL import Image

# Assuming you have a way to load and store the current image
image_history = []

def crop_image():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Crop Image")
        
        # Get crop dimensions from the user
        width, height = current_image.size
        crop_width = st.sidebar.number_input(
            "Enter crop width:", min_value=1, max_value=width, value=width // 2
        )
        crop_height = st.sidebar.number_input(
            "Enter crop height:", min_value=1, max_value=height, value=height // 2
        )

        # Crop when the user clicks the button
        if st.sidebar.button("Crop"):
            # Calculate cropping bounds
            x_start = max((width - crop_width) // 2, 0)
            y_start = max((height - crop_height) // 2, 0)
            x_end = min((width + crop_width) // 2, width)
            y_end = min((height + crop_height) // 2, height)

            # Perform the crop and display the result
            cropped_image = current_image.crop((x_start, y_start, x_end, y_end))
            st.image(cropped_image, caption="Cropped Image", use_column_width=True)
            
