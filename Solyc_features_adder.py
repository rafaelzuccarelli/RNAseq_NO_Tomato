import sys


input_Description_file=sys.argv[2]
input_Description=open(input_Description_file, 'r', encoding="utf-8")
dic_description = {}
for line in input_Description:
	line_list=list(line.split('\t'))
	dic_description[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_entrez_file=sys.argv[3]
input_entrez=open(input_entrez_file, 'r', encoding="utf-8")
dic_entrez = {}
for line in input_entrez:
	line_list=list(line.split('\t'))
	dic_entrez[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_UniProt_file=sys.argv[4]
input_UniProt=open(input_UniProt_file, 'r', encoding="utf-8")
dic_UniProt = {}
for line in input_UniProt:
	line_list=list(line.split('\t'))
	dic_UniProt[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_unigene_file=sys.argv[5]
input_unigene=open(input_unigene_file, 'r', encoding="utf-8")
dic_unigene = {}
for line in input_unigene:
	line_list=list(line.split('\t'))
	dic_unigene[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_GO_file=sys.argv[6]
input_GO=open(input_GO_file, 'r', encoding="utf-8")
dic_GO = {}
for line in input_GO:
	line_list=list(line.split('\t'))
	dic_GO[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_bin_file=sys.argv[7]
input_MapMan_bin=open(input_MapMan_bin_file, 'r', encoding="utf-8")
dic_MapMan_bin = {}
for line in input_MapMan_bin:
	line_list=list(line.split('\t'))
	dic_MapMan_bin[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_name_file=sys.argv[8]
input_MapMan_name=open(input_MapMan_name_file, 'r', encoding="utf-8")
dic_MapMan_name = {}
for line in input_MapMan_name:
	line_list=list(line.split('\t'))
	dic_MapMan_name[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')



input_DE_file=sys.argv[1]
input_DE=open(input_DE_file, 'r', encoding="utf-8")

input_DE_file_name=input_DE_file.split('.')
output_name=input_DE_file_name[0]+"_features_added"+".csv"
output=open(output_name, 'w')

for line in input_DE:
	if line.startswith('Solyc'):
		Description = ''
		entrez = ''
		UniProt = ''
		unigene = ''
		GO = ''
		MapMan_bin = ''
		MapMan_name = ''
		
		line_list=list(line.split('\t'))
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
		


		output.write(Solyc+'\t'+line_list[1]+'\t'+line_list[2]+'\t'+line_list[3]+'\t'+line_list[4].rstrip('\n')+'\t'+Description+'\t'+entrez+'\t'+UniProt+'\t'+unigene+'\t'+GO+'\t'+MapMan_bin+'\t'+MapMan_name+'\n')
	else:
		output.write('gene'+'\t'+'logFC'+'\t'+'logCPM'+'\t'+'PValue'+'\t'+'FDR'+'\t'+'Description'+'\t'+'entrez'+'\t'+'UmiProt'+'\t'+'unigeme'+'\t'+'GO_Term'+'\t'+'MapMan_bin'+'\t'+'MapMan_name'+'\n')