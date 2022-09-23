from Bio import Entrez
import sys

infile = "epi_enzyme_list.txt"
outfile = "epi_enzyme_search_result.txt"

thefile = open(outfile, 'w')

with open(infile, "r") as ins:
    fullfile = ins.readlines()
ins.close()
c = 0

mainarray = []
id_array = []

for fn in fullfile:
    c += 1
    gn = fn.strip()
    if "|" in gn:
        temp = gn.split("|")
        gn = " OR ".join(temp)
        gn = "((((epitranscriptome OR epitranscriptomic OR RNA modification OR RNA methylation)) AND \"rna\"[MeSH Terms]) AND RNA) AND (" + gn + ")"
    else:
        gn = "((((epitranscriptome OR epitranscriptomic OR RNA modification OR RNA methylation)) AND \"rna\"[MeSH Terms]) AND RNA) AND " + gn

    #print gn
    handle = ''
    Entrez.email = "swapdaul@iupui.edu"     # Always tell NCBI who you are
    handle = Entrez.esearch(db="gds", term=gn, retmax=500)
    # print handle
    record = Entrez.read(handle)

    a = ''
    b = ''
    a = fn.strip()
    b = ",".join(record["IdList"])
    print c
    if b:
        # print b
        id_array = id_array + record["IdList"]
        inst = "\t".join([a, b])
        mainarray.append(inst)
        #print inst
        thefile.write(inst)
        thefile.write("\n")

mainarray = set(mainarray)
id_array = set(id_array)
print(len(mainarray))
print(len(id_array))
