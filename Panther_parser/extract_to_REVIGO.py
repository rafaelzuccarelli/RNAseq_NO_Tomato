import sys
import os

wd = os.getcwd()
print('Reading file...')

input_directory = wd + '/from_PANTHER'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        input_PANTHER_file = input_directory + '/' + file
        input_PANTHER = open(input_PANTHER_file, 'r', encoding = "utf-7")
        #creates file based on input file name
        input_PANTHER_file_name_path = input_PANTHER_file.split('/')
        input_PANTHER_file_name_extension = input_PANTHER_file_name_path[-1].split('.')
        input_PANTHER_file_name = input_PANTHER_file_name_extension[0]
        output_file = wd + '/to_REVIGO/' + input_PANTHER_file_name + "_REVIGO.csv"
        output=open(output_file, 'w', encoding = "utf-8")
        print("creating REVIGO list from " + input_PANTHER_file_name_path[-1])
        for line in input_PANTHER:
            line_list = line.split('\t')
            GO_ID_list = line_list[0].split(' ')
            GO_ID = GO_ID_list[-1].rstrip(')').lstrip('(')
            if GO_ID.startswith('GO:'):
                print(GO_ID + '\t' + line_list[7].rstrip('\n'))
                output.write(GO_ID + '\t' + line_list[7])
