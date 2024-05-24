from datetime import datetime
import pytz


def convert_utc_to_indian(utc_time):
    utc_timezone = pytz.utc
    indian_timezone = pytz.timezone('Asia/Kolkata')

    # Convert UTC time to datetime object
    utc_dt = utc_timezone.localize(utc_time)

    # Convert UTC time to Indian time
    indian_dt = utc_dt.astimezone(indian_timezone)

    return indian_dt


if __name__ == "__main__":
    # Get UTC time
    utc_time = datetime.utcnow()

    print(utc_time)

    # Convert UTC time to Indian time
    indian_time = convert_utc_to_indian(utc_time)

    print("UTC Time:", utc_time)
    print("Indian Time:", indian_time)

