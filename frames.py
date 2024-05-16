import cv2
from PIL import Image
import numpy as np
import os

# Constants
VIDEO_PATH = 'bad-apple.mp4'
OUTPUT_FOLDER = 'frames'
ASCII_CHARS = "@%#*+=-:. "
NEW_WIDTH = 100

# Function to extract frames from video
def extract_frames(video_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    cap = cv2.VideoCapture(video_path)
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_path, frame)
        frame_count += 1
    
    cap.release()

# Function to convert image to ASCII art
def image_to_ascii(image_path, new_width=100):
    image = Image.open(image_path)
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width)
    image = image.resize((new_width, new_height)).convert('L')
    pixels = np.array(image)
    ascii_str = "".join([ASCII_CHARS[pixel // 32] for pixel in pixels.flatten()])
    ascii_img = "\n".join([ascii_str[i:i + new_width] for i in range(0, len(ascii_str), new_width)])
    return ascii_img

# Extract frames from video
extract_frames(VIDEO_PATH, OUTPUT_FOLDER)

# Convert frames to ASCII art
ascii_frames = []
frame_files = sorted(os.listdir(OUTPUT_FOLDER))
for frame_file in frame_files:
    ascii_frames.append(image_to_ascii(os.path.join(OUTPUT_FOLDER, frame_file)))

# Save ASCII frames to a text file
with open('ascii_frames.txt', 'w') as f:
    f.write("\n\n".join(ascii_frames))

print("ASCII frames saved to ascii_frames.txt")
