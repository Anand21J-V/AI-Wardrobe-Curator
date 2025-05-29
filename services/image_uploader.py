import os
from datetime import datetime

SAVE_DIR = "saved_images"

def save_image_locally(image_bytes, filename_prefix="img"):
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    filename = f"{filename_prefix}_{timestamp}.png"
    filepath = os.path.join(SAVE_DIR, filename)
    
    with open(filepath, "wb") as f:
        f.write(image_bytes)
    
    return filepath
