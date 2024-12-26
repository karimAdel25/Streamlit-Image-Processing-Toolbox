import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def circular_filter():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Apply Circular Filter")

        # Button to apply the circular filter
        if st.sidebar.button("Apply Circular Filter"):
            # Create a circular kernel (5x5 circle)
            kernel = np.zeros((5, 5), dtype=np.float32)
            center = (2, 2)  # center of the kernel
            radius = 2  # radius of the circle

            for i in range(5):
                for j in range(5):
                    if (i - center[0])**2 + (j - center[1])**2 <= radius**2:
                        kernel[i, j] = 1

            kernel = kernel / kernel.sum()  # Normalize the kernel to sum to 1

            # Apply the circular filter
            filtered_image = cv2.filter2D(np.array(current_image), -1, kernel)
            
            # Convert the filtered image back to PIL and display it
            current_image = Image.fromarray(filtered_image)
            st.image(current_image, caption="Filtered Image", use_column_width=True)
