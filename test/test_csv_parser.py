from unittest import TestCase
from csv_parser.CSVParser import CSVParser

class TestCSVParser(TestCase):
    def setUp(self):
        self.parser = CSVParser()

    def test_parse_csv(self):
        csv = self.parser.parse_csv('mock_data/test_gene.csv')
        expected_headers = ['name','chromosome','strand','start','end','exon_count','genome_id']
        expected_data = [
            ['AT1G01010', '1', '+', '3818', '5953', '6', '1'],
            ['AT1G01010', '1', '+', '3426', '5513', '6', '2'],
            ['AT1G01010', '1', '+', '3699', '5834', '6', '3'],
            ['AT1G01010', '1', '+', '3746', '5830', '6', '4'],
            ['AT1G01010', '1', '+', '3705', '5813', '6', '5']
        ]
        self.assertListEqual(expected_headers, csv.headers)
        self.assertListEqual(expected_data, csv.data)

    def test_parse_csv_no_headers(self):
        csv = self.parser.parse_csv('mock_data/test_gene.csv', has_headers=False)
        expected_headers = []
        expected_data = [
            ['name', 'chromosome', 'strand', 'start', 'end', 'exon_count', 'genome_id'],
            ['AT1G01010', '1', '+', '3818', '5953', '6', '1'],
            ['AT1G01010', '1', '+', '3426', '5513', '6', '2'],
            ['AT1G01010', '1', '+', '3699', '5834', '6', '3'],
            ['AT1G01010', '1', '+', '3746', '5830', '6', '4'],
            ['AT1G01010', '1', '+', '3705', '5813', '6', '5']
        ]
        self.assertListEqual(expected_headers, csv.headers)
        self.assertListEqual(expected_data, csv.data)
