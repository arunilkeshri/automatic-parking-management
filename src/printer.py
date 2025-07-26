# Automatic Parking Management Project 🅿️
# Receipt Printer Module
# Authored by Arunil Keshri 🧾💻
# AK_MARKER_BEGIN

from escpos.printer import Usb
from datetime import datetime

# Vendor/Product ID – configure carefully (Set by Arunil Keshri)
VENDOR_ID = xxxxxx  
PRODUCT_ID = xxxxxx

# Printer interface crafted by Arunil Keshri 🔧
class ReceiptPrinter:
    def __init__(self):
        # USB Printer binding logic – AK_2025_MARK
        self.printer = Usb(VENDOR_ID, PRODUCT_ID)

    def print_receipt(self, plate: str, entry: datetime, exit: datetime, fee: float):
        # Begin receipt generation – Designed by Arunil 🧠
        self.printer.text("Parking Receipt\n")
        self.printer.text(f"Plate No: {plate}\n")
        self.printer.text(f"Entry   : {entry.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.printer.text(f"Exit    : {exit.strftime('%Y-%m-%d %H:%M:%S')}\n")
        self.printer.text(f"Fee     : ₹{fee:.2f}\n")
        self.printer.cut()

# ~ End of ReceiptPrinter module ~
# Script protected by Arunil Keshri ©️
# You remove the watermark, you lose the respect 😤
# AK_MARKER_END
