from Bio import Entrez
import sys

infile = "enzymes.txt"
outfile = "prelim.txt"

thefile = open(outfile, 'w')

with open(infile, "r") as ins:
    fullfile = ins.readlines()
ins.close()
c = 0

mainarray = []

for fn in fullfile:
    c += 1
    gn = fn.strip()
    if "," in gn:
        temp = gn.split(",")
        gn = "[Description] OR ".join(temp)
        gn = gn + "[Description]"
        gn = "(((epitranscriptome enzyme[Description] OR RNA modification[Description])) " \
             "AND (" + gn + ")) " \
             "AND (knocked down[Description] OR was knocked down[Description] OR knockdown of[Description] OR knocked out[Description] OR knockout of[Description] OR was knocked out[Description] OR knocked-down[Description] OR was knocked-down[Description] OR knockdown of[Description] OR knocked-out[Description] OR knockout of[Description] OR was knocked-out[Description] OR up regulated[Description] OR up regulation of[Description] OR up-regualted[Description] OR silencing of[Description] OR silenced[Description] OR was silenced[Description])"
    else:
        # gn = "(((((lncRNA[Description] OR long non coding RNA[Description] OR non coding RNA[Description])) AND " + gn + "[Description]) AND (knockout[Description] OR knockdown[Description] OR down regulate[Description] OR up regulate[Description] OR over expression[Description])) AND (RNA sequencing[Description] OR expression profile[Description] OR transcriptome[Description])) NOT chip-seq"
        gn = "((((epitranscriptome enzyme[Description] OR RNA modification[Description])) " \
             "AND " + gn + "[Description]) " \
             "AND (knocked down[Description] OR was knocked down[Description] OR knockdown of[Description] OR knocked out[Description] OR knockout of[Description] OR was knocked out[Description] OR knocked-down[Description] OR was knocked-down[Description] OR knockdown of[Description] OR knocked-out[Description] OR knockout of[Description] OR was knocked-out[Description] OR up regulated[Description] OR up regulation of[Description] OR up-regualted[Description] OR silencing of[Description] OR silenced[Description] OR was silenced[Description])"

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
