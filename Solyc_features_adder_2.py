import sys
import os

wd = os.getcwd()
print('Reading dictionaries...')

input_Description_file = wd + '/dic_files/Solyc_Description.csv'
input_Description = open(input_Description_file, 'r', encoding="utf-8")
dic_description = {}
for line in input_Description:
	line_list = list(line.split('\t'))
	dic_description[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_entrez_file = wd + '/dic_files/Solyc_entrez.csv'
input_entrez = open(input_entrez_file, 'r', encoding="utf-8")
dic_entrez = {}
for line in input_entrez:
	line_list = list(line.split('\t'))
	dic_entrez[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_UniProt_file = wd + '/dic_files/Solyc_UniProt.csv'
input_UniProt = open(input_UniProt_file, 'r', encoding="utf-8")
dic_UniProt = {}
for line in input_UniProt:
	line_list = list(line.split('\t'))
	dic_UniProt[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_unigene_file = wd + '/dic_files/Solyc_unigene.csv'
input_unigene = open(input_unigene_file, 'r', encoding="utf-8")
dic_unigene = {}
for line in input_unigene:
	line_list = list(line.split('\t'))
	dic_unigene[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_GO_file = wd + '/dic_files/ITAG3.2_protein_go.tsv'
input_GO = open(input_GO_file, 'r', encoding="utf-8")
dic_GO = {}
for line in input_GO:
	line_list = list(line.split('\t'))
	dic_GO[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_bin_file = wd + '/dic_files/Solyc_MapMan_bin.csv'
input_MapMan_bin = open(input_MapMan_bin_file, 'r', encoding="utf-8")
dic_MapMan_bin = {}
for line in input_MapMan_bin:
	line_list = list(line.split('\t'))
	dic_MapMan_bin[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_name_file = wd + '/dic_files/Solyc_MapMan_name.csv'
input_MapMan_name = open(input_MapMan_name_file, 'r', encoding="utf-8")
dic_MapMan_name = {}
for line in input_MapMan_name:
	line_list = list(line.split('\t'))
	dic_MapMan_name[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_NCBI_file = wd + '/dic_files/Solyc_NCBI.csv'
input_NCBI = open(input_NCBI_file, 'r', encoding="utf-8")
dic_NCBI = {}
for line in input_NCBI:
	line_list = list(line.split('\t'))
	dic_NCBI[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_ortho_file = wd + '/dic_files/Solyc_arthal_orthologs.csv'
input_ortho = open(input_ortho_file, 'r', encoding="utf-8")
dic_ortho = {}
for line in input_ortho:
	line_list = list(line.split('\t'))
	dic_ortho[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_directory = wd + '/Input'
for currentpath, folders, files in os.walk(input_directory):
	for file in files:
		input_DE_file = input_directory + '/' + file
		input_DE = open(input_DE_file, 'r', encoding="utf-7")

		input_DE_file_name_path = input_DE_file.split('/')
		input_DE_file_name_extension = input_DE_file_name_path[-1].split('.')
		input_DE_file_name = input_DE_file_name_extension[0]
		print("adding features to " + input_DE_file_name_path[-1])
		output_file=wd + '/Output/' + input_DE_file_name + "_features_added.csv"
		output=open(output_file, 'w')

		for line in input_DE:
			if line.startswith('Solyc'):
				Description = ''
				entrez = ''
				UniProt = ''
				unigene = ''
				GO = ''
				MapMan_bin = ''
				MapMan_name = ''
				NCBI = ''
				ortho_ID = ''


				line_list=list(line.split(';'))
				Solyc=line_list[0]
				
				if Solyc in dic_description.keys():
					Description = dic_description[Solyc]
				if Solyc in dic_entrez.keys():
					entrez = dic_entrez[Solyc]
				if Solyc in dic_UniProt.keys():
					UniProt = dic_UniProt[Solyc]
				if Solyc in dic_unigene.keys():
					unigene = dic_unigene[Solyc]
				if Solyc in dic_GO.keys():
					GO = dic_GO[Solyc]
				if Solyc in dic_MapMan_bin.keys():
					MapMan_bin = dic_MapMan_bin[Solyc]
				if Solyc in dic_MapMan_name.keys():
					MapMan_name = dic_MapMan_name[Solyc]
				if Solyc in dic_NCBI.keys():
					NCBI = dic_NCBI[Solyc]	
				if Solyc in dic_ortho.keys():
					ortho_ID = dic_ortho[Solyc]

				output.write(Solyc+'\t'+line_list[1]+'\t'+line_list[2]+'\t'+line_list[3]+'\t'+line_list[4].rstrip('\n')+'\t'+Description+'\t'+entrez+'\t'+UniProt+'\t'+unigene+'\t'+GO+'\t'+MapMan_bin+'\t'+MapMan_name+'\t'+NCBI+'\t'+ortho_ID+'\n')
			else:
				output.write('gene'+'\t'+'logFC'+'\t'+'logCPM'+'\t'+'PValue'+'\t'+'FDR'+'\t'+'Description'+'\t'+'entrez'+'\t'+'Uniprot'+'\t'+'unigeme'+'\t'+'GO_Term'+'\t'+'MapMan_bin'+'\t'+'MapMan_name'+'\t'+'NCBI'+'\t'+'A._thaliana_ortholog'+'\n')