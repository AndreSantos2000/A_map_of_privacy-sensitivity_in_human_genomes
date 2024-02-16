def readCitoBandFile(file_path):
    """
    """
    #currentline=0
    f = open(file_path, 'r')

    dataset = []
    #count = 0
    for line in f:
        lineArray = line.split("\t")
        #print(len(lineArray))
        dataset.append(lineArray)
    return dataset

def readSTRFile(file_path):
    """
    """
    #currentline=0
    f = open(file_path, 'r')

    dataset = []
    #count = 0
    for line in f:
        lineArray = line.split("\t")
        #print(len(lineArray))
        dataset.append(lineArray)
    return dataset

def getChomossome(ds, num):
    """
    """
    chomossome = 'chr' + str(num)
    chr_list = []
    for line in ds:
        if line[0] == chomossome:
            chr_list.append(line)
    return chr_list


def str_citoband(str_ds, citoband_ds):
    newSTR_dataset = []
    str_ds[0][-1] = str_ds[0][-1][:-1]
    str_ds[0].append("citoband" + "\n")
    newSTR_dataset.append(str_ds[0])

    for row in str_ds[1:]:
        citoband_found = False
        indices = []
        indices.append(row[1])
        indices.append(row[2])
        for citoband in citoband_ds:
            if int(indices[0]) >= int(citoband[1]) and int(indices[1]) <= int(citoband[2]) and citoband_found == False:
                #print("resulting citoband:", citoband[3])
                citoband_found = True
                row[-1] = row[-1][:-1]
                row.append(str(citoband[3] + "\n"))
        
        if citoband_found == False:
            row[-1] = row[-1][:-1]
            row.append("Citoband not found. \n")
            for n in range (len(citoband_ds)-1):
                if indices[0] >= citoband_ds[n][1] and indices[1] <= citoband_ds[n+1][2]:
                    row.append(str(citoband_ds[n][3]) + " & " + str(citoband_ds[n+1][3] + "\n"))
        
        newSTR_dataset.append(row)
    return newSTR_dataset

def writeNewtxt(new_file_path, dataset):
    f = open(new_file_path, 'w')
    for line in dataset:
        str_line = ""
        for col in line[:-1] :
            str_line += col + "\t"
        str_line += line[-1]
        f.write(str_line)
    f.close

CitobandPath = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_new.txt"
STRPath = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/HumanChr.18.txt"
STRPath2 = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/HumanChr.18_new.txt"

citobands_ds = readCitoBandFile(CitobandPath)
str_dataset = readSTRFile(STRPath)

print(citobands_ds[0], "\n")


chr18_list = getChomossome(citobands_ds, 18)
#print(chr18_list, "\n")
#print(len(chr18_list), "\n") # ficheiro de citobands atualizado já encontrado

#print(str_dataset[0])
print("first index: ", str_dataset[1][1], "last index: ", str_dataset[1][2])


newSTR_dataset = str_citoband(str_dataset, chr18_list)
#print(newSTR_dataset[0])
#print(newSTR_dataset[1])


writeNewtxt(STRPath2, newSTR_dataset)


#print(newSTR_dataset[0])
#print(newSTR_dataset[0][16])
#print(newSTR_dataset[1][16])
#print(newSTR_dataset[1][-1])



