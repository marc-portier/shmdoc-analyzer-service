import unittest
from analyze.analyzer import analyze_file


class TestXML(unittest.TestCase):

    def test_basic(self):
        result = analyze_file('tests/data/basic.xml','xml')
        self.assertTrue(result is not None)
        # todo add more assertions


    # todo add more tests