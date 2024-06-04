import requests
import pandas as pd

def fetch_historical_data(filepath):
    return pd.read_csv(filepath)

def fetch_realtime_data(api_key, symbol):
    base_url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_INTRADAY",
        "symbol": symbol,
        "interval": "1min",
        "apikey": api_key
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if "Time Series (1min)" in data:
        time_series = data["Time Series (1min)"]
        df = pd.DataFrame.from_dict(time_series, orient="index")
        df = df.rename(columns={
            "1. open": "open",
            "2. high": "high",
            "3. low": "low",
            "4. close": "close",
            "5. volume": "volume"
        })
        df.index = pd.to_datetime(df.index)
        df = df.astype(float)
        return df
    else:
        raise ValueError("Error fetching real-time data: {}".format(data.get("Note", "Unknown error")))


if __name__ == "__main__":
    API_KEY = "S4222ALIZVA8QY52"
    SYMBOL = "AAPL"
    df = fetch_realtime_data(API_KEY, SYMBOL)
    print(df.head())
