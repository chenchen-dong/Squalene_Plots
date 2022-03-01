library(data.table)
library(textshape)
library(matrixStats)
library(tidyverse)
library(pheatmap)

fread(input = '/Users/dongchen/Downloads/jlm_wrubber_data - jlm_wrubber_data.csv') -> jlm_new
jlm_new %>% 
  select(1:46) %>% 
  column_to_rownames('metabolites') ->heatmap_jlm_new

jlm_new %>% 
  select(1,47) %>% 
  column_to_rownames('metabolites') -> row_annotations_new

png("./heatmap.png")

heatmap_jlm_new %>% 
  pheatmap(annotation_row = row_annotations_new, 
           clustering_distance_cols = 'correlation', 
           clustering_distance_rows = 'correlation', 
           annotation_col = jlm_col_annotation, 
           cutree_cols=3, 
           annotation_colors = list(Tissue=c(stem='#7F6000',leaf="#548235",roots='#BF9000'), 
                                    Genotype=c(EV='#D0DFE6FF',WT='#748AA6FF',J='#6EE2FFFF',L='#F7C530FF',M='#95CC5EFF') ,
                                    pathway=c(MEP='#1B9E77', MVA='#D95F02', PrenylPyrophosphates='#7570B3', resin='#E7298A', rubber='#666666', squalene='#E6AB02')
                                    )
           )

dev.off()


