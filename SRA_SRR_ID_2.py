from Bio import Entrez, Medline
import re
# import xml.etree.ElementTree as ET


with open("srr_info_new2.txt", "r") as ins:
    fullfile = ins.readlines()
ins.close()

outfile = open("GEO_SRR_SRA_IDs_raw2.txt", 'w')
outfile.write("lncRNA_name\tGEO_study\tSRA_UIDs\txml_data\n")
c = 0

for line in fullfile:
    c +=1
    line = line.strip()
    ele = line.split("\t")
    name = ele[0]
    geo_id = ele[1]
    sra_id_list = ele[2].split(",")
    for singleid in sra_id_list:
        initial_ids = name + "\t" + geo_id + "\t" + singleid
        Entrez.email = "swapdaul@iupui.edu"
        handle = Entrez.esummary(db="sra", id=singleid)
        try:
            records = Entrez.read(handle)
            handle.close()
            ostr = initial_ids + "\t" + str(records)
            outfile.write(ostr + "\n")
        except:
            print "This is an error message!"

    print c
