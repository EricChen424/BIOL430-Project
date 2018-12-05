library(tidyverse)
library(ggplot2)

gene_mite_data <- read_csv("results/mite_gene_pairs.csv", col_names = TRUE)

#there's only about 5 of these; perhaps want to ask about them
removed_genes_in_mites <- gene_mite_data %>%
  filter(distance >= 0)

overlapping_mite_genes_count <- removed_genes_in_mites %>% 
  filter(distance == 0) %>%
  nrow()

removed_genes_in_mites %>%
  ggplot() +
  geom_histogram(aes(distance), binwidth=150)

#remove all mites without a family or superfamily (it turns out all families have superfamilies in this dataset)
#compute mite and gene length on the smaller dataset
#select useful columns
clean_data <- removed_genes_in_mites %>% 
  filter(!is.na(mite_family) | !is.na(mite_superfamily)) %>%
  mutate(mite_length = mite_end - mite_start) %>%
  mutate(gene_length = gene_end - gene_start) %>%
  select(mite_name, mite_length, mite_family, mite_superfamily, gene_name, gene_length, distance)

#count the number of gene-mites that overlap
overlapping_mite_genes_count_clean_data <- clean_data %>% 
  filter(distance == 0) %>%
  nrow()

#histogram
clean_data %>%
  ggplot() +
  geom_histogram(aes(distance, fill=mite_superfamily), binwidth=150)

#tables
family_stats <- clean_data %>%
  group_by(mite_family, mite_superfamily) %>%
  summarize(mean_distance=mean(distance),median_distance=median(distance),mite_count=n()) %>%
  arrange(mite_family, mite_count)

superfamily_stats <- clean_data %>%
  group_by(mite_superfamily) %>%
  summarize(mean_distance=mean(distance),median_distance=median(distance),mite_count=n()) %>%
  arrange(mite_count)

#box plots
clean_data %>%
  ggplot(aes(x=mite_family, y=distance, color=mite_superfamily)) +
  geom_boxplot(notch=TRUE) + 
  stat_summary(fun.y=mean, geom="point", shape=23, size=3) +
  theme(axis.text.x = element_text(angle = 45,
                                   hjust = 1))

clean_data %>%
  ggplot(aes(x=mite_superfamily, y=distance, color=mite_superfamily)) +
  geom_boxplot(notch=TRUE) + 
  stat_summary(fun.y=mean, geom="point", shape=23, size=3) +
  theme(axis.text.x = element_text(angle = 30,
                                   hjust = 1))
#Kruskal-Wallis
kruskal.test(distance ~ as.factor(mite_family), data=clean_data)
kruskal.test(distance ~ as.factor(mite_superfamily), data=clean_data)
