import streamlit as st
import numpy as np
from PIL import Image
import cv2

# Assuming you have a way to load and store the current image
image_history = []

def low_pass_filter():
    # Upload and display the image
    file = st.file_uploader('Upload an image', type=['jpeg', 'jpg', 'png'])
    if file is not None:
        current_image = Image.open(file).convert('RGB')
        st.image(current_image, caption="Uploaded Image", use_column_width=True)

        # Save the uploaded image state
        image_history.append(np.array(current_image))  # Save as a NumPy array for undo
        
        st.sidebar.header("Apply Low Pass Filter")

        # Button to apply the low-pass filter
        if st.sidebar.button("Apply Low Pass Filter"):
            # Convert the image to grayscale and then to float32
            gray_image = cv2.cvtColor(np.array(current_image), cv2.COLOR_BGR2GRAY)
            gray_image = np.float32(gray_image)

            # Apply FFT to the image
            f = np.fft.fft2(gray_image)
            fshift = np.fft.fftshift(f)

            # Create a low pass filter mask
            rows, cols = gray_image.shape
            crow, ccol = rows // 2, cols // 2  # center of the image
            radius = 30  # Low-pass filter radius

            mask = np.zeros((rows, cols), np.float32)
            mask[crow - radius:crow + radius, ccol - radius:ccol + radius] = 1  # Create circular mask

            # Apply mask to the frequency space
            fshift = fshift * mask

            # Inverse FFT to get the image back
            f_ishift = np.fft.ifftshift(fshift)
            img_back = np.fft.ifft2(f_ishift)
            img_back = np.abs(img_back)

            # Convert back to uint8
            img_back = np.uint8(img_back)
            current_image = cv2.cvtColor(img_back, cv2.COLOR_GRAY2BGR)
            
            # Convert to PIL image and display
            current_image = Image.fromarray(current_image)
            st.image(current_image, caption="Filtered Image", use_column_width=True)
