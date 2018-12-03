from unittest import TestCase
from csv_parser.model.Gene import Gene

class TestGene(TestCase):
    def testConstructor(self):
        gene = Gene("ABC", "4", "+", "132", "154", "5", "3")
        self.assertEqual(gene.name, "ABC")
        self.assertEqual(gene.chromosome, 4)
        self.assertEqual(gene.strand, "+")
        self.assertEqual(gene.start, 132)
        self.assertEqual(gene.end, 154)
        self.assertEqual(gene.exon_count, 5)
        self.assertEqual(gene.genome_id, 3)

    def testEquals(self):
        gene1 = Gene("ABC", "4", "+", "132", "154", "5", "3")
        gene2 = Gene("ABC", "4", "+", "132", "154", "5", "3")
        self.assertEqual(gene1, gene2)

    def testNotEquals(self):
        gene1 = Gene("ABC", "4", "+", "132", "154", "5", "3")
        gene2 = Gene("A", "4", "+", "132", "154", "5", "3")
        gene3 = Gene("ABC", "3", "+", "132", "154", "5", "3")
        gene4 = Gene("ABC", "4", "-", "132", "154", "5", "3")
        gene5 = Gene("ABC", "4", "+", "1", "154", "5", "3")
        gene6 = Gene("ABC", "4", "+", "132", "1", "5", "3")
        gene7 = Gene("ABC", "4", "+", "132", "154", "1", "3")
        gene8 = Gene("ABC", "4", "+", "132", "154", "5", "1")
        self.assertNotEqual(gene1, gene2)
        self.assertNotEqual(gene1, gene3)
        self.assertNotEqual(gene1, gene4)
        self.assertNotEqual(gene1, gene5)
        self.assertNotEqual(gene1, gene6)
        self.assertNotEqual(gene1, gene7)
        self.assertNotEqual(gene1, gene8)

    def testToRow(self):
        gene = Gene("ABC", "4", "+", "132", "154", "5", "3")
        csv_row_string = gene.to_csv_row()
        expected_string = "ABC,4,+,132,154,3,5"
        self.assertEqual(expected_string, csv_row_string)

    def testHeaders(self):
        headers = Gene.csv_headers()
        expected_string = "gene_name,gene_chromosome,gene_strand,gene_start,gene_end,gene_genome_id,gene_exon_count"
        self.assertEqual(expected_string, headers)