import unittest
from analyze.analyzer import analyze_file


class TestCSV(unittest.TestCase):

    def test_basic(self):
        result = analyze_file('tests/data/basic.csv','csv')
        self.assertTrue(result is not None)
        #todo add more assertions


    #todo add more tests