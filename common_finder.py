file1 = ""
f1 = []
f2 = []
with open(file1, "r") as ins:
    f1 = ins.readlines()    # ins.readlines()[1:] if header
ins.close()

file2 = ""
with open(file2, "r") as ins2:
    f2 = ins2.readlines()  # ins2.readlines()[1:] if header
ins2.close()

ofn = "common.txt"
outfile = open(ofn, 'w')

lnc_dict = {}
pmid_dict = {}

for line in pmid_anno:
    line = line.strip()
    elements = line.split("\t")
    pmid_dict[elements[0]] = elements[1] + "\t" + elements[2]

for each_line in lnc_pmid:
    a = 0
    each_line = each_line.strip()
    array = each_line.split("\t")
    if ";" in array[1]:
        pmids = []
        pmids = array[1].split(";")
        for pm in pmids:
            if pm in pmid_dict:
                if a == 0:
                    outfile.write("\n" + array[0] + "\n")
                    a = 1
                outfile.write(str(pm) + "\t" + pmid_dict[pm] + "\n")
    else:
        if array[1] in pmid_dict:
            outfile.write("\n" + array[0] + "\n")
            a = 1
            outfile.write(str(array[1]) + "\t" + pmid_dict[array[1]] + "\n")



