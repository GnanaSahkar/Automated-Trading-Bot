# utils/load_historical_data.py

import os
import pandas as pd

def load_historical_data(file_name):
    """
    Load historical data from a CSV file.

    :param file_name: str, the name of the CSV file
    :return: DataFrame, the historical data
    """
    file_path = os.path.join('data', 'historical', file_name)
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"File {file_name} not found in historical data directory.")

# Example usage
if __name__ == "__main__":
    historical_data = load_historical_data('historical_data.csv')
    print(historical_data.head())
