import cv2
from tkinter import filedialog, simpledialog, messagebox
import numpy as np
from PIL import Image

# Assuming current_image is a global variable holding the image (for example, loaded with OpenCV)
current_image = None  # This should be assigned with an actual image, e.g., from OpenCV or PIL

def save_compressed_image():
    global current_image
    if current_image is not None:
        # Ask the user where to save the image
        save_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("PNG files", "*.png")])
        
        # If the user cancels, save_path will be an empty string, so we check if save_path is valid
        if save_path:
            # Determine the file type and set compression parameters
            if save_path.endswith(".jpg"):
                # Save as JPEG with compression quality (0-100, higher = better quality)
                quality = simpledialog.askinteger("JPEG Quality", "Enter quality (1-100):", minvalue=1, maxvalue=100)
                if quality is not None:
                    cv2.imwrite(save_path, current_image, [cv2.IMWRITE_JPEG_QUALITY, quality])
                    messagebox.showinfo("Image Saved", f"Image saved successfully with quality = {quality}!")
            elif save_path.endswith(".png"):
                # Save as PNG with compression level (0-9, higher = more compression)
                compression = simpledialog.askinteger("PNG Compression", "Enter compression level (0-9):", minvalue=0, maxvalue=9)
                if compression is not None:
                    cv2.imwrite(save_path, current_image, [cv2.IMWRITE_PNG_COMPRESSION, compression])
                    messagebox.showinfo("Image Saved", f"Image saved successfully with compression level = {compression}!")
            else:
                messagebox.showerror("Unsupported Format", "Please save the image as .jpg or .png!")
        else:
            messagebox.showwarning("Save Cancelled", "Image save was cancelled!")
    else:
        messagebox.showerror("No Image", "No image to save!")
