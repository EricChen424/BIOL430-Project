class GeneticElement:
    def __init__(self, name, chromosome, strand, start, end, genome_id):
        self.name = name
        self.chromosome = int(chromosome)
        self.strand = strand
        self.start = int(start)
        self.end = int(end)
        self.genome_id = int(genome_id)

    def __eq__(self, other):
        return self.name == other.name and self.chromosome == other.chromosome and self.strand == other.strand and self.start == other.start and self.end == other.end and self.genome_id == other.genome_id