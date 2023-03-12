import unittest
from main import get_weather, format_output


class TestWeatherApp(unittest.TestCase):
    def test_get_weather_valid_city(self):
        # Test with a valid city name
        city = "London"
        weather_data = get_weather(city)
        self.assertIsInstance(weather_data, dict)
        self.assertNotIn('error', weather_data)
        self.assertIn('location', weather_data)
        self.assertIn('description', weather_data)
        self.assertIn('sunrise_time', weather_data)
        self.assertIn('sunset_time', weather_data)


    def test_format_output_valid_data(self):
        # Test with valid weather data
        weather_data = {
            'location': 'London, GB',
            'description': 'Clear',
            'sunrise_time': '06:08:38',
            'sunset_time': '17:48:17'
        }
        expected_output = "Location: London, GB\n" \
                          "Conditions: Clear\n" \
                          "Sunrise: 06:08:38\n" \
                          "Sunset: 17:48:17"
        output = format_output(weather_data)
        self.assertEqual(output, expected_output)

     def test_format_output_invalid_data(self):
        # Test with invalid weather data (i.e. error message)
        weather_data = {'error': 'Invalid city name'}
        expected_output = "Error: Invalid city name"
        output = format_output(weather_data)
        self.assertEqual(output, expected_output)

if __name__ == "__main__":
    unittest.main()
