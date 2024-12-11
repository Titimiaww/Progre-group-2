import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread(r'C:\Users\LOQ\Pictures\Kucing sweg.jpeg') 
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Mengonversi citra dari BGR ke RGB

# 1. Rotasi
def rotate_image(image, angle):
    # Mendapatkan dimensi citra
    (h, w) = image.shape[:2]
    # Titik pusat gambar untuk rotasi
    center = (w // 2, h // 2)
    # Matriks transformasi rotasi
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Melakukan rotasi citra
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

# 2. Penskalaan (Scaling)
def scale_image(image, scale_factor):
    # Menghitung ukuran baru
    new_w = int(image.shape[1] * scale_factor)
    new_h = int(image.shape[0] * scale_factor)
    # Mengubah ukuran gambar
    scaled_image = cv2.resize(image, (new_w, new_h))
    return scaled_image

# 3. Translasi
def translate_image(image, tx, ty):
    # Matriks translasi
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    # Melakukan translasi citra
    translated_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return translated_image

# 4. Skewing (Shearing)
def skew_image(image, shear_factor_x, shear_factor_y):
    # Matriks skewing
    M = np.float32([[1, shear_factor_x, 0], [shear_factor_y, 1, 0]])
    # Melakukan skewing citra
    skewed_image = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return skewed_image

# Menampilkan hasil gambar
def show_images(images, titles):
    plt.figure(figsize=(15, 10))
    for i, (image, title) in enumerate(zip(images, titles)):
        plt.subplot(2, 3, i+1)
        plt.imshow(image)
        plt.title(title)
        plt.axis('off')
    plt.show()

# Menggunakan fungsi-fungsi di atas
rotated = rotate_image(image, 45)  # Rotasi 45 derajat
scaled = scale_image(image, 0.5)  # Penskalaan dengan faktor 0.5
translated = translate_image(image, 50, 50)  # Translasi 50 piksel di x dan y
skewed = skew_image(image, 0.5, 0)  # Skewing horizontal dengan faktor 0.5

# Menampilkan gambar
show_images([rotated, scaled, translated, skewed], ['Rotated 45°', 'Scaled 0.5', 'Translated', 'Skewed'])
