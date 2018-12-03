from unittest import TestCase
from csv_parser.MiteCSVParser import MiteCSVParser
from csv_parser.model.Mite import Mite

class TestMiteCSVParser(TestCase):
    def setUp(self):
        self.parser = MiteCSVParser()

    def test_parse_csv(self):
        mites = self.parser.parse_csv('mock_data/test_mite.csv')
        expected_mites = [
            Mite("AT1M10", "1", "-", "255103", "255179", "NULL", "Unclassified", "Unclassified", "1"),
            Mite("AT1M10", "1", "-", "253498", "253574", "NULL", "Unclassified", "Unclassified", "2"),
            Mite("AT1M10", "1", "-", "255561", "255637", "NULL", "Unclassified", "Unclassified", "3"),
            Mite("AT1M10", "1", "-", "255321", "255397", "NULL", "Unclassified", "Unclassified", "4"),
            Mite("AT1M10", "1", "-", "255769", "255845", "NULL", "Unclassified", "Unclassified", "5")
        ]
        self.assertListEqual(expected_mites, mites)