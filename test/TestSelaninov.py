import unittest
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from drought_index.Selaninov import selaninov_drought_index

class TestSelaninovDroughtIndex(unittest.TestCase):

    def test_valid_input(self):
        temperature_data = [25, 26, 27, 24, 23, 22, 21, 20, 19, 18, 17, 16]
        precipitation_data = [50, 40, 30, 20, 10, 5, 5, 10, 15, 20, 25, 30]

        result = selaninov_drought_index(temperature_data, precipitation_data)
        expected_result = (
            sum(temperature_data)/len(temperature_data)
            ) / (
                sum(precipitation_data) / len(precipitation_data)
                )

        self.assertAlmostEqual(result, expected_result, places=5, msg="Invalid result")

    def test_invalid_input_length(self):
        temperature_data = [25, 26, 27, 24, 23, 22, 21, 20, 19, 18, 17]
        precipitation_data = [50, 40, 30, 20, 10, 5, 5, 10, 15, 20, 25, 30]

        
        result=selaninov_drought_index(temperature_data, precipitation_data)
        self.assertAlmostEqual(result, None)

    def test_invalid_input_zero_length(self):
        temperature_data = []
        precipitation_data = []

        result=selaninov_drought_index(temperature_data, precipitation_data)
        self.assertAlmostEqual(result, None )

if __name__ == '__main__':
    unittest.main()


