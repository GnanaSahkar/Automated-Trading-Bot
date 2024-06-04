import pandas as pd
import numpy as np
#generating signals for Trading
class MovingAverageStrategy:
    def __init__(self, short_window=40, long_window=100):
        self.short_window = short_window
        self.long_window = long_window
    
    def generate_signals(self, data):
        if 'close' not in data.columns:
            raise ValueError("Column 'close' not found in the data")

        signals = pd.DataFrame(index=data.index)
        signals['signal'] = 0.0

        # Create short simple moving average
        signals['short_mavg'] = data['close'].rolling(window=self.short_window, min_periods=1, center=False).mean()

        # Create long simple moving average
        signals['long_mavg'] = data['close'].rolling(window=self.long_window, min_periods=1, center=False).mean()

        # Generate signals
        signals['signal'][self.short_window:] = np.where(signals['short_mavg'][self.short_window:] > signals['long_mavg'][self.short_window:], 1.0, 0.0)   

        # Generate trading orders
        signals['positions'] = signals['signal'].diff()

        return signals
