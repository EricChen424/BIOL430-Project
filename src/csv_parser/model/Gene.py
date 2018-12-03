import csv_parser.model.CSVModelConstants as CONSTANTS
from csv_parser.model.GeneticElement import GeneticElement

class Gene(GeneticElement):
    @staticmethod
    def csv_headers():
        return GeneticElement.csv_headers() + ",exon_count"

    def __init__(self, name, chromosome, strand, start, end, exon_count, genome_id):
        GeneticElement.__init__(self, name, chromosome, strand, start, end, genome_id)
        self.exon_count = int(exon_count)
        self.type = CONSTANTS.gene_type

    def __eq__(self, other):
        return super(Gene, self).__eq__(other) and self.exon_count == other.exon_count and self.genome_id == other.genome_id and self.type == other.type

    def to_csv_row(self):
        string = super(Gene, self).to_csv_row() + "," + str(self.exon_count)
        return string