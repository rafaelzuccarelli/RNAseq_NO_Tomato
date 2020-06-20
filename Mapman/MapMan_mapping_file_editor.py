import sys
import os

wd = os.getcwd()
print('Reading new bins...')
New_bins_file = wd + '/New_bins/New_bins.csv'
New_bins = open(New_bins_file, 'r', encoding = "utf-8")
New_bins_dic = {}
for line in New_bins:
    line_list = list(line.split('\t'))
    Solyc_new = line_list[0].replace('"', '').split('.')
    Solyc_new_short = Solyc_new[0].replace('s','S')
    New_bins_dic[Solyc_new_short.replace('"', '')] = line_list[-1].rstrip("\n").replace('"', '')
    #print(Solyc_new)
BinCode_BinName_file = wd + '/dic_files/BinCode_BinName.csv'
BinCode_BinName = open(BinCode_BinName_file, 'r', encoding = "utf-8")
BinCode_BinName_dic = {}
for line in BinCode_BinName:
    line_list = list(line.split('\t'))
    BinCode = line_list[0].lstrip('"').rstrip('"')
    BinCode_BinName_dic[BinCode] = line_list[1].lstrip('"').rstrip('"')
    #print(BinCode + '\t' + BinCode_BinName_dic[BinCode])

input_directory = wd + '/input'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        mapping_file = input_directory + '/' + file
        mapping = open(mapping_file, 'r', encoding = "utf-8")
        mapping_file_name_path = mapping_file.split('/')
        mapping_file_name_extension = mapping_file_name_path[-1].split('.')
        mapping_file_name = mapping_file_name_extension[0]
        print("Edited mapping file... " + mapping_file_name_path[-1] + '\tSolyc\t\tOld_bin\t\tNew_bin')
        output_file = wd + '/output/' + mapping_file_name + "_custom.txt"
        output = open(output_file, 'w', encoding = 'utf-8')
        Solyc_short_set = set() 
        for line in mapping:
            line_list = line.split('\t')
            Solyc = line_list[2].replace('"', '').replace('s','S').replace("'","").split('.')
            Bin = line_list[0].replace('"', '').replace("'","").split('.')
            Bin_1st = Bin[0]
            Solyc_short = Solyc[0]
            set_list = list(Solyc_short_set)
            dot = '.'
            if Solyc_short in New_bins_dic.keys() and Bin_1st == '35' and Solyc_short not in set_list:
                 
                New_bins = New_bins_dic[Solyc_short]
                New_bins_list = New_bins.split('|')
                counter = list(range(0,len(New_bins_list)))
                for i in counter:
                    print('Removed not assigned\t' + dot.join(Solyc) + '\tfrom bin\t' + dot.join(Bin) +  '\tand added to\t' + New_bins_list[i])
                    output.write("'" + New_bins_list[i] + "'\t'"
                                 + BinCode_BinName_dic[New_bins_list[i]] + "'\t"
                                 + line_list[2] + "\t"
                                 + line_list[3] + "\n")
                    
            elif Solyc_short in New_bins_dic.keys() and Bin_1st != '35' and Solyc_short not in set_list:
                New_bins = New_bins_dic[Solyc_short]
                New_bins_list = New_bins.split('|')
                counter = list(range(0,len(New_bins_list)))
                for i in counter:
                    print('replaced\t' + dot.join(Solyc) + '\tfrom bin\t' + dot.join(Bin) +  '\tto\t' + New_bins_list[i])#print(New_bins_list)
                    output.write(line)#(remember to remove that)
                    output.write("'" + New_bins_list[i] + "'\t'"
                                 + BinCode_BinName_dic[New_bins_list[i]]+ "'\t"
                                 + line_list[2] + "\t"
                                 + line_list[3] + "\n")
            elif Solyc_short not in New_bins_dic.keys() and Solyc_short not in set_list:
                output.write(line)
            if Solyc_short != '':
                Solyc_short_set.add(Solyc_short)
print('Done!')
