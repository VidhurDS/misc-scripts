with open("lnc_protein_pval_FDR.txt", "r") as ins:
    fdr = ins.readlines()[1:]    # ins.readlines()[1:] if header
ins.close()

with open("RBP_list_155.txt", "r") as ins:
    rbps = ins.readlines()   # ins.readlines()[1:] if header
ins.close()

outfile = open("lncRNA_RBP_correlation_FDR_0.05.txt", 'w')

rbps = map(lambda s: s.strip(), rbps)

for line in fdr:
    line = line.strip()
    ele = line.split("\t")
    if ele[1] in rbps and float(ele[4]) < 0.05:
        outfile.write(line + "\n")
