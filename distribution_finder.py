infile = "epi_enzyme_prelim_study_search_no_filter.txt"
outfile = "distribution_epi_enzyme_prelim_study_search_no_filter.txt"

thefile = open(outfile, 'w')

with open(infile, "r") as ins:
    fullfile = ins.readlines()[1:]
ins.close()
c = 0

count = {}

for fn in fullfile:
    gn = fn.strip()
    temp = gn.split("\t")
    ids = temp[1].split(",")
    for each_id in ids:
        if each_id in count:
            count[each_id] += 1
        else:
            count[each_id] = 1

for key in count:
    thefile.write(key + "\t" + str(count[key]) + "\n")
