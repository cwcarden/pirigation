import unittest
import sys
sys.path.append("..")
import weather


class TestWeather(unittest.TestCase):
    
    def test_get_forecast(self):
        result = weather.get_forecast()
        self.assertFalse(result, True)
        
        

if __name__ == '__main__':
    unittest.main()