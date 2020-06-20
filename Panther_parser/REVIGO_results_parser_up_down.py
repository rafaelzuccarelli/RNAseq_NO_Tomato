import sys
import os

wd = os.getcwd()
print('Reading dictionaries...')


input_REVIGO_file = wd + '/from_REVIGO/REVIGO.csv'
input_REVIGO = open(input_REVIGO_file, 'r', encoding = "utf-7")
REVIGO_dic = {}
for line in input_REVIGO:
    line_list = line.split(',')
    REVIGO_dic[line_list[0]] = line_list
eliminated_dic = {}
for line in input_REVIGO:
    line_list = line.split(',')
    eliminated_dic[line_list[0]] = line_list[10].rstrip("\n").replace('"', '')


input_directory = wd + '/from_PANTHER'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        input_PANTHER_file = input_directory + '/' + file
        input_PANTHER = open(input_PANTHER_file, 'r', encoding = "utf-7")
        #creates file based on input file name
        input_PANTHER_file_name_path = input_PANTHER_file.split('/')
        input_PANTHER_file_name_extension = input_PANTHER_file_name_path[-1].split('.')
        input_PANTHER_file_name = input_PANTHER_file_name_extension[0]
        output_file = wd + '/to_R/' + input_PANTHER_file_name + ".csv"
        output=open(output_file, 'w', encoding = "utf-8")
        print("creating REVIGO list from " + input_PANTHER_file_name_path[-1])
        output.write('GO' + ',' +
                     'Gene_number' + ',' +
                     'Fold_enrichment' + ',' +
                     'FDR' + '\n')
        for line in input_PANTHER:
            line_list = line.split('\t')
            GO_ID_list = line_list[0].split(' ')
            GO_ID = GO_ID_list[-1].rstrip(')').lstrip('(')
            if GO_ID.startswith('GO:'):
                if GO_ID in REVIGO_dic.keys() and eliminated_dic[GO_ID] == '0':
                    print(line_list[0] + '\t' +
                          line_list[2] + '\t' +
                          line_list[5] + '\t' +
                          line_list[7].rstrip('\n'))
                    output.write(line_list[0] + ',' +
                          line_list[2] + ',' +
                          line_list[5] + ',' +
                          line_list[7])
