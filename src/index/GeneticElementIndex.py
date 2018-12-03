class GeneticElementIndex:
    def __init__(self):
        pass

    def index_elements(self, elements, by_name=True):
        index = {}

        for element in elements:
            genome = element.genome_id
            chromosome = element.chromosome
            name = element.name

            if genome not in index:
                index[genome] = {}

            genome_dict = index[genome]

            if chromosome not in genome_dict:
                genome_dict[chromosome] = {} if by_name else []

            chromosome_dict = genome_dict[chromosome]

            if by_name:
                assert name not in chromosome_dict
                chromosome_dict[name] = element
            else:
                chromosome_dict.append(element)

        return index
