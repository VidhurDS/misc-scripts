with open("IDs.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)


for i in array:
    i = i.strip()
    with open("scripts/" + str(i) + "_download.sh", "w") as f:
        print>> f, """#!/bin/bash

#PBS -N %s_download
#PBS -l nodes=1:ppn=8,walltime=00:20:00

module load sra-toolkit/2.8.2
cd /N/dc2/projects/CancerFight/Vidhur/label_prediction/KO_study_validation/1.download/fastqs

fastq-dump %s -O /N/dc2/projects/CancerFight/Vidhur/label_prediction/KO_study_validation/1.download/fastqs/

""" % (str(i), str(i))

k = open("qsub_download_code.txt", "w")

for i in array:
    i = i.strip()
    k.write("qsub %s_download.sh\n" % (str(i)))

for i in array:
    i = i.strip()
    k.write("dos2unix %s_download.sh\n" % (str(i)))

# for i in array:
#     i = i.strip()
#     k.write("/gpfs/home/s/w/swapdaul/BigRed2/sratoolkit.2.8.2-1-ubuntu64/bin/fastq-dump %s -O /N/dc2/projects/CancerFight/Vidhur/label_prediction/KO_study_validation/1.download/fastqs\n" % (str(i)))

