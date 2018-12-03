from unittest import TestCase
from pairer.model.MiteGenePair import MiteGenePair
from csv_parser.model.Mite import Mite
from csv_parser.model.Gene import Gene

class TestMiteGenePair(TestCase):
    def testEquals(self):
        mite = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene = Gene("gABC", "4", "+", "132", "154", "5", "3")
        pair1 = MiteGenePair(mite, gene)
        pair2 = MiteGenePair(mite, gene)
        self.assertEqual(pair1, pair2)

    def testNotEquals(self):
        mite1 = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene1 = Gene("gABC", "4", "+", "132", "154", "5", "3")
        mite2 = Mite("ABC", "3", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene2 = Gene("gABC", "4", "+", "132", "154", "5", "3")
        pair1 = MiteGenePair(mite1, gene1)
        pair2 = MiteGenePair(mite2, gene2)
        self.assertNotEqual(pair1, pair2)

    def testToRowLeftOfGene(self):
        mite = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene = Gene("gABC", "4", "+", "120", "125", "5", "3")
        pair = MiteGenePair(mite, gene)
        csv_row_string = pair.to_csv_row()
        expected_string = "ABC,4,+,132,154,3,,,,gABC,4,+,120,125,3,5,7"
        self.assertEqual(expected_string, csv_row_string)

    def testToRowRightOfGene(self):
        mite = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene = Gene("gABC", "4", "+", "160", "170", "5", "3")
        pair = MiteGenePair(mite, gene)
        csv_row_string = pair.to_csv_row()
        expected_string = "ABC,4,+,132,154,3,,,,gABC,4,+,160,170,3,5,6"
        self.assertEqual(expected_string, csv_row_string)

    def testToRowInsideGene(self):
        mite = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        gene = Gene("gABC", "4", "+", "153", "160", "5", "3")
        pair = MiteGenePair(mite, gene)
        csv_row_string = pair.to_csv_row()
        expected_string = "ABC,4,+,132,154,3,,,,gABC,4,+,153,160,3,5,0"
        self.assertEqual(expected_string, csv_row_string)

    def testHeaders(self):
        headers = MiteGenePair.csv_headers()
        expected_string = "name,chromosome,strand,start,end,genome_id,correlated_gene,family,superfamily,name,chromosome,strand,start,end,genome_id,exon_count,distance"
        self.assertEqual(expected_string, headers)
