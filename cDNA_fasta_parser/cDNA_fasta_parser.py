#! /usr/bin/env python3
import sys
import re

input_fasta_file = sys.argv[1]
input_fasta = open(input_fasta_file, 'r', encoding = "utf-8")

input_fasta_file_name = input_fasta_file.split('.')
output_name = input_fasta_file_name[0]+"_Solyc_Description_UniProt"+".csv"
output = open(output_name, 'w')

for line in input_fasta:
	if line.startswith('>Solyc') and re.search("AHRD", line): #lines starting with >Solyc
		line_list = list(line.split(' ')) #list of contents of that line divided by space
		Solyc = line_list[0].lstrip('\>') #list of first columm with Solyc name.
		UniProt = line_list[-1].rstrip("\)\n")
		line_list.pop(0) #removing garbage around the uniprot ID
		line_list.pop(-1) #same here
		line_list.pop(-1) #same here
		line_list.pop(-1) #same here
		line_list.pop(-1) #same here
		Description = ' '.join(line_list)
		output.write(Solyc + '\t' + Description + '\t' + UniProt + '\n')
		#print(Solyc + '\t' + Description + '\t' + UniProt)
	elif line.startswith('>Solyc') and not re.search("AHRD", line): #lines starting with >Solyc
		line_list = list(line.split(' '))
		Solyc = line_list[0].lstrip('\>') #list of first columm with Solyc name.
		line_list.pop(0)
		Description = ' '.join(line_list).rstrip("\n")
		output.write(Solyc + '\t' + Description + '\t' + '' + '\n')
		#print(Solyc + '\t' + Description + '\t' + '')

		
