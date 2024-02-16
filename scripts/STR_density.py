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

def Somatorio_STR_lengths(citoband, STR_ds):
    totalSTRlength = 0
    #print("STR_citoband: ", STR_ds[1][-3])
    #print("citoband: ", citoband[3])
    for row in STR_ds[1:]:
        #print("citoband in STR_File: ", row[-3], "citoband", citoband[3], "\n")
        if row[-3] == citoband[3] or citoband[3] in row[-3]:
            #print("match found \n")
            totalSTRlength += int(row[-2])
    print("Total length: ", totalSTRlength, "\n")
    return totalSTRlength

#Esta função só considera STRs em linhas seguidas
def STR_overlap(STR_ds):
    to_subtract = 0
    for row in range(len(STR_ds)-2):
        last_index = STR_ds[row][2]
        first_index2 = STR_ds[row+1][1]
        if first_index2<last_index:
            to_subtract += last_index - first_index2
    return to_subtract


def calc_byCitoband(citoList, STR_ds):
    """
    """
    new_citolist = []
    for citoband in citoList:
        print("citoband:", citoband[3])
        citoband[-1] = citoband[-1][:-1]
        densidade = Somatorio_STR_lengths(citoband, STR_ds)/int(citoband[-1])
        print("citoband:", citoband[3], " densidadeSTR: ", densidade)
        citoband.append(str(densidade)+"\n")
        new_citolist.append(citoband)
    return new_citolist

        
def writeNewtxt(new_file_path, dataset):
    f = open(new_file_path, 'w')
    for line in dataset:
        str_line = ""
        for col in line[:-1] :
            str_line += str(col) + "\t"
        str_line += str(line[-1])
        f.write(str_line)
    f.close 

def findout(dataset):
    for line in dataset[1:]:
        if int(line[1]) >= 80373285:
            print ("blabla:   ", line)



citobandPath = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_new.txt"
new_citobandPath = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_new_dens.txt"
STRPath = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/HumanChr.18_new2.txt"
STRcitoPath = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/STRcitobands.txt"

citobands_ds = readCitoBandFile(citobandPath)
str_dataset = readSTRFile(STRPath)

citobands18 = getChomossome(citobands_ds, 18)
#print(getChomossome(citobands_ds, 18), "\n")

str_densities18 = calc_byCitoband(citobands18, str_dataset)

writeNewtxt(new_citobandPath, str_densities18)

#print(citobands_ds[0])
#print(str_dataset[0])


def getSTR_citobands(dataset, newPath):
    STRcitobands=[]
    firstLine = ["firstIndex", "lastIndex", "citoband\n"]
    STRcitobands.append(firstLine)
    for row in dataset[1:]:
        newRow = [row[1], row[2], row[-3] + "\n"]
        STRcitobands.append(newRow)
    #print (STRcitobands)
    writeNewtxt(newPath, STRcitobands)



getSTR_citobands(str_dataset, STRcitoPath)

findout(str_dataset)