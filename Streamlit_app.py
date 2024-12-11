import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('input_image.jpg')  # Change to your image path
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB for matplotlib

# Function to apply rotation
def rotate_image(image, angle):
    # Get the image center
    center = (image.shape[1] // 2, image.shape[0] // 2)
    # Get the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    # Apply the rotation
    rotated_image = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))
    return rotated_image

# Function to apply scaling
def scale_image(image, fx, fy):
    # Apply scaling
    scaled_image = cv2.resize(image, None, fx=fx, fy=fy, interpolation=cv2.INTER_LINEAR)
    return scaled_image

# Function to apply translation
def translate_image(image, tx, ty):
    # Translation matrix
    translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    # Apply translation
    translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))
    return translated_image

# Function to apply skewing (shearing)
def skew_image(image, alpha, beta):
    # Define the skewing matrix for x and y
    skew_matrix = np.float32([[1, np.tan(np.radians(alpha)), 0], 
                               [np.tan(np.radians(beta)), 1, 0]])
    # Apply skewing
    skewed_image = cv2.warpAffine(image, skew_matrix, (image.shape[1], image.shape[0]))
    return skewed_image

# Example transformations
rotated_image = rotate_image(image, 45)  # Rotate by 45 degrees
scaled_image = scale_image(image, 1.5, 1.5)  # Scale by 1.5 times
translated_image = translate_image(image, 100, 50)  # Translate by (100, 50)
skewed_image = skew_image(image, 30, 20)  # Skew by 30 degrees along x and 20 degrees along y

# Display the images using matplotlib
plt.figure(figsize=(10, 10))

plt.subplot(2, 2, 1)
plt.imshow(rotated_image)
plt.title("Rotated Image (45 degrees)")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(scaled_image)
plt.title("Scaled Image (1.5x)")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(translated_image)
plt.title("Translated Image (100, 50)")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(skewed_image)
plt.title("Skewed Image (30x, 20y)")
plt.axis('off')

# Show the plot
plt.tight_layout()
plt.show()
