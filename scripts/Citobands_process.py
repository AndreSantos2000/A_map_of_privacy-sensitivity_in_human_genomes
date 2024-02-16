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

def add_dimensionscolumn(dataset):
    new_dataset = []
    for line in dataset:
        last_index = int(line[2]) -1
        line[2] = str(last_index)
        line[-1] = line[-1][:-1]
        line.append(str(int(line[2])-int(line[1])) + "\n")
        new_dataset.append(line)
    return new_dataset

def writeCitoBandFile(new_file_path, dataset):
    f = open(new_file_path, 'w')
    for line in dataset:
        line = str(line[0]+"\t"+ line[1]+"\t"+ line[2]+"\t"+ line[3]+"\t"+ line[4]+"\t"+line[5])
        f.write(line)
    f.close

filePath = "/home/androx/Documents/trabalho/citobands/cytobandFiltered.txt"
writeFilePath = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_new.txt"
path_list = filePath.split("/")
path_list = path_list.pop(len(path_list) - 1)
writeFile = ""
for l in path_list:
    writeFile = writeFile + l + "/"
writeFile = writeFile + "Citoband_newFile"


dataset = readCitoBandFile(filePath)

print(dataset[0])
print(dataset[1])

new_dataset = add_dimensionscolumn(dataset)

print(new_dataset[0])
print(new_dataset[1])

writeCitoBandFile(writeFilePath, new_dataset)