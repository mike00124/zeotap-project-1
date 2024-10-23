import unittest
from src.utils.weather_api import convert_kelvin_to_celsius

class TestWeather(unittest.TestCase):
    def test_temperature_conversion(self):
        kelvin = 300
        celsius = convert_kelvin_to_celsius(kelvin)
        self.assertEqual(round(celsius, 2), 26.85)
