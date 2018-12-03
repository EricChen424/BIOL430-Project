library(tidyverse)
library(ggplot2)

gene_mite_data <- read_csv("results/mite_gene_pairs.csv", col_names = TRUE)

gene_mite_data %>% 
  View()
