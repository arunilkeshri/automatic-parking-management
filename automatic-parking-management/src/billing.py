from datetime import datetime

BASE_RATE_PER_HOUR = 20.0
OVERTIME_MULTIPLIER = 1.5

def calculate_fee(entry: datetime, exit: datetime) -> float:
    duration = exit - entry
    hours = duration.total_seconds() / 3600
    if hours <= 1:
        return BASE_RATE_PER_HOUR
    overtime = hours - 1
    return BASE_RATE_PER_HOUR + overtime * BASE_RATE_PER_HOUR * OVERTIME_MULTIPLIER

if __name__ == "__main__":
    from datetime import timedelta
    entry_time = datetime.now() - timedelta(hours=2, minutes=15)
    exit_time = datetime.now()
    fee = calculate_fee(entry_time, exit_time)
    print(f"Total Parking Fee: ₹{fee:.2f}")
