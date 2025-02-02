import sys
import os

wd = os.getcwd()
print('Reading dictionaries...')

input_Description_file = wd + '/dic_files/Solyc_Description.csv'
input_Description = open(input_Description_file, 'r', encoding = "utf-8")
dic_description = {}
for line in input_Description:
    line_list = list(line.split('\t'))
    dic_description[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_entrez_file = wd + '/dic_files/Solyc_entrez.csv'
input_entrez = open(input_entrez_file, 'r', encoding = "utf-8")
dic_entrez = {}
for line in input_entrez:
    line_list = list(line.split('\t'))
    dic_entrez[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_UniProt_file = wd + '/dic_files/Solyc_UniProt.csv'
input_UniProt = open(input_UniProt_file, 'r', encoding = "utf-8")
dic_UniProt = {}
for line in input_UniProt:
    line_list = list(line.split('\t'))
    dic_UniProt[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_unigene_file = wd + '/dic_files/Solyc_unigene.csv'
input_unigene = open(input_unigene_file, 'r', encoding = "utf-8")
dic_unigene = {}
for line in input_unigene:
    line_list = list(line.split('\t'))
    dic_unigene[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_GO_file = wd + '/dic_files/ITAG3.2_protein_go.tsv'
input_GO = open(input_GO_file, 'r', encoding = "utf-8")
dic_GO = {}
for line in input_GO:
    line_list = list(line.split('\t'))
    dic_GO[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_bin_file = wd + '/dic_files/Solyc_bin.csv'
input_MapMan_bin = open(input_MapMan_bin_file, 'r', encoding = "utf-8")
dic_MapMan_bin = {}
for line in input_MapMan_bin:
    line_list = list(line.split('\t'))
    dic_MapMan_bin[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_name_file = wd + '/dic_files/Solyc_MapMan_name.csv'
input_MapMan_name = open(input_MapMan_name_file, 'r', encoding = "utf-8")
dic_MapMan_name = {}
for line in input_MapMan_name:
        line_list = list(line.split('\t'))
        dic_MapMan_name[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_MapMan_BinCode_BinName_file = wd + '/dic_files/BinCode_BinName.csv'
input_MapMan_BinCode_BinName = open(input_MapMan_BinCode_BinName_file, 'r', encoding = "utf-8")
dic_MapMan_BinCode_BinName = {}
for line in input_MapMan_BinCode_BinName:
        line_list = list(line.split('\t'))
        dic_MapMan_BinCode_BinName[line_list[0].replace('"', '')] = line_list[1].rstrip("\n").replace('"', '')
        
input_NCBI_file = wd + '/dic_files/Solyc_NCBI.csv'
input_NCBI = open(input_NCBI_file, 'r', encoding = "utf-8")
dic_NCBI = {}
for line in input_NCBI:
    line_list = list(line.split('\t'))
    dic_NCBI[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_ortho_file = wd + '/dic_files/Solyc_arthal_orthologs.csv'
input_ortho = open(input_ortho_file, 'r', encoding = "utf-8")
dic_ortho = {}
for line in input_ortho:
    line_list = list(line.split('\t'))
    dic_ortho[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_GO_names_file = wd + '/dic_files/go_list.csv'
input_GO_names = open(input_GO_names_file, 'r', encoding = "utf-8")
dic_GO_names = {}
for line in input_GO_names:
    line_list = list(line.split('\t'))
    dic_GO_names[line_list[0].replace('"', '')] = line_list[-2].rstrip("\n").replace('"', '')

input_GO_domain_file = wd + '/dic_files/go_list.csv'
input_GO_domain = open(input_GO_domain_file, 'r', encoding = "utf-8")
dic_GO_domain = {}
for line in input_GO_domain:
    line_list = list(line.split('\t'))
    dic_GO_domain[line_list[0].replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')

input_SNO_file = wd + '/dic_files/Solyc_SNO.csv'
input_SNO = open(input_SNO_file, 'r', encoding = "utf-8")
SNO_list = []
for line in input_SNO:
    SNO_list.append(line.rstrip('\n'))

input_YNO2_file = wd + '/dic_files/Solyc_YNO2.csv'
input_YNO2 = open(input_YNO2_file, 'r', encoding = "utf-8")
YNO2_list = []
for line in input_YNO2:
    YNO2_list.append(line.rstrip('\n')) 

input_directory = wd + '/Input'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        input_DE_file = input_directory + '/' + file
        input_DE = open(input_DE_file, 'r', encoding = "utf-8")
        input_DE_file_name_path = input_DE_file.split('/')
        input_DE_file_name_extension = input_DE_file_name_path[-1].split('.')
        input_DE_file_name = input_DE_file_name_extension[0]
        print("adding features to " + input_DE_file_name_path[-1])
        output_file=wd + '/Output/' + input_DE_file_name + "_features_added_MapMan.csv"
        output=open(output_file, 'w')
        for line in input_DE:
            if line.startswith('Solyc'):
                
                Description = ''
                entrez = ''
                UniProt = ''
                unigene = ''
                GO = ''
                MapMan_bin = ''
                MapMan_names = ''
                NCBI = ''
                ortho_ID = ''
                SNO = ''
                YNO2 = ''
                SNO_and_YNO2 = ''
                line_list = list(line.split('\t')) #change separator for input DE here
                Solyc = line_list[0]
                
                if Solyc in dic_description.keys():
                    Description = dic_description[Solyc]
                if Solyc in dic_entrez.keys():
                    entrez = dic_entrez[Solyc]
                if Solyc in dic_UniProt.keys():
                    UniProt = dic_UniProt[Solyc]
                if Solyc in dic_unigene.keys():
                    unigene = dic_unigene[Solyc]
               
                              
                if Solyc in dic_NCBI.keys():
                    NCBI = dic_NCBI[Solyc]
                if Solyc in dic_ortho.keys():
                    ortho_ID = dic_ortho[Solyc]
                if Solyc in SNO_list:
                    SNO = 'SNO'
                if Solyc in YNO2_list:
                    YNO2 = 'YNO2'
                if Solyc in SNO_list and Solyc in YNO2_list:
                    SNO_and_YNO2 = 'SNO_&_YNO2'

                if Solyc in dic_GO.keys():
                    GO = dic_GO[Solyc]
                GO_list = list(GO.split('|'))
                len_GO = len(GO_list)
                counter_GO = list(range(0,len_GO))
                dic_GO_names_key = ''
                GO_names_list = []
                empty = []
                for i in counter_GO:
                    dic_GO_names_key = GO_list[i]
                    if dic_GO_names_key in dic_GO_names.keys():
                        GO_names_list.append(dic_GO_names[dic_GO_names_key])
                if GO_names_list != empty:
                    bar = ' | '
                    GO_names = bar.join(GO_names_list)

                if Solyc in dic_MapMan_bin.keys():
                    MapMan_bin = dic_MapMan_bin[Solyc] #mapman bin with "|" separator
                MapMan_bin_list = list(MapMan_bin.split('|')) #split the bins in individual BinCode
                len_MapMan_bin_list = len(MapMan_bin_list) #list of individual BinCode
                counter_MapMan = list(range(0,len_MapMan_bin_list)) #counter to "walk" throught the MapMan_bin_list
                MapMan_BinCode_BinName_key = '' #key to use in the dic_MapMan_BinCode_BinName dicionary
                MapMan_names_list = [] #list with the MapMan names retrieved from the dic_MapMan_BinCode_BinName dictionary
                empty = []
                for i in counter_MapMan:
                    MapMan_BinCode_BinName_key = MapMan_bin_list[i].replace(' ','')
                    if MapMan_BinCode_BinName_key in dic_MapMan_BinCode_BinName.keys():
                        MapMan_names_list.append(dic_MapMan_BinCode_BinName[MapMan_BinCode_BinName_key])
                        #print(dic_MapMan_BinCode_BinName[MapMan_BinCode_BinName_key])
                if MapMan_names_list != empty:
                    bar = ' | '
                    MapMan_names = bar.join(MapMan_names_list)
                for i in counter_MapMan:
                    output.write(line.rstrip('\n') + '\t'
                                     + Description + '\t'
                                     + entrez + '\t'
                                     + UniProt + '\t'
                                     + unigene + '\t'
                                     + GO + '\t'
                                     + MapMan_bin_list[i].replace(' ','') + '\t'
                                     + MapMan_names_list[i] + '\t'
                                     + NCBI + '\t'
                                     + ortho_ID+'\t'
                                     + SNO + '\t'
                                     + YNO2 + '\t'
                                     + SNO_and_YNO2 + '\n')                
            else:
                output.write(line.rstrip('\n') + '\t'
                             + 'Description' + '\t'
                             + 'entrez' + '\t'
                             + 'Uniprot' + '\t'
                             + 'unigeme' + '\t'
                             + 'GO' + '\t'
                             + 'MapMan_bin' + '\t'
                             + 'MapMan_name' + '\t'
                             + 'NCBI' + '\t'
                             + 'A._thaliana_ortholog'+'\t'
                             + 'SNO' + '\t'
                             + 'YNO2' + '\t'
                             + 'SNO_and_YNO2' + '\n')
