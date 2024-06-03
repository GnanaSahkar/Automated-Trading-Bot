import json
import random
from datetime import datetime

def generate_realtime_data(file_name):
    data = {
        "Symbol": "XYZ",
        "Timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "Price": round(random.uniform(100, 200), 2),
        "Volume": random.randint(1000, 10000),
        "MarketCap": round(random.uniform(1000000, 10000000), 2)
    }
    with open(file_name, 'w') as jsonfile:
        json.dump(data, jsonfile)

generate_realtime_data('data/realtime/sample_realtime_data.json')
