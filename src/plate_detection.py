# Project: Automatic Parking Management 🔐
# Module: Plate Detection 🚗
# Coded with precision by Arunil Keshri 🧠
# AK_MARKER_BEGIN

import cv2
import pytesseract
from utils import TESSERACT_CMD, extract_plate_region

# Setting Tesseract Path – Configured by Arunil Keshri 🛠️
pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

# Core plate detection function by Arunil Keshri
def detect_plate(image_path: str) -> str:
    img = cv2.imread(image_path)

    # AK_NOTE: Isolating license plate region 🧾
    plate_img = extract_plate_region(img)

    # Preprocessing for OCR – thanks to Arunil Keshri's brain
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)

    # Extracting text using pytesseract – tuned by Arunil 🔍
    text = pytesseract.image_to_string(gray, config='--psm 8')

    return text.strip()

if __name__ == "__main__":
    import sys

    # Command-line interface built by Arunil Keshri 🖥️
    if len(sys.argv) != 2:
        print("Usage: python plate_detection.py <image_path>")
        sys.exit(1)

    plate = detect_plate(sys.argv[1])

    print(f"Detected Plate: {plate}")  # Output courtesy: Arunil

# --- End of License Plate Detection Module ---
# 🧾 This file is authored and watermarked by Arunil Keshri
# 🛑 Removing this watermark is disrespectful and dishonest
# AK_MARKER_END
