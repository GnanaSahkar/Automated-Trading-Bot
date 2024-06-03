import csv
import random
from datetime import datetime, timedelta

def generate_historical_data(file_name, num_records=100):
    headers = ["Date", "Open", "High", "Low", "Close", "Volume"]
    with open(file_name, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        current_date = datetime.now()
        for _ in range(num_records):
            writer.writerow({
                "Date": current_date.strftime('%Y-%m-%d'),
                "Open": round(random.uniform(100, 200), 2),
                "High": round(random.uniform(100, 200), 2),
                "Low": round(random.uniform(100, 200), 2),
                "Close": round(random.uniform(100, 200), 2),
                "Volume": random.randint(1000, 10000)
            })
            current_date -= timedelta(days=1)

generate_historical_data('data/historical/sample_historical_data.csv')
