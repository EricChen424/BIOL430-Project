from csv_parser.model.Mite import Mite
from csv_parser.model.Gene import Gene

class MiteGenePair:
    @staticmethod
    def csv_headers():
        return Mite.csv_headers() + "," + Gene.csv_headers() + ",distance"

    def __init__(self, mite, gene):
        self.mite = mite
        self.gene = gene

    def __eq__(self, other):
        return self.mite == other.mite and self.gene == other.gene

    def _gene_to_right(self):
        return self.gene.start < self.mite.start and self.gene.end < self.mite.start

    def _is_mite_in_gene(self):
        return (self.mite.start <= self.gene.end and self.mite.start >= self.gene.start) or (
                self.mite.end <= self.gene.end and self.mite.end >= self.gene.start)

    def to_csv_row(self):
        if self._is_mite_in_gene():
            distance = 0
        elif self._gene_to_right():
            distance = self.mite.start - self.gene.end
        else:
            distance = self.gene.start - self.mite.end

        csv_string = self.mite.to_csv_row() + "," + self.gene.to_csv_row() + "," + str(distance)
        return csv_string

