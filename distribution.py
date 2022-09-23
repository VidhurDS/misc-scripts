# with open("sample_merged.txt", "r") as ins:
with open("merged_FIMO_output.txt", "r") as ins:
    fimo = ins.readlines()    # ins.readlines()[1:] if header
ins.close()

outfile2 = open("RBP_lncRNA_binding_sites_FIMO_human.txt", 'w')
outfile2.write("RBP\tRBP_motif_ID\tlncRNA_name\tlncRNA_ENSG\tlength\tstart\tstop\tscore	p-value	q-value	matched sequence\n")
rbp_arr = []
lnc_arr = []
head_count = 0
for line in fimo:
    line = line.strip()
    if line.startswith("#"):
        head_count += 1
    else:
        ele = line.split("\t")
        t2 = ele[0].split("_")
        rbp = t2[0]
        start = int(ele[2])
        stop = int(ele[3])
        motif_length = abs(start - stop) + 1

        rbp_arr.append(rbp)
        temp = ele[1].split("|")
        lnc_name = temp[5]
        lnc_ensg = temp[1]
        lnc_arr.append(lnc_name)
        ostr = rbp + "\t" + ele[0] + "\t" + lnc_name + "\t" + lnc_ensg + "\t" + str(motif_length) + \
               "\t" + str(start) + "\t" + str(stop) + "\t" + str(ele[5]) + "\t" + str(ele[6]) + "\t" + str(ele[7]) + "\t" + str(ele[8]) + "\n"
        outfile2.write(ostr)

lnc_arr = set(lnc_arr)
rbp_arr = set(rbp_arr)


x = str(len(fimo) - head_count) + " binding sites across " + str(len(rbp_arr)) + " RBPS and " + str(len(lnc_arr)) + " lncRNAs"
print x
print head_count
