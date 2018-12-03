from unittest import TestCase
from pairer.model.MiteGenePair import MiteGenePair
from csv_parser.model.Mite import Mite
from csv_parser.model.Gene import Gene

class TestMiteGenePair(TestCase):
    def testEquals(self):
        mite = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene = Gene("ABC", "4", "+", "132", "154", "5", "3")
        pair1 = MiteGenePair(mite, gene)
        pair2 = MiteGenePair(mite, gene)
        self.assertEqual(pair1, pair2)

    def testNotEquals(self):
        mite1 = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene1 = Gene("ABC", "4", "+", "132", "154", "5", "3")
        mite2 = Mite("ABC", "3", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene2 = Gene("ABC", "4", "+", "132", "154", "5", "3")
        pair1 = MiteGenePair(mite1, gene1)
        pair2 = MiteGenePair(mite2, gene2)
        self.assertNotEqual(pair1, pair2)
