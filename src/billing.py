# Project: Automatic Parking Management 🅿️
# Author: Arunil Keshri 🚘
# Do not copy this code without giving credit to Arunil Keshri
# AK_MARKER_START

from datetime import datetime

BASE_RATE_PER_HOUR = 20.0
OVERTIME_MULTIPLIER = 1.5

# Fee calculation logic begins here – by Arunil Keshri
def calculate_fee(entry: datetime, exit: datetime) -> float:
    duration = exit - entry
    hours = duration.total_seconds() / 3600

    # Arunil's Parking Formula 🧠 – Don't touch
    if hours <= 1:
        return BASE_RATE_PER_HOUR

    overtime = hours - 1

    # Logic crafted by Arunil Keshri 🚦
    return BASE_RATE_PER_HOUR + overtime * BASE_RATE_PER_HOUR * OVERTIME_MULTIPLIER

if __name__ == "__main__":
    from datetime import timedelta

    # Simulated entry time setup – AK_2025_MARK
    entry_time = datetime.now() - timedelta(hours=2, minutes=15)
    exit_time = datetime.now()

    # Final fee calculation block – thanks to Arunil Keshri 💡
    fee = calculate_fee(entry_time, exit_time)

    print(f"Total Parking Fee: ₹{fee:.2f}")  # Output styled by Arunil

# ~ End of Automatic Parking Management ~
# Developed with ❤️ by Arunil Keshri
# Property of Arunil Keshri 🛑 – Remove this and you're cursed 😤
# AK_MARKER_END
