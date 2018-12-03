from csv_parser.CSVParser import CSVParser
from csv_parser.model.Gene import Gene

class GeneCSVParser(CSVParser):
    def __init__(self):
        CSVParser.__init__(self)

    def parse_csv(self, path):
        csv = super(GeneCSVParser, self).parse_csv(path, has_headers=True)

        name = 0
        chromosome = 1
        strand = 2
        start = 3
        end = 4
        exon_count = 5
        genome_id = 6

        genes = []
        for row in csv.data:
            gene = Gene(row[name], row[chromosome], row[strand], row[start], row[end], row[exon_count], row[genome_id])
            genes.append(gene)

        return genes