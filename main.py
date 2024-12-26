import streamlit as st

# Add a title to the app
st.title('ToolBox for your BOX')
# Add a selection option in the sidebar
selected_project = st.sidebar.selectbox("Choose the part you want to check", ( "Description","Pneumonia Detection", "Crop Image"
                                                                              ,"Skew Image", "Histogram Equalization", 
                                                                              "Apply Median Filter","Gaussian Filter",
                                                                              "Negative Image", "Gray Level Slicing", "Bit Plane Slicing"
                                                                             ,"face_reco" ,"Save Compressed Image","Smooth and Sharpen","Thresholding","edge_detection","Gaussian Noise","Salt and Pepper Noise","High Pass Filter","Low Pass Filter","sobel_filter","laplacian_filter","Averaging Filter","Circular Filter","Rotate Image","Flip Image","Resize Image", "Gamma Correction"))


# Load the selected project based on user choice
if selected_project == "Circular Filter":
    import circular_filter
    circular_filter.circular_filter()
elif selected_project == "Gaussian Noise":
    import gaussian_noise
    gaussian_noise.gaussian_noise()


elif selected_project == "face_reco":
    import FR
    FR.face_reco()
    
elif selected_project == "Edge Detection":
    import edge_detection
    edge_detection.edge_detection()
elif selected_project == "Crop Image":
    import crop
    crop.crop_image()
elif selected_project == "Thresholding":
    import thresholding
    thresholding.thresholding()
elif selected_project == "Smooth and Sharpen":
    import smooth_and_sharpen
    smooth_and_sharpen.smooth_and_sharpen()
elif selected_project == "Save Compressed Image":
    import save_compressed_image
    save_compressed_image.save_compressed_image()
elif selected_project == "Averaging Filter":
    import averaging_filter
    averaging_filter.averaging_filter()
elif selected_project == "laplacian_filter":
    import laplacian_filter
    laplacian_filter.laplacian_filter()
elif selected_project == "Sobel Filter":
    import sobel_filter
    sobel_filter.sobel_filter()
elif selected_project == "Low Pass Filter":
    import low_pass_filter
    low_pass_filter.low_pass_filter()
elif selected_project == "High Pass Filter":
    import high_pass_filter
    high_pass_filter.high_pass_filter()
elif selected_project == "Salt and Pepper Noise":
    import salt_and_pepper_noise
    salt_and_pepper_noise.salt_and_pepper_noise()


elif selected_project == "Gaussian Filter":
    import gaussian_filter
    gaussian_filter.gaussian_filter()
elif selected_project == "Apply Median Filter":
    import apply_median_filter
    apply_median_filter.apply_median_filter()
elif selected_project == "Bit Plane Slicing":
    import bit_plane_slicing
    bit_plane_slicing.bit_plane_slicing()
elif selected_project == "Gray Level Slicing":
    import gray_level_slicing
    gray_level_slicing.gray_level_slicing()  
elif selected_project == "Rotate Image":
    import rotate_image
    rotate_image.rotate_image()    
elif selected_project == "Flip Image":
    import flip_image
    flip_image.flip_image()
elif selected_project == "Gamma Correction":
    import gamma
    gamma.gamma_correction()
elif selected_project == "Resize Image":
    import resize_image
    resize_image.resize_image()
elif selected_project == "Skew Image":
    import skew_image
    skew_image.skew_image()
elif selected_project == "Histogram Equalization":
    import histogram_equalization
    histogram_equalization.histogram_equalization()
elif selected_project == "Negative Image":
    import negative_image
    negative_image.negative_image()
elif selected_project == "Description":
    import help
    help.show_help()
elif selected_project == "Pneumonia Detection":
    import main_chest
    main_chest.run()