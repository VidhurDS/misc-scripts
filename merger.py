with open("GEO_SRR_SRA_IDs.txt", "r") as ins:
    geo_file = ins.readlines()[1:]
ins.close()

with open("PMID_SRR_SRA_IDs.txt", "r") as ins:
    pmid_file = ins.readlines()[1:]
ins.close()

outfile = open("merged_geo_pmid_srr_ids.txt", 'w')
outfile.write("lncRNA_name\tPMID or GEO_UID\tSRA_UID\tCreateDate\tSRR_ids\texp_status\ttitle\tplatform\tsra_accession\texp_accession\tstudy_name\torganism\tsample_accession\tstrategy\tsource\tlibrary_selection\tlibrary_layout\tproject_id\tbiosample_id\n")

resource = {}
lnc_sra = {}
sra_info = {}

for line in geo_file:
    line = line.strip()
    ele = line.split("\t")
    lnc_name = ele[0]
    geo_id = ele[1]
    sra_uid = ele[2]
    info_str = "\t".join(ele[3:len(ele)])
    combo_lnc_sra = lnc_name + "||" + sra_uid

    if combo_lnc_sra in resource:
        resource[combo_lnc_sra].append(geo_id)
    else:
        resource[combo_lnc_sra] = []
        resource[combo_lnc_sra].append(geo_id)

    if sra_uid in sra_info:
        sra_info[sra_uid].append(info_str)
    else:
        sra_info[sra_uid] = []
        sra_info[sra_uid].append(info_str)

    if lnc_name in lnc_sra:
        lnc_sra[lnc_name].append(sra_uid)
    else:
        lnc_sra[lnc_name] = []
        lnc_sra[lnc_name].append(sra_uid)


for line in pmid_file:
    line = line.strip()
    ele = line.split("\t")
    lnc_name = ele[0]
    geo_id = "PMID" + ele[1]
    sra_uid = ele[2]
    info_str = "\t".join(ele[3:len(ele)])
    combo_lnc_sra = lnc_name + "||" + sra_uid

    if combo_lnc_sra in resource:
        resource[combo_lnc_sra].append(geo_id)
    else:
        resource[combo_lnc_sra] = []
        resource[combo_lnc_sra].append(geo_id)

    if sra_uid in sra_info:
        sra_info[sra_uid].append(info_str)
    else:
        sra_info[sra_uid] = []
        sra_info[sra_uid].append(info_str)

    if lnc_name in lnc_sra:
        lnc_sra[lnc_name].append(sra_uid)
    else:
        lnc_sra[lnc_name] = []
        lnc_sra[lnc_name].append(sra_uid)


for rna in resource:
    # re = "||".join(resource[rna])
    # print(rna + " " + re)
    resource[rna] = set(resource[rna])
    # print(rna + " " + re)

for rna in lnc_sra:
    lnc_sra[rna] = set(lnc_sra[rna])

for uid in sra_info:
    sra_info[uid] = set(sra_info[uid])

for rna_sra in resource:
    temp = rna_sra.split("||")
    rna = temp[0]
    sra = temp[1]
    rid = "|".join(resource[rna_sra])
    ostr = "|||".join(sra_info[sra])
    op = rna + "\t" + str(rid) + "\t" + str(sra) + "\t" + ostr + "\n"
    outfile.write(op)
