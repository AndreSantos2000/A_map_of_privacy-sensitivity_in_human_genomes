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
        ps = np.zeros(40, dtype=(str, 6))
        qs = np.zeros(40, dtype=(str, 6))
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
    print(chromossomes)
    for chromosome in chromossomes:
        chr_subset = cb_df.get(cb_df["Chromossome"] == chromosome)
        cytobands = chr_subset["Citoband"].unique()
        ps = np.zeros(34, dtype=(float, 1))
        qs = np.zeros(38, dtype=(float, 1))
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
        #print(ps_list)
        #print(qs_list)
        pqs = ps_list + qs_list
        #mapping.append(cytobands.tolist())
        mapping.append(pqs)
    print("mapping: ", mapping[11])
    print("mapping length: ", len(mapping))
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

def plotMap(data, dict):
    
    #mais tarde inverter as linhas com as colunas
    rows = ('chr1', 'chr10', 'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr2', 'chr20', 'chr21', 'chr22', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chrX', 'chrY')
    cols = ["p34", "p33", "p32", "p31", "p30", "p29", "p28", "p27", "p26", "p25", "p24", "p23", "p22", "p21", "p20", "p19", "p18", "p17", "p16", "p15", "p14", "p13", "p12", "p11", "p10", "p09", "p08", "p07", "p06", "p05", "p04", "p03", "p02", "p01-centromer", "q01-centromer", "q02", "q03", "q04", "q05", "q06", "q07", "q08", "q09", "q10", "q11", "q12", "q13", "q14", "q15", "q16", "q17", "q18", "q19", "q20", "q21", "q22", "q23", "q24", "q25", "q26", "q27", "q28", "q29", "q30", "q31", "q32", "q33", "q34", "q35", "q36", "q37", "q38"]
    
    n_rows = len(data)
    n_cols = len(data[0])

    #index = np.arange(len(columns)) + 0.3
    index = np.arange(len(rows)) + 0.3
    bar_width = 0.4

    # Initialize the vertical-offset for the stacked bar chart.
    y_offset = np.zeros(len(rows))

    # Plot bars and create text labels for the table
    cell_text = []
    for row in range(n_rows):
        #plt.bar(index, data[row], bar_width, bottom=y_offset)#, color=colors[row])
        #y_offset = y_offset + data[row]
        #cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
        cell_text.append(data[row])

    #Get some lists of color specs for row and column headers
    rcolors = plt.cm.BuPu(np.full(len(rows), 0.1))
    ccolors = plt.cm.BuPu(np.full(len(cols), 0.1))
    cellcolours = plt.cm.YlOrRd(data)                     #coolwarm, Greys

    plt.figure(linewidth=2,
           #edgecolor=fig_border,
           #facecolor=fig_background_color,
           tight_layout={'pad':1},
           figsize = (72,24),
          )
    

    the_table = plt.table(cellText=cell_text,
                      rowLabels=rows,
                      colLabels=cols,
                      rowLoc='right',
                      rowColours=rcolors,
                      colColours=ccolors,
                      cellColours=cellcolours,
                      loc='center')
    
    the_table.scale(1, 2)
    # Hide axes
    ax = plt.gca()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    
    # Hide axes border
    plt.box(on=None)
    
    # Add title
    plt.suptitle("STR density in human genome")
    
    
    # Force the figure to update, so backends center objects correctly within the figure.
    # Without plt.draw() here, the title will center on the axes and not the figure.
    plt.draw()
    
    # Create image. plt.savefig ignores figure edge and face colors, so map them.
    fig = plt.gcf()
    
    plt.savefig('STR_density_in_human_genome.png',
            #bbox='tight',
            #edgecolor=fig.get_edgecolor(),
            #facecolor=fig.get_facecolor(),
            dpi=150
            )
    
    #plt.subplots_adjust(left=0.2, bottom=0.2)
    
    #plt.xlabel("Citobands")
    #plt.ylabel("STRs density")
    #plt.yticks(values * value_increment, ['%d' % val for val in values])
    
    #plt.xticks([])
    #plt.title('STR density in human genome')

    #plt.show()

    #plt.plot(x, y)
    #plt.xticks(x,chromossomes)
    #the_table.scale(1, 1.5)
    #plt.show()



citoPath_read = "/home/androx/Documents/trabalho/citobands/cytobandFiltered_processed_complete.txt"

cb_df = pd.read_csv(citoPath_read, sep="\t")

#print(cb_df)
#plotAll(cb_df)

#plot_1chr(cb_df, "chrM")

#makeMap_cb(cb_df)

dens_map = makeMap_dens(cb_df)

plotMap(dens_map)

#plotMap(cb_df)
