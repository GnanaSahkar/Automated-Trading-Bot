import os
from utils.data_fetcher import fetch_historical_data
from stratergies.moving_average import MovingAverageStrategy

def main():
    data_path = os.path.join('data', 'historical', 'historical_data.csv')
    data = fetch_historical_data(data_path)

    strategy = MovingAverageStrategy(short_window=40, long_window=100)
    signals = strategy.generate_signals(data)


    print(signals)

if __name__ == "__main__":
    main()
