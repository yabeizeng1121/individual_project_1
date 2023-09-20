import unittest
import pandas as pd
from script import main
from lib import load_data, data_summary

class TestScript(unittest.TestCase):

    def setUp(self):
        self.data_path = "cars.csv"
        self.df = pd.read_csv(self.data_path, sep=';')


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
