import streamlit as st
from util_chest import set_background
import os 
os.chdir(r"C:\APP")

def show_help():
    # Help descriptions
    set_background('toolbox.jpg') 
    descriptions = """
    **Open Image**:
    Use this button to open an image file from your computer. Once opened, the image will be displayed
    in the window.

    **Save Image**:
    Use this button to save the currently displayed image to a file. You can choose the format
    (JPEG, PNG, etc.) and location.

    **Save Compressed**:
    Use this button to save the image in a compressed format. 
    - For JPEG: You will be prompted to enter a quality value (1-100). 
      Higher values mean better quality but less compression.
    - For PNG: You will be prompted to enter a compression level (0-9). 
      Higher values mean higher compression but slower saving time.

    **Apply Grayscale**:
    This converts the image to grayscale (black & white). It removes color information
    and retains intensity.

    **Undo Last Action**:
    Reverts the image to its previous state. You can only undo if an action has been performed before.

    **Redo Last Action**:
    Restores the last undone action. You can only redo if you have undone a previous action.

    **Reset Image**:
    Restores the image to its original state when it was first opened. 
    This will discard any changes made.

    **Resize Image**:
    Allows you to resize the image by entering new width and height values.
    Be mindful of maintaining aspect ratio.

    **Crop Image**:
    Lets you crop the image by specifying the width and height for the crop area. 
    The crop will be centered in the image.

    **Flip Image**:
    Flips the image either horizontally, vertically, or both. 
    Select the flip option from the dropdown menu.

    **Rotate Image**:
    Rotates the image by a specified angle. 
    The rotation is done in degrees and can be either clockwise or counterclockwise.

    **Skew Image**:
    Skews the image along the X and Y axes by entering factors for each direction. 
    This distorts the image's shape.

    **Histogram Equalization**:
    Enhances the contrast of an image by adjusting the intensity distribution. 
    This is useful for improving visibility.

    **Negative Image**:
    Inverts the colors of the image. Dark areas become light, and light areas become dark.

    **Log Transformation**:
    Applies a logarithmic transformation to enhance dark regions of the image. 
    Useful for low-contrast images.

    **Gamma Correction**:
    Adjusts the brightness of the image.
    Values greater than 1 make the image darker, while values less than 1 make it brighter.

    **Gray Level Slicing**:
    Selects a range of gray levels and slices the image to retain only pixels in that range, 
    creating a high contrast effect.

    **Bit Plane Slicing**:
    Extracts a specific bit plane from the image, 
    which represents the least significant bits of the pixel values.

    **Median Filter**:
    Applies a median filter to reduce noise in the image. 
    This is particularly useful for removing "salt and pepper" noise.

    **Gaussian Filter**:
    Smoothens the image using a Gaussian blur, 
    which reduces high-frequency noise and softens edges.

    **Circular Filter**:
    Applies a circular kernel filter, 
    which is used for smoothing and enhancing specific features in the image.

    **Averaging Filter**:
    Applies a mean filter to the image, 
    smoothing the pixel values by averaging them with their neighbors.

    **Laplacian Filter**:
    Detects edges in the image by calculating the Laplacian (second derivative) of the image. 
    Useful for edge detection.

    **Sobel Filter**:
    Applies the Sobel filter to detect horizontal and vertical edges in the image. 
    This is one of the edge detection techniques.

    **Low Pass Filter (Frequency Domain)**:
    Filters out high-frequency components in the image, keeping only the low frequencies. 
    This is typically used for smoothing.

    **High Pass Filter (Frequency Domain)**:
    Removes low-frequency components, keeping only the high frequencies, 
    which enhances edges and fine details.

    **Salt and Pepper Noise**:
    Adds random black and white pixels (salt and pepper noise) to the image. 
    You can control the percentage of noise added.

    **Gaussian Noise**:
    Adds random noise from a Gaussian distribution to the image. 
    This simulates noise often seen in low-light conditions.

    **Edge Detection**:
    Detects edges in the image using the Canny edge detection algorithm. 
    This highlights the areas where significant intensity changes occur.

    **Thresholding**:
    Converts the image to black and white based on a specific threshold value. 
    Pixels above the threshold become white, below become black.

    **Smooth and Sharpen**:
    First smoothens the image using a Gaussian blur, 
    then sharpens it by applying a filter that enhances edges.

    **OCR (Extract Text from Image)**:
    This feature extracts text from the image using Optical Character Recognition (OCR). 
    It converts text in the image to editable text.
    After extraction, the text is displayed in a pop-up window and can be optionally saved to a .txt file.
    """

    # Use Streamlit widgets to display the help descriptions
    st.title("Help - Function Descriptions")
    with st.expander("Click to view function descriptions"):
        st.text(descriptions)

# Example usage in a Streamlit app
if __name__ == "__main__":
    st.sidebar.button("Show Help", on_click=show_help)
