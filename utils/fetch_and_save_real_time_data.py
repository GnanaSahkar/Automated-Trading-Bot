# utils/fetch_and_save_realtime_data.py

import os
import json
from utils import fetch_realtime_data

def save_realtime_data(data, file_name):
    """
    Save real-time data to a JSON file.

    :param data: dict, the real-time data
    :param file_name: str, the name of the JSON file
    """
    file_path = os.path.join('data', 'real-time', file_name)
    with open(file_path, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    api_endpoint = "https://api.example.com/realtime-data"
    api_key = "S4222ALIZVA8QY52"
    data = fetch_realtime_data(api_endpoint, api_key)
    save_realtime_data(data, 'sample_realtime_data.json')
    print(f"Real-time data saved to 'data/real-time/sample_realtime_data.json'")
