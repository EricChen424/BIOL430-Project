from unittest import TestCase
from csv_parser.model.Gene import Gene
from csv_parser.model.Mite import Mite
from index.GeneticElementIndex import GeneticElementIndex

class TestGeneticElementIndex(TestCase):
    def setUp(self):
        self.indexer = GeneticElementIndex()

    def test_index_elements(self):
        mite1 = Mite("ABC1", "1", "+", "1", "10", "NULL", "AA", "A", "1")
        mite2 = Mite("ABC2", "1", "-", "11", "20", "NULL", "AA", "A", "1")
        mite3 = Mite("ABC3", "2", "+", "21", "30", "NULL", "AA", "A", "1")
        mite4 = Mite("ABC4", "2", "-", "31", "40", "NULL", "AA", "A", "1")
        mite5 = Mite("ABC5", "1", "+", "41", "50", "NULL", "AA", "A", "2")
        mite6 = Mite("ABC6", "1", "-", "51", "60", "NULL", "AA", "A", "2")
        mite7 = Mite("ABC7", "2", "+", "61", "70", "NULL", "AA", "A", "2")
        mite8 = Mite("ABC8", "2", "-", "71", "80", "NULL", "AA", "A", "2")
        gene1 = Gene("gABC1", "1", "+", "76", "85", "5", "1")
        gene2 = Gene("gABC2", "1", "-", "5", "15", "5", "1")
        gene3 = Gene("gABC3", "2", "+", "16", "25", "5", "1")
        gene4 = Gene("gABC4", "2", "-", "26", "35", "5", "1")
        gene5 = Gene("gABC5", "1", "+", "36", "45", "5", "2")
        gene6 = Gene("gABC6", "1", "-", "46", "55", "5", "2")
        gene7 = Gene("gABC7", "2", "+", "56", "65", "5", "2")
        gene8 = Gene("gABC8", "2", "-", "66", "75", "5", "2")

        elements = [
            mite1,
            mite2,
            mite3,
            mite4,
            gene5,
            gene6,
            gene7,
            gene8,
            gene1,
            gene2,
            gene3,
            gene4,
            mite5,
            mite6,
            mite7,
            mite8
        ]

        expected_index = {
            1: {
                1: {
                    "+": {
                        "ABC1": mite1,
                        "gABC1": gene1
                    },
                    "-": {
                        "ABC2": mite2,
                        "gABC2": gene2
                    }
                },
                2: {
                    "+": {
                        "ABC3": mite3,
                        "gABC3": gene3
                    },
                    "-": {
                        "ABC4": mite4,
                        "gABC4": gene4
                    }
                }
            },
            2: {
                1: {
                    "+": {
                        "ABC5": mite5,
                        "gABC5": gene5
                    },
                    "-": {
                        "ABC6": mite6,
                        "gABC6": gene6
                    }
                },
                2: {
                    "+": {
                        "ABC7": mite7,
                        "gABC7": gene7
                    },
                    "-": {
                        "ABC8": mite8,
                        "gABC8": gene8
                    }
                }
            }
        }

        index = self.indexer.index_elements(elements)
        self.assertEqual(expected_index, index)
