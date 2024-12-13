import cv2

# Load the image in grayscale
img = cv2.imread('jk.jpg', 0)

# Apply median blur for smoothing
img = cv2.medianBlur(img, 5)

# Apply adaptive thresholding to create a binary image
image = cv2.adaptiveThreshold(
    img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Resize the image while preserving the aspect ratio
new_width = 120  # Increase this for more detail
aspect_ratio = len(image) / len(image[0])
new_height = int(aspect_ratio * new_width)
resized_image = cv2.resize(image, (new_width, new_height))

# Map pixel intensity to characters
chars = "@#S%?*+;:,."  # Gradient of characters from dark to light
char_len = len(chars)

for row in resized_image:
    for pixel in row:
        # Map pixel value (0-255) to an index in the character list
        char_index = int((pixel / 255) * (char_len - 1))
        print(chars[char_index], end="")
    print()  # New line at the end of each row
