import streamlit as st
import face_recognition
import numpy as np
import cv2
from PIL import Image
import os
import base64
def face_reco():
# Set up a directory for storing known faces
    KNOWN_FACES_DIR = "known_faces"
    if not os.path.exists(KNOWN_FACES_DIR):
        os.makedirs(KNOWN_FACES_DIR)
    
    # Function to encode known faces and store them
    def encode_known_faces():
        known_face_encodings = []
        known_face_names = []
        
        for image_name in os.listdir(KNOWN_FACES_DIR):
            image_path = os.path.join(KNOWN_FACES_DIR, image_name)
            image = face_recognition.load_image_file(image_path)
            encoding = face_recognition.face_encodings(image)[0]
            known_face_encodings.append(encoding)
            known_face_names.append(image_name.split('.')[0])  # Name is the image filename without extension
    
        return known_face_encodings, known_face_names
    
    # Function to compare a new image with known faces
    def compare_faces(known_face_encodings, known_face_names, uploaded_image):
        # Encode the uploaded image
        uploaded_image_encoding = face_recognition.face_encodings(uploaded_image)
    
        if uploaded_image_encoding:
            uploaded_image_encoding = uploaded_image_encoding[0]
            distances = face_recognition.face_distance(known_face_encodings, uploaded_image_encoding)
    
            best_match_index = np.argmin(distances)
            return known_face_names[best_match_index], distances[best_match_index]
        else:
            return None, None
    
    # Streamlit UI
    st.title("One-Shot Face Recognition")
    
    # Upload an image
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        # Load the uploaded image
        uploaded_image = face_recognition.load_image_file(uploaded_file)
        
        # Get the known face encodings
        known_face_encodings, known_face_names = encode_known_faces()
        
        # Compare the uploaded image with known faces
        match_name, match_distance = compare_faces(known_face_encodings, known_face_names, uploaded_image)
    
        # Display the result
        if match_name:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            st.write(f"Match found! This is {match_name} with a distance of {match_distance:.2f}")
        else:
            st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
            st.write("No match found in the database.")
    else:
        st.write("Please upload an image to check.")
    
