library(tidyverse)
library(ggplot2)

gene_mite_data <- read_csv("results/mite_gene_pairs.csv", col_names = TRUE)

#remove all mites without a family or superfamily (it turns out all families have superfamilies in this dataset)
#compute mite and gene length on the smaller dataset
#select useful columns
clean_data <- gene_mite_data %>% 
  filter(!is.na(mite_family) | !is.na(mite_superfamily)) %>%
  mutate(mite_length = mite_end - mite_start) %>%
  mutate(gene_length = gene_end - gene_start) %>%
  select(mite_name, mite_length, mite_family, mite_superfamily, gene_name, gene_length, distance)
