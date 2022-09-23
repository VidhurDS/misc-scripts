#with open("sample_RBP_lncRNA_binding_sites_FIMO_human.txt", "r") as ins:
with open("RBP_lncRNA_binding_sites_FIMO_human.txt", "r") as ins:
    fimo = ins.readlines()[1:]    # ins.readlines()[1:] if header
ins.close()

with open("lncRNA_RBP_correlation_FDR_0.05.txt", "r") as ins:
    correlation_file = ins.readlines()[1:]    # ins.readlines()[1:] if header
ins.close()

outfile = open("RBP_lncRNA_binding_sites_FIMO_correlation_human.txt", 'w')

f_lnc = []
f_ensg = []
c_lnc = []
c_ensg = []


def common_items(list1,list2):
    temp2 = list(set(list1).intersection(list2))
    return len(temp2)


f_rbp = []
c_rbp = []

for line in fimo:
    line = line.strip()
    ele = line.split("\t")
    f_lnc.append(ele[2])
    temp = ele[3].split(".")
    f_ensg.append(temp[0])
    f_rbp.append(ele[0])

f_lnc = set(f_lnc)
f_ensg = set(f_ensg)
f_rbp = set(f_rbp)

for line in correlation_file:
    line = line.strip()
    ele = line.split("\t")
    c_lnc.append(ele[0])
    c_ensg.append(ele[1])
    c_rbp.append(ele[2])

c_lnc = set(c_lnc)
c_ensg = set(c_ensg)
c_rbp = set(c_rbp)

print "lnc"
print common_items(f_lnc, c_lnc)
print "ensg"
print common_items(f_ensg, c_ensg)
print "common RBP"
print common_items(f_rbp, c_rbp)


# ensg identifies 5800 lncrna, therefore using ensg
