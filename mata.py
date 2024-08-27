import streamlit as st
import os
from PIL import Image

# Set up paths
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Admin Section - Image Upload
st.title("Image Management")

if 'is_admin' not in st.session_state:
    st.session_state.is_admin = False

# Toggle admin mode
if st.button("Toggle Admin Mode"):
    st.session_state.is_admin = not st.session_state.is_admin

# Admin view
if st.session_state.is_admin:
    st.subheader("Admin: Upload Images")
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Save the uploaded image
        file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"Image {uploaded_file.name} uploaded successfully!")

# User View - Image Gallery and Download
st.subheader("Image Gallery")
image_files = os.listdir(UPLOAD_FOLDER)

if image_files:
    for image_file in image_files:
        image_path = os.path.join(UPLOAD_FOLDER, image_file)
        st.image(Image.open(image_path), caption=image_file)
        with open(image_path, "rb") as img_file:
            st.download_button(
                label="Download Image",
                data=img_file,
                file_name=image_file,
                mime="image/jpeg"
            )
else:
    st.info("No images uploaded yet.")
