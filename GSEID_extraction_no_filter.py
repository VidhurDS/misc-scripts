from Bio import Entrez
import sys

infile = "all_enzymes.txt"
outfile = "epi_enzyme_prelim_study_search_no_filter.txt"

thefile = open(outfile, 'w')

with open(infile, "r") as ins:
    fullfile = ins.readlines()
ins.close()
c = 0

mainarray = []

for fn in fullfile:
    c += 1
    gn = fn.strip()
    temp = gn.split("|")
    gn = " OR ".join(temp)
    gn = "(" + gn + ")"
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
        #print record
        inst = "\t".join([a, b])
        mainarray.append(inst)
        #print inst
        thefile.write(inst)
        thefile.write("\n")

mainarray = set(mainarray)
print(len(mainarray))
