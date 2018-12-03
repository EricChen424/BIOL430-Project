import csv_parser.model.CSVModelConstants as CONSTANTS
from csv_parser.model.GeneticElement import GeneticElement

class Mite(GeneticElement):
    @staticmethod
    def csv_headers():
        return GeneticElement.csv_headers() + ",correlated_gene,family,superfamily"

    def __init__(self, name, chromosome, strand, start, end, correlated_gene, family, superfamily, genome_id):
        GeneticElement.__init__(self, name, chromosome, strand, start, end, genome_id)
        self.correlated_gene = None if correlated_gene == CONSTANTS.null else correlated_gene
        self.family = None if family == CONSTANTS.unclassified else family
        self.superfamily = None if superfamily == CONSTANTS.unclassified else superfamily
        self.type = CONSTANTS.mite_type

    def __eq__(self, other):
        return super(Mite, self).__eq__(other) and self.correlated_gene == other.correlated_gene and self.family == other.family and self.superfamily == other.superfamily and self.type == other.type

    def to_csv_row(self):
        correlated_gene = "" if self.correlated_gene is None else str(self.correlated_gene)
        family = "" if self.family is None else str(self.family)
        superfamily = "" if self.superfamily is None else str(self.superfamily)
        string = super(Mite, self).to_csv_row() + "," + correlated_gene + "," + family + "," + superfamily
        return string