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
    plt.savefig("")

def makeMap_cb(cb_df):
    chromossomes = cb_df["Chromossome"].unique()
    chromossomes = list(map(str, chromossomes))
    chromossomes.remove("chrM")
    cytobands = cb_df["Citoband"].unique()
    cytobands = list(map(str, cytobands))
    mapping = []
    for chromosome in chromossomes:
        chr_subset = cb_df.get(cb_df["Chromossome"] == chromosome)
        citobands = chr_subset["Citoband"].unique()
        ps = np.zeros(45, dtype=(str, 6))
        qs = np.zeros(45, dtype=(str, 6))
        pcount = -1
        qcount = 0
        for cytoband in citobands:
            if cytoband[0] == "p":
                ps[pcount] = cytoband
                pcount -= 1
            elif cytoband[0] == "q":
                qs[qcount] = cytoband
                qcount += 1
        ps_list = ps.tolist()
        qs_list = qs.tolist()
        pqs = ps_list + qs_list
        mapping.append(citobands.tolist())
        mapping.append(pqs)
    print("mapping: ", mapping)


def makeMap_dens(cb_df):
    chromossomes = cb_df["Chromossome"].unique()
    chromossomes = list(map(str, chromossomes))
    chromossomes.remove("chrM")
    cytobands = cb_df["Citoband"].unique()
    cytobands = list(map(str, cytobands))
    mapping = []
    row_count = 0
    for chromosome in chromossomes:
        chr_subset = cb_df.get(cb_df["Chromossome"] == chromosome)
        cytobands = chr_subset["Citoband"].unique()
        ps = np.zeros(45, dtype=(float, 6))
        qs = np.zeros(45, dtype=(float, 6))
        pcount = -1
        qcount = 0
        count = row_count
        if chromosome == "chrX" or chromosome == "chrY":
            count += 1
        for row in range (len(chr_subset.values)):
            if count>=63:
                row += count
            cytoband = chr_subset["Citoband"][row]
            str_density = chr_subset["STR_Density"][row]
            if cytoband[0] == "p":
                ps[pcount] = str_density
                pcount -= 1
            elif cytoband[0] == "q":
                qs[qcount] = str_density
                qcount += 1
            row_count+=1
        ps_list = ps.tolist()
        qs_list = qs.tolist()
        pqs = ps_list + qs_list
        mapping.append(cytobands.tolist())
        mapping.append(pqs)
    print("mapping: ", mapping)
    return mapping



def makeMap_dict(cb_df):
    chromossomes = cb_df["Chromossome"].unique()
    chromossomes = list(map(str, chromossomes))
    chromossomes.remove("chrM")
    print(chromossomes)
    cytobands = cb_df["Citoband"].unique()
    cytobands = list(map(str, cytobands))
    
    mapping = {}
    row_count = 0
    for chromosome in chromossomes:
        #print("\nchromosome: ", chromosome)
        chr_subset = cb_df.get(cb_df["Chromossome"] == chromosome)
        #print("chr_subset: ", chr_subset)
        #print("type: ", type(chr_subset))
        #print("cytobands of chromosome ", chromosome, ":\n", chr_subset["Citoband"])
        ps = np.zeros(45, dtype=(list, 2))
        qs = np.zeros(45, dtype=(list, 2))
        pcount = -1
        qcount = 0
        count = row_count
        if chromosome == "chrX" or chromosome == "chrY":
            count += 1
        for row in range (len(chr_subset.values)):
            if count>=63:
                row += count
            cytoband = chr_subset["Citoband"][row]
            str_density = chr_subset["STR_Density"][row]
            if cytoband[0] == "p":
                ps[pcount] = [cytoband, str_density]
                pcount -= 1
            elif cytoband[0] == "q":
                qs[qcount] = [cytoband, str_density]
                qcount += 1
            row_count+=1
        ps_list = ps.tolist()
        qs_list = qs.tolist()
        #print("ps: ", ps_list)
        #print("qs: ", qs_list)
        pqs = ps_list + qs_list

        #print("nº de cytobands no cromossoma:", chromosome, ": ", len(citobands))
        #print("pqs: ", pqs)

        #mapping.append(citobands.tolist())
        mapping.update({chromosome : pqs})
    print("mapping: ", mapping)
    return mapping

def plotMap(data):
    #x = chromossomes#[0]
    #y = mapping#[0]
    #x=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
    #plt.xticks(x,chromossomes)

    #plt.plot(x, y)
    #plt.xticks(x,chromossomes)

    #the_table = plt.table(cellText=cell_text,
    #                  rowLabels=row_headers,
    #                  rowColours=rcolors,
    #                  colLabels=column_headers,
    #                  loc='center')
    
    
    #the_table.scale(1, 1.5)

    plt.savefig('pyplot-table-figure-style.png',
            bbox_inches='tight',
            #edgecolor=fig.get_edgecolor(),
            #facecolor=fig.get_facecolor(),
            dpi=150
            )
    #plt.show()

citoPath_read = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_processed_complete.txt"

cb_df = pd.read_csv(citoPath_read, sep="\t")

#print(cb_df)
#plotAll(cb_df)

#plot_1chr(cb_df, "chrM")

#makeMap_cb(cb_df)

makeMap_dens(cb_df)

#plotMap(cb_df)
