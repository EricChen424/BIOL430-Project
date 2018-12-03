from unittest import TestCase
from pairer.MitePairer import MitePairer
from pairer.model.MiteGenePair import MiteGenePair
from csv_parser.model.Gene import Gene
from csv_parser.model.Mite import Mite

class TestMitePairer(TestCase):
    def setUp(self):
        self.pairer = MitePairer()

    def test_pair_mites_with_genes_positive_strand_(self):
        mite1 = Mite("ABC", "4", "+", "132", "154", "NULL", "AA", "A", "3")
        mite2 = Mite("ABC1", "4", "+", "0", "15", "NULL", "AA", "A", "3")
        mite3 = Mite("ABC2", "4", "+", "190", "200", "NULL", "AA", "A", "3")
        mite4 = Mite("ABC3", "4", "+", "50", "65", "NULL", "AA", "A", "3")

        gene1 = Gene("gABC", "4", "+", "100", "115", "5", "3")
        gene2 = Gene("gBBC", "4", "+", "160", "170", "5", "3")
        mites = [
            mite1,
            mite2,
            mite3
        ]
        genes = [
            gene1,
            gene2
        ]
        pairs = self.pairer.pair_mites_with_genes(mites, genes)
        expected_pairs = [
            MiteGenePair(mite1, gene2),
            MiteGenePair(mite2, gene1),
            MiteGenePair(mite3, gene2),
            MiteGenePair(mite4, gene1)
        ]
        self.assertEqual(pairs, expected_pairs)

    def test_pair_mites_prefers_nested_elements(self):
        #we assume that if a mite is nested in a gene (partially or completely), then it's associated with the gene
        #so we pair the two elements together rather than another gene that's not nested but may be closer
        mite1 = Mite("ABC", "4", "+", "132", "154", "NULL", "AA", "A", "3")

        gene1 = Gene("gABC", "4", "+", "100", "143", "5", "3")
        gene2 = Gene("gBBC", "4", "+", "155", "170", "5", "3")

        mites = [
            mite1
        ]
        genes = [
            gene1,
            gene2
        ]
        pairs = self.pairer.pair_mites_with_genes(mites, genes)
        expected_pairs = [
            MiteGenePair(mite1, gene1)
        ]
        self.assertEqual(pairs, expected_pairs)

    def test_pair_mites_prefers_nested_elements_input_order_doesnt_matter(self):
        #sanity check
        mite1 = Mite("ABC", "4", "+", "132", "154", "NULL", "AA", "A", "3")

        gene1 = Gene("gABC", "4", "+", "100", "143", "5", "3")
        gene2 = Gene("gBBC", "4", "+", "155", "170", "5", "3")

        mites = [
            mite1
        ]
        genes = [
            gene2,
            gene1
        ]
        pairs = self.pairer.pair_mites_with_genes(mites, genes)
        expected_pairs = [
            MiteGenePair(mite1, gene1)
        ]
        self.assertEqual(pairs, expected_pairs)

    def test_pair_mites_uses_correlated_gene_if_provided(self):
        #we assume that correlated_gene was filled for a reason so we ignore our distance heuristic or any other heuristic
        mite1 = Mite("ABC", "4", "+", "132", "154", "ABC", "AA", "A", "3")

        gene1 = Gene("gABC", "4", "+", "0", "10", "5", "3")
        gene2 = Gene("gBBC", "4", "+", "155", "170", "5", "3")
        gene3 = Gene("gCBC", "4", "+", "100", "143", "5", "3")

        mites = [
            mite1
        ]
        genes = [
            gene1,
            gene2,
            gene3
        ]
        pairs = self.pairer.pair_mites_with_genes(mites, genes)
        expected_pairs = [
            MiteGenePair(mite1, gene1)
        ]
        self.assertEqual(pairs, expected_pairs)

    def test_pair_mites_uses_heuristics_if_correlated_not_exist(self):
        #go back to heuristics if we can't find the correlated gene
        mite1 = Mite("ABC", "4", "+", "132", "154", "ABC", "AA", "A", "3")

        gene1 = Gene("gDBC", "4", "+", "0", "10", "5", "3")
        gene2 = Gene("gBBC", "4", "+", "155", "170", "5", "3")
        gene3 = Gene("gCBC", "4", "+", "100", "143", "5", "3")

        mites = [
            mite1
        ]
        genes = [
            gene1,
            gene2,
            gene3
        ]
        pairs = self.pairer.pair_mites_with_genes(mites, genes)
        expected_pairs = [
            MiteGenePair(mite1, gene3)
        ]
        self.assertEqual(pairs, expected_pairs)

    def test_pair_mites_correctly_separates_by_genome_location(self):
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

        mites = [
            mite1,
            mite2,
            mite3,
            mite4,
            mite5,
            mite6,
            mite7,
            mite8
        ]
        genes = [
            gene1,
            gene2,
            gene3,
            gene4,
            gene5,
            gene6,
            gene7,
            gene8
        ]

        pairs = self.pairer.pair_mites_with_genes(mites, genes)
        expected_pairs = [
            MiteGenePair(mite1, gene1),
            MiteGenePair(mite2, gene2),
            MiteGenePair(mite3, gene3),
            MiteGenePair(mite4, gene4),
            MiteGenePair(mite5, gene5),
            MiteGenePair(mite6, gene6),
            MiteGenePair(mite7, gene7),
            MiteGenePair(mite8, gene8)
        ]
        self.assertEqual(pairs, expected_pairs)
