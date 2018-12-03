from pairer.model.MiteGenePair import MiteGenePair
from index.GeneticElementIndex import GeneticElementIndex
import csv_parser.model.CSVModelConstants as CONSTANTS

class MitePairer:
    def __init__(self):
        pass

    def _nearest_gene_left_of_idx(self, elements, idx):
        curr_idx = idx - 1
        while curr_idx >= 0:
            element = elements[curr_idx]
            if element.type == CONSTANTS.gene_type:
                return element
            curr_idx -= 1

        return None

    def _nearest_gene_right_of_idx(self, elements, idx):
        length = len(elements)
        curr_idx = idx + 1
        while curr_idx < length:
            element = elements[curr_idx]
            if element.type == CONSTANTS.gene_type:
                return element
            curr_idx += 1

        return None

    def _is_contained_in(self, gene, mite):
        return mite.start <= gene.end or mite.start >= gene.start or mite.end <= gene.end or mite.end >= gene.start

    def _get_closest_mite_gene_pair(self, elements, mite, idx):
        left_gene = self._nearest_gene_left_of_idx(elements, idx)
        right_gene = self._nearest_gene_right_of_idx(elements, idx)

        if left_gene is not None and right_gene is None:
            pair = MiteGenePair(mite, left_gene)
        elif left_gene is None and right_gene is not None:
            pair = MiteGenePair(mite, right_gene)
        elif left_gene is not None and right_gene is not None:
            if self._is_contained_in(left_gene, mite):
                pair = MiteGenePair(mite, left_gene)
            elif self._is_contained_in(right_gene, mite):
                pair = MiteGenePair(mite, right_gene)
            else:
                left_distance = mite.start - left_gene.end
                right_distance = right_gene.start - mite.end
                if left_distance < right_distance:
                    pair = MiteGenePair(mite, left_gene)
                else:
                    pair = MiteGenePair(mite, right_gene)
        else:
            pair = None
        return pair

    def pair_mites_with_genes(self, mites, genes):
        pairs = []
        indexer = GeneticElementIndex()
        all_elements = mites + genes
        index = indexer.index_elements(all_elements, by_name=True)
        indexed_list = indexer.index_elements(all_elements, by_name=False)

        for genome_key in indexed_list:
            genome = indexed_list[genome_key]
            for chromosome_key in genome:
                chromosome = genome[chromosome_key]
                for strand_key in chromosome:
                    elements = chromosome[strand_key].copy()
                    elements.sort(key=lambda e : e.start)
                    for idx in range(len(elements)):
                        element = elements[idx]
                        if element.type != CONSTANTS.mite_type:
                            continue

                        correlated_gene_id = element.correlated_gene
                        if correlated_gene_id is not None:
                            correlated_gene = index[genome_key][chromosome_key][strand_key][correlated_gene_id]
                            if correlated_gene is not None:
                                pair = MiteGenePair(element, correlated_gene)
                                pairs.append(pair)
                                continue

                        pair = self._get_closest_mite_gene_pair(elements, element, idx)

                        if pair is not None:
                            pairs.append(pair)

        return pairs
