import csv_parser.model.CSVModelConstants as CONSTANTS
from csv_parser.model.GeneticElement import GeneticElement

class Mite(GeneticElement):
    def __init__(self, name, chromosome, strand, start, end, correlated_gene, family, superfamily, genome_id):
        GeneticElement.__init__(self, name, chromosome, strand, start, end, genome_id)
        self.correlated_gene = None if correlated_gene == CONSTANTS.null else correlated_gene
        self.family = None if family == CONSTANTS.unclassified else family
        self.superfamily = None if superfamily == CONSTANTS.unclassified else superfamily
        self.type = CONSTANTS.mite_type

    def __eq__(self, other):
        return super(Mite, self).__eq__(other) and self.correlated_gene == other.correlated_gene and self.family == other.family and self.superfamily == other.superfamily and self.type == other.type