from csv_parser.CSVParser import CSVParser
from csv_parser.model.Mite import Mite

class MiteCSVParser(CSVParser):
    def __init__(self):
        CSVParser.__init__(self)

    def parse_csv(self, path):
        csv = super(MiteCSVParser, self).parse_csv(path, has_headers=True)

        name = 0
        chromosome = 1
        strand = 2
        start = 3
        end = 4
        correlated_gene = 5
        family = 10
        superfamily = 11
        genome_id = 13

        mites = []
        for row in csv.data:
            mite = Mite(row[name], row[chromosome], row[strand], row[start], row[end], row[correlated_gene], row[family], row[superfamily], row[genome_id])
            mites.append(mite)

        return mites