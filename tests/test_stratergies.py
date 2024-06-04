import unittest
import pandas as pd
from stratergies.moving_average import MovingAverageStrategy

class TestMovingAverageStrategy(unittest.TestCase):

    def setUp(self):
        
        self.data = pd.DataFrame({
            'close': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        })
        self.strategy = MovingAverageStrategy(short_window=2, long_window=3)

    def test_generate_signals(self):
        signals = self.strategy.generate_signals(self.data)
        self.assertEqual(len(signals), len(self.data))
        self.assertIn('signal', signals)
        self.assertIn('short_mavg', signals)
        self.assertIn('long_mavg', signals)

if __name__ == '__main__':
    unittest.main()
