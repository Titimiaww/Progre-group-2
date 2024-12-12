import cv2
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Fungsi untuk memuat gambar
def load_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        st.error("Gambar gagal dimuat. Periksa path gambar.")
        return None
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Konversi BGR ke RGB untuk matplotlib
    return image

# Fungsi untuk rotasi gambar
def rotate_image(image, angle):
    center = (image.shape[1] // 2, image.shape[0] // 2)
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

# Fungsi untuk skala gambar
def scale_image(image, fx, fy):
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Fungsi untuk translasi gambar
def translate_image(image, tx, ty):
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

# Fungsi untuk skewing (shearing) gambar
def skew_image(image, alpha, beta):
    skew_matrix = np.float32([[1, np.tan(np.radians(alpha)), 0], 
                               [np.tan(np.radians(beta)), 1, 0]])
    skewed_image = cv2.warpAffine(image, skew_matrix, (image.shape[1], image.shape[0]))
    return skewed_image

# Judul aplikasi
st.title("Transformasi Gambar dengan OpenCV")

# Upload gambar dari pengguna
uploaded_file = st.file_uploader("Pilih gambar", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Membaca dan menampilkan gambar yang diupload
    image = load_image(uploaded_file)
    if image is not None:
        # Menampilkan gambar asli
        st.image(image, caption="Gambar Asli", use_column_width=True)

        # Menu untuk memilih transformasi gambar
        transformation = st.selectbox("Pilih Transformasi", ["Rotasi", "Skala", "Translasi", "Skewing"])

        if transformation == "Rotasi":
            angle = st.slider("Pilih sudut rotasi", min_value=-180, max_value=180, value=45)
            rotated_image = rotate_image(image, angle)
            st.image(rotated_image, caption="Gambar Setelah Rotasi", use_column_width=True)

        elif transformation == "Skala":
            fx = st.slider("Skala Sumbu X", min_value=0.1, max_value=3.0, value=1.5)
            fy = st.slider("Skala Sumbu Y", min_value=0.1, max_value=3.0, value=1.5)
            scaled_image = scale_image(image, fx, fy)
            st.image(scaled_image, caption="Gambar Setelah Skala", use_column_width=True)

        elif transformation == "Translasi":
            tx = st.slider("Pilih translasi sumbu X", min_value=-100, max_value=100, value=50)
            ty = st.slider("Pilih translasi sumbu Y", min_value=-100, max_value=100, value=50)
            translated_image = translate_image(image, tx, ty)
            st.image(translated_image, caption="Gambar Setelah Translasi", use_column_width=True)

        elif transformation == "Skewing":
            alpha = st.slider("Skew Sumbu X (derajat)", min_value=-45, max_value=45, value=30)
            beta = st.slider("Skew Sumbu Y (derajat)", min_value=-45, max_value=45, value=20)
            skewed_image = skew_image(image, alpha, beta)
            st.image(skewed_image, caption="Gambar Setelah Skewing", use_column_width=True)
