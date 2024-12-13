import cv2
import numpy as np
import streamlit as st

# Function to load the uploaded image
def load_image(image_file):
    image_bytes = np.asarray(bytearray(image_file.read()), dtype=np.uint8)
    image = cv2.imdecode(image_bytes, cv2.IMREAD_COLOR)
    
    if image is None:
        st.error("Failed to load image. Check the file format.")
        return None
    
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return image

# Function to rotate the image
def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

# Function to scale the image
def scale_image(image, fx, fy):
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Function to translate the image
def translate_image(image, tx, ty):
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

# Function to skew the image
def skew_image(image, alpha, beta):
    skew_matrix = np.float32([[1, np.tan(np.radians(alpha)), 0], 
                               [np.tan(np.radians(beta)), 1, 0]])
    skewed_image = cv2.warpAffine(image, skew_matrix, (image.shape[1], image.shape[0]))
    return skewed_image

# Title of the app
st.title("Image Transformation with OpenCV")

# Image upload functionality
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = load_image(uploaded_file)
    
    if image is not None:
        # Display the original image
        st.image(image, caption="Original Image", use_container_width=True)

        # Dropdown for selecting the transformation
        transformation = st.selectbox("Choose a Transformation", ["Rotation", "Scaling", "Translation", "Skewing"])

        if transformation == "Rotation":
            angle = st.slider("Select Rotation Angle", min_value=-180, max_value=180, value=45)
            rotated_image = rotate_image(image, angle)
            st.image(rotated_image, caption="Rotated Image", use_container_width=True)

        elif transformation == "Scaling":
            fx = st.slider("Scale X Axis", min_value=0.1, max_value=3.0, value=1.5)
            fy = st.slider("Scale Y Axis", min_value=0.1, max_value=3.0, value=1.5)
            scaled_image = scale_image(image, fx, fy)
            st.image(scaled_image, caption="Scaled Image", use_container_width=True)

        elif transformation == "Translation":
            tx = st.slider("Translate X Axis", min_value=-100, max_value=100, value=50)
            ty = st.slider("Translate Y Axis", min_value=-100, max_value=100, value=50)
            translated_image = translate_image(image, tx, ty)
            st.image(translated_image, caption="Translated Image", use_container_width=True)

        elif transformation == "Skewing":
            alpha = st.slider("Skew X Axis (degrees)", min_value=-45, max_value=45, value=30)
            beta = st.slider("Skew Y Axis (degrees)", min_value=-45, max_value=45, value=20)
            skewed_image = skew_image(image, alpha, beta)
            st.image(skewed_image, caption="Skewed Image", use_container_width=True)
