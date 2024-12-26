import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def histogram_equalization():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Histogram Equalization")
        
        # Apply histogram equalization when the user clicks the button
        if st.sidebar.button("Apply Histogram Equalization"):
            # Check if image is grayscale or color
            if len(current_image.convert('RGB').getbands()) == 1:  # Grayscale image
                equalized_image = cv2.equalizeHist(np.array(current_image))
            else:  # Color image
                # Convert to YUV color space and equalize the Y channel
                yuv_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_RGB2YUV)
                yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
                equalized_image = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2RGB)
            
            # Convert the result back to an image and display it
            current_image = Image.fromarray(equalized_image)
            st.image(current_image, caption="Equalized Image", use_column_width=True)
