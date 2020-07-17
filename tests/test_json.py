import unittest
from analyze.analyzer import analyze_file


class TestJSON(unittest.TestCase):

    def test_basic(self):
        result = analyze_file('tests/data/basic.json', 'json')
        self.assertTrue(result is not None)
        # todo add more assertions


    # todo add more tests