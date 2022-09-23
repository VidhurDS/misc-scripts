
# reading files
material_fn = "material_type_keywords.txt"
prop_fn = "properties_keywords.txt"
corpus_fn = "solar_pero_merged.txt"
# material_array = []
# properties_array = []
# corpus_array = []

with open(material_fn, "r") as ins:
    material_array = ins.readlines()    # ins.readlines()[1:] if header
ins.close()

with open(prop_fn, "r") as ins2:
    properties_array = ins2.readlines()    # ins.readlines()[1:] if header
ins2.close()

with open(corpus_fn, "r") as ins3:
    corpus_array = ins3.readlines()    # ins.readlines()[1:] if header
ins3.close()

out_fn = "parsed_corpus_table1.txt"
outfile = open(out_fn, 'w')

# total 45070 lines
# print(len(corpus_array))
clean_corpus_array = []

# removing empty lines
for line in corpus_array:
    if line != "\n":
        # outfile.write(line)
        line = line.strip()
        clean_corpus_array.append(line)


# total 19946 lines after removing new lines
# print(len(clean_corpus_array))
# total abstract: 2851

# corpus structure
# index 0-title
# 1-author
# 2-journal,doi
# 3-abstract
# 4-citings
# 5-tags


# create abstract array
# doi based dictionary
temp = []
title = {}
author = {}
journal = {}
abstract = {}
citings = {}

for line in clean_corpus_array:
    line = line.strip()
    line = str(line)
    if line.startswith("Copyright"):
        # get doi
        if "DOI" in temp[2]:
            doi = temp[2].split(", ")[-1]
        else:
            # cleaning up doi if actual DOI not present
            doi = temp[2].replace(" ", "")
            doi = doi.replace("From", "")
            doi = doi.replace("Language: English", "")
            doi = doi.replace("Language:English", "")
        # feeding dictionary based on doi
        title[doi] = temp[0]
        author[doi] = temp[1]
        journal[doi] = temp[2]
        abstract[doi] = temp[3]
        citings[doi] = temp[4]
        # outfile.write(doi + "\n")
        temp = []
        doi = ''
    else:
        temp.append(line)


def checkIfAny(mainStr, listOfStr):
    kstr = ''
    for subStr in listOfStr:
        subStr = subStr.strip()
        count = mainStr.count(subStr)
        kstr = kstr + str(count) + "\t"
    return kstr.strip("\t")


#add both arrays into one
both_array = material_array + properties_array
both_array = map(lambda s: s.strip(), both_array)
header = "\t".join(both_array)
outfile.write("DOI\t" + header + "\n")

for key in title:
    # send as lowercase list
    mstr = str(title[key]) + " " + str(abstract[key])
    ostr = checkIfAny(mstr, both_array)
    numlist = ostr.split("\t")
    numlist = map(int, numlist[1:])
    s = sum(numlist)
    if s > 0:
        outfile.write(key + "\t" + ostr + "\n")
