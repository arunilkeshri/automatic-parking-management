import cv2
import pytesseract
from utils import TESSERACT_CMD, extract_plate_region

pytesseract.pytesseract.tesseract_cmd = TESSERACT_CMD

def detect_plate(image_path: str) -> str:
    img = cv2.imread(image_path)
    plate_img = extract_plate_region(img)
    gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, config='--psm 8')
    return text.strip()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python plate_detection.py <image_path>")
        sys.exit(1)
    plate = detect_plate(sys.argv[1])
    print(f"Detected Plate: {plate}")
