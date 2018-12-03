class MiteGenePair:
    def __init__(self, mite, gene):
        self.mite = mite
        self.gene = gene

    def __eq__(self, other):
        return self.mite == other.mite and self.gene == other.gene