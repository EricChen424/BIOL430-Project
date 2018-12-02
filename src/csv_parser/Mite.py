class Mite:
    def __init__(self, name, chromosome, strand, start, end, correlated_gene, family, superfamily, genome_id):
        self.name = name
        self.chromosome = chromosome
        self.strand = strand
        self.start = start
        self.end = end
        self.correlated_gene = correlated_gene
        self.family = family
        self.superfamily = superfamily
        self.genome_id = genome_id