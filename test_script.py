import unittest
import polars as pl
from main_script import main
from lib import load_data, data_summary

class TestScript(unittest.TestCase):

    def setUp(self):
        self.data_path = "cars.csv"
        self.df = pl.read_csv(self.data_path)

    def test_load_data(self):
        data = load_data(self.data_path)
        self.assertIsNotNone(data)
        self.assertTrue(len(data) > 0)

    def test_data_summary(self):
        summary = data_summary(self.df)
        self.assertIsNotNone(summary)
        self.assertTrue(len(summary) > 0)

    def test_main_function(self):
        main()

if __name__ == '__main__':
    unittest.main()
