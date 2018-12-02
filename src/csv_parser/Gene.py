class Gene:
    def __init__(self, name, chromosome, strand, start, end, exon_count, genome_id):
        self.name = name
        self.chromosome = chromosome
        self.strand = strand
        self.start = start
        self.end = end
        self.exon_count = exon_count
        self.genome_id = genome_id