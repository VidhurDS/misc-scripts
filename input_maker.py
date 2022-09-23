# with open("sample_RBP_lncRNA_binding_sites_FIMO_human.txt", "r") as ins:
with open("RBP_lncRNA_binding_sites_FIMO_human.txt", "r") as ins:
    fimo = ins.readlines()[1:]    # ins.readlines()[1:] if header
ins.close()

with open("lncRNA_RBP_correlation_FDR_0.05.txt", "r") as ins:
    correlation_file = ins.readlines()[1:]    # ins.readlines()[1:] if header
ins.close()

outfile = open("RBP_lncRNA_binding_sites_FIMO_correlation_human.txt", 'w')

coor_dict = {}

# making lnc_ENSG - RBP dictionary
for line in correlation_file:
    line = line.strip()
    ele = line.split("\t")
    ensg = ele[1]
    rbp = ele[2]
    r_value = float(ele[3])
    keystr = ensg + "|" + rbp
    coor_dict[keystr] = r_value

rbp_list = []
lnc_list = []
for line in fimo:
    line = line.strip()
    ele = line.split("\t")
    rbp = ele[0]
    temp = ele[3].split(".")
    ensg = temp[0]
    kstr = ensg + "|" + rbp
    if kstr in coor_dict:
        rbp_list.append(rbp)
        lnc_list.append(ensg)
        outfile.write(ele[2] + "\t" + ensg + "\t" + rbp + "\t" + ele[1] + "\t" + str(float(ele[8])) + "\t" + str(float(ele[9])) + "\t" + ele[10] + "\t" + str(coor_dict[kstr]) + "\n")

rbp_list = set(rbp_list)
lnc_list = set(lnc_list)

print "number of lncRNAs: " + str(len(lnc_list))
print "number of RBPs: " + str(len(rbp_list))
