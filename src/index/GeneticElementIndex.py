class GeneticElementIndex:
    def __init__(self):
        pass

    def index_elements(self, elements):
        index = {}

        for element in elements:
            genome = element.genome_id
            chromosome = element.chromosome
            strand = element.strand
            name = element.name

            if genome not in index:
                index[genome] = {}

            genome_idx = index[genome]

            if chromosome not in genome_idx:
                genome_idx[chromosome] = {}

            chromosome_idx = genome_idx[chromosome]

            if strand not in chromosome_idx:
                chromosome_idx[strand] = {}

            strand_idx = chromosome_idx[strand]

            strand_idx[name] = element

        return index
