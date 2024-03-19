import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def getChromossome(df, n):
    """Returns pandas dataframe with only the citobands of one chromossome n
    """
    chomossome = str(n)
    chr_array = []
    #print("dataframe columns = ", df.columns)
    #chr_array.append(['Chromossome','First_index', 'Last_index', "Citoband", 'Unkown'])
    for row in df.values:
        cito_array = []
        if row[0] == chomossome:
            for col in row:
                cito_array.append(col)
            chr_array.append(cito_array)
    return pd.DataFrame(chr_array, columns=df.columns)


def plotAll(cb_df):
    figure, axis = plt.subplots(4, 6)
    chromossomes = cb_df["Chromossome"].unique()
    chr_n = 0
    for i in range(4):
        for j in range(6):
            chr_df = getChromossome(cb_df, chromossomes[chr_n])
            axis[i, j].plot(chr_df["Citoband"], chr_df["STR_Density"], 'ro--', linewidth=2, markersize=6)
            plt.xlabel("Citoband")
            plt.ylabel("STR_density")
            plt.grid()
            axis[i, j].set_title("STR densities in chromossome: " + chromossomes[chr_n])
            chr_n += 1
            #axis.invert_yaxis()
    plt.show() 

def plot_1chr(cb_df, chromossome):
    chr_df = getChromossome(cb_df, str(chromossome))
    plt.figure(figsize=(20,10))
    plt.plot(chr_df["Citoband"], chr_df["STR_Density"], 'ro--', linewidth=2, markersize=6)
    plt.xlabel("Cytoband")
    plt.ylabel("STR_density")
    plt.grid()
    plt.title('STR density in chromosome ' + chromossome)
    plt.show()


citoPath_read = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_processed_complete.txt"

cb_df = pd.read_csv(citoPath_read, sep="\t")
#plotAll(cb_df)

plot_1chr(cb_df, "chr18")
