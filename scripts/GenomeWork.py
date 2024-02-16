import argparse 
import math

filePath = "/home/androx/Documents/trabalho/datasets/STR/HomosapiensHG38_nov2014/HumanChr.22.txt"
RefFilePath = "/home/androx/Documents/trabalho/datasets/GenomeAssembly/feb3_2022/ncbi_dataset/data/GCF_000001405.40/GCF_000001405.40_GRCh38.p14_genomic.fna'"


refFilePath = filePath.split("/")
currentline=0
f = open(filePath, 'r')

#Escrever função que devolva a janela da dimensao desejada à volta do padrão
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


def getSTRSequence(dataframe, line, size):
    """
    Indices may be specific to single STR file
    """
    n_leftFlank = dataframe[0].index('FlankingLeft50')
    n_arraySeq = dataframe[0].index('ArraySequence')
    n_rightFlank = dataframe[0].index('FlankingRight50')
    #full_sequence = dataframe[line][n_leftFlank] + dataframe[line][n_arraySeq] + dataframe[line][n_rightFlank]
    print(dataframe[:4])
    STRsize = len(dataframe[line][n_arraySeq])
    
    if size < STRsize:
        print("need a bigger sized sequence, at least:", STRsize+2)
    elif size == STRsize:
        sequence = dataframe[line][n_arraySeq]
        lc_sequence =sequence.lower()
        print("returning the STR sequence with no flanks")
        return lc_sequence, len(lc_sequence)
    else:
        flanks_size = size - STRsize
        print("STR size: ", STRsize)
        print("flanks size: ", flanks_size)
        sequence = dataframe[line][n_leftFlank][-round(flanks_size/2):] + dataframe[line][n_arraySeq] + dataframe[line][n_rightFlank][:math.floor(flanks_size/2)]
        
        lc_sequence =sequence.lower()
        return lc_sequence, len(lc_sequence)

    

#print(getSTRSequence(dataset, 1, 53))


def main():

    parser = argparse.ArgumentParser(description='Script to receive gene string sequence from STR txt input file')

    parser.add_argument('-p','--refpath', required=True, type=str, help='Path to the STR file')
    parser.add_argument('-r','--row', required=True, type=str, help='number of the row to obtain the sequence')
    parser.add_argument('-s', '--Sequence_size', required=True, type=str, help='the size of returned sequence')
    parser.add_argument('-c', '--case', required=False, type=str, help='upper or lowercase')

    args = parser.parse_args()

    file = args.refpath

    dataset = readSTRFile(args.refpath)

    seq = getSTRSequence(dataset, int(args.row), int(args.Sequence_size))

    print(seq)

if __name__ == '__main__':
    main()



