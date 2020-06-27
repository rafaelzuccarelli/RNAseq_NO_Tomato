import sys
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

wd = os.getcwd()

#Scale, dark red, red, light red, white, light blue, blue, dark blue
r_scale = []
g_scale = []
b_scale = []
value_scale = []
input_scale_file = wd + '/dic_files/Scale.csv'
input_scale = open(input_scale_file, 'r', encoding = 'utf8')
for line in input_scale:
    line_list = line.split('\t')
    r_scale.append(int(line_list[0].rstrip('\n')))
    g_scale.append(int(line_list[1].rstrip('\n')))
    b_scale.append(int(line_list[2].rstrip('\n')))
    
    #column position for values to scale (3 = -3 to 3, 4 = -2.5 to 2.5, 5 = -2 to 2, 6 = -1.5 to 1.5 and 7 = -1 to 1)
    value_scale.append(float(line_list[3])) 

bin_set = set()
bin_set_1st = set()
bin_set_2nd = set()

bin_set_name = set()
bin_set_name_1st = set()
bin_set_name_2nd = set()

Solyc_bin_dic = {}
Solyc_fold_change_dic = {}
Solyc_bin_name_dic = {}
Solyc_list = []
list2 = []

input_directory = wd + '/Input'
for currentpath, folders, files in os.walk(input_directory):
    for file in files:
        input_DEG_file = input_directory + '/' + file
        input_DEG = open(input_DEG_file, 'r', encoding = "utf-8")
        input_DEG_file_name_path = input_DEG_file.split('/')
        input_DEG_file_name_extension = input_DEG_file_name_path[-1].split('.')
        input_DEG_file_name = input_DEG_file_name_extension[0]
        for line in input_DEG: 
            if line.startswith('Solyc'):
                line_list = line.split('\t')
                Solyc = line_list[0]
                Solyc_list.append(Solyc)#all solycs in DEG file                
                bins = line_list[14].split(' | ')
                bin_name = line_list[15].split(' | ')
                Solyc_bin_dic[Solyc] = bins
                Solyc_bin_name_dic[Solyc] = bin_name
                for i in bins:#set with all bin 1st level
                    bin_split = i.split('.')
                    bin_set_1st.add(bin_split[0])
                    if len(bin_split) >= 2:#set with all bin 2nd level
                        bin_set_2nd.add(bin_split[0] + '.' + bin_split[1])
                    
                for i in bin_name:
                    bin_name_split = i.split('.')
                    bin_set_name_1st.add(bin_name_split[0])
                    if len(bin_name_split) >= 2:
                        bin_set_name_2nd.add(bin_name_split[0] + '.' + bin_name_split[1])
                        
                fold_change = line_list[7]
                Solyc_fold_change_dic[Solyc] = fold_change
        
        bin_list_1st = list(bin_set_1st)
        bin_list_2nd = list(bin_set_2nd)
        

        bin_list_name_1st = list(bin_set_1st)
        bin_list_name_2nd = list(bin_set_2nd)
        #counters for walk in the list using 'for'
        counter_1st = list(range(0,len(bin_list_1st)))
        counter_2nd = list(range(0,len(bin_list_2nd)))
            
        #add zero to the fist number small then 10 in BinCode to apply a natural sorting 
        for i in counter_1st:
            if int(bin_list_1st[i]) < 10:
                bin_list_1st[i] = '0' + bin_list_1st[i]
        for i in counter_2nd:
            bin_split_list = bin_list_2nd[i].split('.')
            if int(bin_split_list[0]) < 10:
                bin_list_2nd[i] = '0' + bin_list_2nd[i]
        bin_list_1st.sort()#all bins natural sorted for the first level
        bin_list_2nd.sort()

        first_index = list(range(0, len(bin_list_1st)))
        second_index = list(range(0, len(bin_list_2nd)))
        
        list_test = [0]  
    
    x0 = 500 #pixel positions to insert text and objects in the image
    y0 = 145
    x1 = 520
    y1 = 165
    
    # creates a image file to put all 1st level bins
    image_png_1st = wd + '/Output/' + '1st.png'
    scale = Image.open('/media/rafael/2803D1E32A95159A/RNAseq/Scripts/MapMan_parser/heatmap_2nd/scale_3.png')
    img = Image.new('RGB', (13480,3508), color = (255,255,255))
    img.paste(scale)
    d = ImageDraw.Draw(img)
    fnt = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Verdana.ttf', 25)
    yn = 160
    ym = 110
    dot = '.'
    underscore = '_________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'
# get all bins and organize a list with 1st level bins and names
    for i in first_index:
        bin_name_1st = ''
        for Solyc in Solyc_list:
            for j in Solyc_bin_dic[Solyc]:
                bin_split_list = j.split('.')
                for k in bin_split_list:
                    bin_split_list_1st = bin_split_list[0]
                    if int(bin_split_list_1st) < 10:
                        bin_split_list_1st = '0' + bin_split_list_1st
                    if bin_split_list_1st == bin_list_1st[i]:
                        bin_name_full = Solyc_bin_name_dic[Solyc]
                        bin_name_1st_list = bin_name_full[0].split('.')
                        bin_name_1st = bin_name_1st_list[0]                                
                
        bin_number_name = bin_list_1st[i] + ' ' + bin_name_1st
        d.text((20,yn), bin_number_name, font=fnt, fill=(0,0,0))
        d.text((20,ym), underscore, font=fnt, fill=(0,0,0))
        print(bin_number_name)
#get all fold change values and store n a list for each    
        list2 = []
        for Solyc in Solyc_list:
            for j in Solyc_bin_dic[Solyc]:
                bin_split_list_1st = ''
                bin_split_list = j.split('.')
                for k in bin_split_list:
                    bin_split_list_1st = bin_split_list[0]
                    if int(bin_split_list_1st) < 10:
                        bin_split_list_1st = '0' + bin_split_list_1st
                if bin_split_list_1st == bin_list_1st[i]:
                    list2.append(float(Solyc_fold_change_dic[Solyc]))
        list2.sort(reverse = True)
    
        index_list2 = list(range(0, len(list2)))
               
        for index in index_list2:
            index_scale = min(range(len(value_scale)), key = lambda i: abs(value_scale[i] - list2[index]))#get the index of values_scale, based in the nearest value
            n = index_scale

            r = r_scale[n]
            g = g_scale[n]
            b = b_scale[n]

            if index % 3 == 0:
                d.rectangle((x0, y0, x1, y1), fill = (r, g, b), width = 2, outline = (0, 0, 0))
            if index % 3 == 1:
                d.rectangle((x0, y0 + 20, x1, y1 + 20), fill = (r, g, b), width = 2, outline = (0, 0, 0))
            if index % 3 == 2:
                d.rectangle((x0, y0 + 40, x1, y1 + 40), fill = (r, g, b), width = 2, outline=(0, 0, 0))
                x0 = x0 + 20 #move block right to the next step
                x1 = x1 + 20

        x0 = 500
        y0 = y0 + 75
        x1 = 520
        y1 = y1 + 75
        yn = yn + 75 
        ym = ym + 75
    
    d.text((20,ym), underscore, font=fnt, fill=(0,0,0))    
    img.save(image_png_1st, 'PNG')
    
#creates a file for each 1st level bin
    for l in first_index:              
        bin_set_1st_2nd = set()
        bin_list_1st_2nd = []
        set_bincode_binname = set()
        sety = set()
        for i in second_index:#gets all bins 2nd level and names, put in a set and print out to the image
            bin_2nd = bin_list_2nd[i]
            bin_name_2nd = ''
            for Solyc in Solyc_list:
                Solyc_bin = Solyc_bin_dic[Solyc]
                Solyc_bin_name = Solyc_bin_name_dic[Solyc]
                index = list(range(0,len(Solyc_bin)))
                for j in index:
                    if len(Solyc_bin[j].split('.')) >= 2:
                        bin_split_list = Solyc_bin[j].split('.')
                        bin_1st = bin_split_list[0]
                        bin_2nd = bin_split_list[0] + '.' + bin_split_list[1]
                        if int(bin_1st) < 10:
                            bin_1st = '0' + bin_1st
                            bin_2nd = '0' + bin_2nd
                        bin_name_split_list = Solyc_bin_name[j].split('.')
                        bin_name_2nd = bin_name_split_list[1]
                        bincode_binname = bin_2nd + ' ' + bin_name_2nd
                        if bin_list_1st[l] == bin_1st:
                            set_bincode_binname.add(bincode_binname)
        list_bincode_binname = list(set_bincode_binname)
        list_bincode_binname.sort()
        binname_size = 0
        gene_number_in_bin = 0
        
        for binname in list_bincode_binname:
            if len(binname) > binname_size:
                binname_size = len(binname)
        file_height = 160 + (len(list_bincode_binname) * 80)
        
        for m in list_bincode_binname:
            list3 = []
            bincode_binname_list = m.split(' ')
            bin = bincode_binname_list[0].split('.')
            first = bin[0]
            second = bin[0] + '.' + bin[1]
            fold_change_set = set()
            for Solyc in Solyc_list:
                Solyc_bin = Solyc_bin_dic[Solyc]
                Solyc_bin_name = Solyc_bin_name_dic[Solyc]
                index = list(range(0,len(Solyc_bin)))
                for j in index:
                    if len(Solyc_bin[j].split('.')) >= 2:
                        bin_split_list = Solyc_bin[j].split('.')
                        bin_1st = bin_split_list[0]
                        bin_2nd = bin_split_list[0] + '.' + bin_split_list[1]
                        if int(bin_1st) < 10:
                            bin_1st = '0' + bin_1st
                            bin_2nd = '0' + bin_2nd
                        if bin_2nd == second:
                            fold_change_set.add(float(Solyc_fold_change_dic[Solyc]))
            list3 = list(fold_change_set)
            list3.sort(reverse = True)
            if len(list3) > gene_number_in_bin:
                gene_number_in_bin = len(list3)
        heatmap_lenght = int((gene_number_in_bin * 21)/ 3 + 30)
            
        print(bin_list_1st[l])
        x0 = binname_size * 16 #pixel positions to insert text and objects in the image
        y0 = 145
        x1 = x0 + 20
        y1 = 165
        file_lenght = x0 + heatmap_lenght
        file_name = bin_list_1st[l]
        image_png_2nd = wd + '/Output/' + file_name + '.png'
        img = Image.new('RGB', (file_lenght,file_height), color = (255,255,255))
        scale = Image.open('/media/rafael/2803D1E32A95159A/RNAseq/Scripts/MapMan_parser/heatmap_2nd/scale_3.png')
        img.paste(scale)
        d = ImageDraw.Draw(img)
        fnt = ImageFont.truetype('/usr/share/fonts/truetype/msttcorefonts/Verdana.ttf', 25)
        yn = 160
        ym = 110
        dot = '.'
        underscore = '____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________'
        
        for m in list_bincode_binname:
            print(m)
            d.text((20,yn), m, font=fnt, fill=(0,0,0))
            d.text((20,ym), underscore, font=fnt, fill=(0,0,0))
            list3 = []
            bincode_binname_list = m.split(' ')
            bin = bincode_binname_list[0].split('.')
            first = bin[0]
            second = bin[0] + '.' + bin[1]
            fold_change_set = set()
            for Solyc in Solyc_list:
                Solyc_bin = Solyc_bin_dic[Solyc]
                Solyc_bin_name = Solyc_bin_name_dic[Solyc]
                index = list(range(0,len(Solyc_bin)))
                for j in index:
                    if len(Solyc_bin[j].split('.')) >= 2:
                        bin_split_list = Solyc_bin[j].split('.')
                        bin_1st = bin_split_list[0]
                        bin_2nd = bin_split_list[0] + '.' + bin_split_list[1]
                        if int(bin_1st) < 10:
                            bin_1st = '0' + bin_1st
                            bin_2nd = '0' + bin_2nd
                        if bin_2nd == second:
                            fold_change_set.add(float(Solyc_fold_change_dic[Solyc]))
            list3 = list(fold_change_set)
            list3.sort(reverse = True)
            file_lenght = len(list3)
            #print(list3)
            index_list3 = list(range(0, len(list3)))
            #print(index_list3)
            #print(list3)      
            for index in index_list3:
                #print(list3[index])
                
                index_scale = min(range(len(value_scale)), key = lambda m: abs(value_scale[m] - float(list3[index])))#get the index of values_scale, based in the nearest value
                n = index_scale
                
                r = r_scale[n]
                g = g_scale[n]
                b = b_scale[n]

                if index % 3 == 0:
                    d.rectangle((x0, y0, x1, y1), fill = (r, g, b), width = 2, outline = (0, 0, 0))
                if index % 3 == 1:
                    d.rectangle((x0, y0 + 20, x1, y1 + 20), fill = (r, g, b), width = 2, outline = (0, 0, 0))
                if index % 3 == 2:
                    d.rectangle((x0, y0 + 40, x1, y1 + 40), fill = (r, g, b), width = 2, outline=(0, 0, 0))
                    x0 = x0 + 20 #move block right to the next step
                    x1 = x1 + 20
            #print(m)
            x0 = binname_size * 16
            y0 = y0 + 75
            x1 = x0 + 20
            y1 = y1 + 75
            yn = yn + 75 
            ym = ym + 75
            
        d.text((20,ym), underscore, font=fnt, fill=(0,0,0))
        img.save(image_png_2nd, 'PNG')
