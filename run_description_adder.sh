#!/usr/bin/bash
for file in *DE*
do
  python3 Solyc_features_adder.py "$file" ITAG3.2_loci_gene_descriptions_from_cDNA.csv Solyc_shortname.csv ITAG3_Solyc_Description_UniProt.csv Solyc_entrez.csv ITAG3.2_protein_go.tsv
done
