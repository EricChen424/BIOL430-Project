from unittest import TestCase
from csv_parser.GeneCSVParaser import GeneCSVParser
from csv_parser.model.Gene import Gene

class TestGeneCSVParser(TestCase):
    def setUp(self):
        self.parser = GeneCSVParser()

    def test_parse_csv(self):
        genes = self.parser.parse_csv('mock_data/test_gene.csv')
        expected_genes = [
            Gene("AT1G01010", "1", "+", "3818", "5953", "6", "1"),
            Gene("AT1G01010", "1", "+", "3426", "5513", "6", "2"),
            Gene("AT1G01010", "1", "+", "3699", "5834", "6", "3"),
            Gene("AT1G01010", "1", "+", "3746", "5830", "6", "4"),
            Gene("AT1G01010", "1", "+", "3705", "5813", "6", "5")
        ]
        self.assertListEqual(expected_genes, genes)