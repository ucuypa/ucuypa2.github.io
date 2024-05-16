import cv2

def image_to_ascii(image_path, new_width=100):
    try:
        image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if image is None:
            raise Exception("Failed to read image")
        height, width = image.shape
        aspect_ratio = height / width
        new_height = int(aspect_ratio * new_width)
        resized_image = cv2.resize(image, (new_width, new_height))
        ascii_str = "".join([ASCII_CHARS[pixel // 32] for row in resized_image for pixel in row])
        ascii_img = "\n".join([ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width)])
        return ascii_img
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None
