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


def calc_size1(dataset):
    """Calculate size of STR by subtractong last index with first index
    """
    newSTR_dataset = []
    dataset[0][-1] = dataset[0][-1][:-1]
    dataset[0].append("Size1" + "\n")
    newSTR_dataset.append(dataset[0])

    for row in dataset[1:]:
        size = int(row[2]) - int(row[1])
        row[-1] = row[-1][:-1]
        row.append(str(size) + "\n")
        newSTR_dataset.append(row)
    return newSTR_dataset

def calc_size2(dataset):
    """Calculate size of STR by multiplying pattern_size and copy_number
    """
    newSTR_dataset = []
    dataset[0][-1] = dataset[0][-1][:-1]
    dataset[0].append("Size2" + "\n")
    newSTR_dataset.append(dataset[0])

    for row in dataset[1:]:
        size = float(row[3]) * float(row[4])
        row[-1] = row[-1][:-1]
        row.append(str(size) + "\n")
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

STRPath = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/HumanChr.18_new.txt"
STRPath2 = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/HumanChr.18_new2.txt"


str_dataset = readSTRFile(STRPath)
str_dataset_sized1 = calc_size1(str_dataset)
str_dataset_sized2 = calc_size2(str_dataset_sized1)

writeNewtxt(STRPath2, str_dataset_sized2)

print(str_dataset_sized2[0])
print(str_dataset_sized2[18][-10])
print(str_dataset_sized2[18][16], len(str_dataset_sized2[18][-10]), int(str_dataset_sized2[18][16])/len(str_dataset_sized2[18][-10]), str_dataset_sized2[18][3], str_dataset_sized2[18][4])
print(str_dataset_sized2[18][16])
print(str_dataset_sized2[18][-2])      #A coluna 17 (index16) parece ser o tamanho do STR(Last - First indeces  + 1)

print(508/43)
print(43*11.813953488372093)           #