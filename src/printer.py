from escpos.printer import Usb
from datetime import datetime

VENDOR_ID = 0x04b8
PRODUCT_ID = 0x0202

class ReceiptPrinter:
    def __init__(self):
        self.printer = Usb(VENDOR_ID, PRODUCT_ID)

    def print_receipt(self, plate: str, entry: datetime, exit: datetime, fee: float):
        self.printer.text("Parking Receipt\n")
        self.printer.text(f"Plate No: {plate}\n")
        self.printer.text(f"Entry   : {entry.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.printer.text(f"Exit    : {exit.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.printer.text(f"Fee     : ₹{fee:.2f}\n")
        self.printer.cut()
