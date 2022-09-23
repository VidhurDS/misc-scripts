from Bio import Entrez, Medline
# import re
# import xml.etree.ElementTree as ET

with open("GSEIDs_search_full_output_2.txt", "r") as ins:
    fullfile = ins.readlines()
ins.close()

#outfile = open("srr_info.txt", 'w')
outfile = open("srr_info_new.txt", 'w')
outfile.write("lncRNA_name\tGEO_study\tSRA_UIDs\n")
for line in fullfile:
    line = line.strip()
    ele = line.split("\t")
    name = ele[0]
    idlist = ele[1].split(";")
    for singleid in idlist:
        Entrez.email = "swapdaul@iupui.edu"
        # handle = Entrez.elink(dbfrom="gds", id=singleid, linkname="gds_sra", retmode = "text")
        handle = Entrez.elink(db="sra", dbfrom="gds", id=singleid, linkname="gds_sra", retmode = "text",  idtype="acc")
        #gds_sra
        records = Entrez.read(handle)
        #records = str(records)
        handle.close()
        #outfile.write(records + "\n")
        # parsing xml
        for record in records:
            for x in record['LinkSetDb']:
                uids = str(x['Link'])
                uids = uids.replace("'}, {u'Id': '", ",")
                uids = uids.replace("[{u'Id': '", "")
                uids = uids.replace("'}]", "")
                outfile.write(name + "\t" + singleid + "\t" + uids + "\n")

