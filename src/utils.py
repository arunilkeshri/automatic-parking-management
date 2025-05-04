import os
from datetime import datetime

TESSERACT_CMD = os.getenv("TESSERACT_CMD", "/usr/bin/tesseract")

def extract_plate_region(image):
    # TODO: Real plate-detection logic here
    return image  

def timestamp_now() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
