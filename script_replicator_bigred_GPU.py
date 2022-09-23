with open("IDs.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

for i in array:
    i = i.strip()
    with open(str(i) + "_download.sh", "w") as f:
        print>> f, """#!/bin/bash
#PBS -l nodes=1:ppn=16 
#PBS -l walltime=10:00:00
#PBS -l gres=ccm
#PBS -q gpu
#PBS -N download_%s

module load ccm

cd /N/dc2/projects/CancerFight/Vidhur/fastqs_GSE79249

ccmrun /gpfs/home/s/w/swapdaul/BigRed2/sratoolkit.2.8.2-1-ubuntu64/bin/fastq-dump --split-files --gzip %s

""" % (str(i), str(i))

k = open("qsub_download_code.txt", "w")

for i in array:
    i = i.strip()
    k.write("qsub %s_download.sh\n" % (str(i)))

for i in array:
    i = i.strip()
    k.write("dos2unix %s_download.sh\n" % (str(i)))
