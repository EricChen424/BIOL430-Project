import csv_parser.model.CSVModelConstants as CONSTANTS
from csv_parser.model.GeneticElement import GeneticElement

class Gene(GeneticElement):
    def __init__(self, name, chromosome, strand, start, end, exon_count, genome_id):
        GeneticElement.__init__(self, name, chromosome, strand, start, end, genome_id)
        self.exon_count = int(exon_count)
        self.type = CONSTANTS.gene_type

    def __eq__(self, other):
        return super(Gene, self).__eq__(other) and self.exon_count == other.exon_count and self.genome_id == other.genome_id and self.type == other.type