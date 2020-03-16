import sys
import os

wd = os.getcwd()
print('Reading dictionaries...')

#creates dictionaries from files in /dic_files

input_Description_file = wd + '/dic_files/DE_WTCTRLxNOBk_features_added_dic.csv'
input_Description = open(input_Description_file, 'r', encoding = "utf-8")
dic_description = {}
dic_header = ''
for line in input_Description:
    if not line.startswith('Solyc'):
        print(line)
        dic_header = line.rstrip('\n')
    line_list = list(line.split('\t'))
    dic_description[line_list[0].replace('"', '')] = line.rstrip("\n").replace('"', '')
        
input_directory = wd + '/input'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        input_MapMan_file = input_directory + '/' + file
        input_MapMan = open(input_MapMan_file, 'r', encoding = "utf-8")
        #creates file based on input file name
        input_MapMan_file_name_path = input_MapMan_file.split('/')
        input_MapMan_file_name_extension = input_MapMan_file_name_path[-1].split('.')
        input_MapMan_file_name = input_MapMan_file_name_extension[0]
        output_file = wd + '/output/' + input_MapMan_file_name + "_features_added.csv"
        output = open(output_file, 'w')
        print("adding features to " + input_MapMan_file_name_path[-1])
        for line in input_MapMan: #add features checking each Solyc, line by line
            if not line.startswith('BinCode'):
                line_list = list(line.split('\t'))
                Solyc = line_list[2].replace('s', 'S')
                #print(Solyc)
                if Solyc in dic_description.keys():
                    output.write(line.rstrip('\n') + '\t' + dic_description[Solyc] + '\n')
            else:
                output.write(line.rstrip('\n') + '\t' + dic_header + '\n')
