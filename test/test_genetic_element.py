from unittest import TestCase
from csv_parser.model.GeneticElement import GeneticElement

class TestGeneticElement(TestCase):
    def testConstructor(self):
        element = GeneticElement("ABC", "4", "+", "132", "154", "3")
        self.assertEqual(element.name, "ABC")
        self.assertEqual(element.chromosome, 4)
        self.assertEqual(element.strand, "+")
        self.assertEqual(element.start, 132)
        self.assertEqual(element.end, 154)
        self.assertEqual(element.genome_id, 3)

    def testEquals(self):
        element1 = GeneticElement("ABC", "4", "+", "132", "154", "3")
        element2 = GeneticElement("ABC", "4", "+", "132", "154", "3")
        self.assertEqual(element1, element2)

    def testNotEquals(self):
        element1 = GeneticElement("ABC", "4", "+", "132", "154", "3")
        element2 = GeneticElement("A", "4", "+", "132", "154", "3")
        element3 = GeneticElement("ABC", "3", "+", "132", "154", "3")
        element4 = GeneticElement("ABC", "4", "-", "132", "154", "3")
        element5 = GeneticElement("ABC", "4", "+", "1", "154", "3")
        element6 = GeneticElement("ABC", "4", "+", "132", "1", "3")
        element7 = GeneticElement("ABC", "4", "+", "132", "154", "1")
        self.assertNotEqual(element1, element2)
        self.assertNotEqual(element1, element3)
        self.assertNotEqual(element1, element4)
        self.assertNotEqual(element1, element5)
        self.assertNotEqual(element1, element6)
        self.assertNotEqual(element1, element7)

