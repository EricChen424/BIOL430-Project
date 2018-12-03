from unittest import TestCase
from csv_parser.model.Mite import Mite

class TestMite(TestCase):
    def testConstructor(self):
        mite = Mite("ABC", "4", "+", "132", "154", "gene1", "AA", "A", "3")
        self.assertEqual(mite.name, "ABC")
        self.assertEqual(mite.chromosome, 4)
        self.assertEqual(mite.strand, "+")
        self.assertEqual(mite.start, 132)
        self.assertEqual(mite.end, 154)
        self.assertEqual(mite.correlated_gene, "gene1")
        self.assertEqual(mite.family, "AA")
        self.assertEqual(mite.superfamily, "A")
        self.assertEqual(mite.genome_id, 3)

    def testConstructorUnknownValues(self):
        mite = Mite("ABC", "4", "+", "132", "154", "NULL", "Unclassified", "Unclassified", "3")
        self.assertEqual(mite.name, "ABC")
        self.assertEqual(mite.chromosome, 4)
        self.assertEqual(mite.strand, "+")
        self.assertEqual(mite.start, 132)
        self.assertEqual(mite.end, 154)
        self.assertEqual(mite.correlated_gene, None)
        self.assertEqual(mite.family, None)
        self.assertEqual(mite.superfamily, None)
        self.assertEqual(mite.genome_id, 3)

    def testEquals(self):
        mite1 = Mite("ABC", "4", "+", "132", "154", "gene1", "AA", "A", "3")
        mite2 = Mite("ABC", "4", "+", "132", "154", "gene1", "AA", "A", "3")
        self.assertEqual(mite1, mite2)

    def testNotEquals(self):
        mite1 = Mite("ABC", "4", "+", "132", "154", "gene1", "AA", "A", "3")
        mite2 = Mite("A", "4", "+", "132", "154", "gene1", "AA", "A", "3")
        mite3 = Mite("ABC", "1", "+", "132", "154", "gene1", "AA", "A", "3")
        mite4 = Mite("ABC", "4", "-", "132", "154", "gene1", "AA", "A", "3")
        mite5 = Mite("ABC", "4", "+", "1", "154", "gene1", "AA", "A", "3")
        mite6 = Mite("ABC", "4", "+", "132", "1", "gene1", "AA", "A", "3")
        mite7 = Mite("ABC", "4", "+", "132", "154", "gene2", "AA", "A", "3")
        mite8 = Mite("ABC", "4", "+", "132", "154", "gene1", "BB", "A", "3")
        mite9 = Mite("ABC", "4", "+", "132", "154", "gene1", "AA", "B", "3")
        mite10 = Mite("ABC", "4", "+", "132", "154", "gene1", "AA", "B", "1")
        self.assertNotEqual(mite1, mite2)
        self.assertNotEqual(mite1, mite3)
        self.assertNotEqual(mite1, mite4)
        self.assertNotEqual(mite1, mite5)
        self.assertNotEqual(mite1, mite6)
        self.assertNotEqual(mite1, mite7)
        self.assertNotEqual(mite1, mite8)
        self.assertNotEqual(mite1, mite9)
        self.assertNotEqual(mite1, mite10)
