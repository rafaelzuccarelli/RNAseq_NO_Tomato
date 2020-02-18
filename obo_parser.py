#! /usr/bin/env python3
import sys

input_obo_file=sys.argv[1]
input_obo=open(input_obo_file, 'r', encoding="utf-8")

input_obo_file_name=input_obo_file.split('.')
output_name=input_obo_file_name[0]+"_list"+".csv"
output=open(output_name, 'w')

GO_Terms = input_obo.read().split('[Term]')
GO_Terms.pop(0)

for term in GO_Terms:
	dic_name = {}
	dic_namespace = {}
	atributes = term.split('\n')
	atributes.pop(0)

	GO_id = atributes[0].lstrip('id: ').rstrip('\n')
	GO_name = atributes[1].lstrip('name: ').rstrip('\n')
	GO_namespace = atributes[2].lstrip('namespace: ').rstrip('\n')
	print(GO_id +'\t'+ GO_name +'\t'+ GO_namespace)
	output.write(GO_id +'\t'+ GO_name +'\t'+ GO_namespace+'\n')

