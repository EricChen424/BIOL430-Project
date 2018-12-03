import sys
sys.path.append('../')

import time

from csv_parser.GeneCSVParser import GeneCSVParser
from csv_parser.MiteCSVParser import MiteCSVParser
from pairer.MitePairer import MitePairer
from pairer.model.MiteGenePair import MiteGenePair

def main():
    mites_path = "../../data/all_mites.csv"
    genes_path = "../../data/all_genes.csv"

    mites_parser = MiteCSVParser()
    genes_parser = GeneCSVParser()
    pairer = MitePairer()

    start_time = time.time()
    mites = mites_parser.parse_csv(mites_path)
    end_time = time.time()
    print("Mite CSV parsing took " + str(end_time - start_time) + "s")

    start_time = time.time()
    genes = genes_parser.parse_csv(genes_path)
    end_time = time.time()
    print("Gene CSV parsing took " + str(end_time - start_time) + "s")

    start_time = time.time()
    pairs = pairer.pair_mites_with_genes(mites, genes)
    end_time = time.time()
    print("Finding mite-gene pairs took " + str(end_time - start_time) + "s")

    start_time = time.time()
    output_path = "../../results/mite_gene_pairs.csv"
    output_file = open(output_path, mode="w+")
    output_file.write(MiteGenePair.csv_headers() + "\n")

    for pair in pairs:
        output_file.write(pair.to_csv_row() + "\n")

    output_file.close()

    end_time = time.time()
    print("Writing mite-gene pairs took " + str(end_time - start_time) + "s")


if __name__ == "__main__":
    main()