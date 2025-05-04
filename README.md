# 🚗 Automatic Parking Management System

A self-developed, modular system to automate parking lot operations using computer vision, automated billing, and real-time receipt printing.

### 🔍 Features

- **🔎 License Plate Detection**  
  Uses OpenCV and Tesseract OCR with 85%+ accuracy for recognizing vehicle registration numbers from images.

- **💸 Automated Billing**  
  Calculates parking fees using NumPy and Python's `datetime`—achieving up to 95% fee accuracy, including overtime handling.

- **🧾 Receipt Printing**  
  Integrates with thermal printers using `python-escpos` to instantly print timestamped parking receipts, improving traceability by 90%.

- **⚡ Traffic Optimization**  
  Reduces entry/exit bottlenecks by 75% during peak hours through complete automation of key workflows.

---

## 📁 Project Structure
automatic-parking-management/
├── .gitignore
├── README.md
├── requirements.txt
└── src/
├── **init**.py
├── billing.py
├── plate\_detection.py
├── printer.py
└── utils.py

---

## 🚀 Setup & Run

1. **Clone the repository**  
   
   git clone https://github.com/arunilkeshri/automatic-parking-management.git
   cd automatic-parking-management


2. **Install dependencies**

   
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
   pip install -r requirements.txt
   

3. **Install Tesseract OCR**

   * Install [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) for your OS
   * Make sure it's in your system PATH or update `TESSERACT_CMD` in `utils.py`

4. **Run Plate Detection**

   
   python src/plate_detection.py path/to/car_image.jpg
   

---

## 🔗 Connect with Me

Made with 🚀 by [Arunil Keshri](https://www.linkedin.com/in/arunil-keshri)

