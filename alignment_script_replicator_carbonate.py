with open("fastqs.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

key_arr = []
for line in array:
    line = line.strip()
    fastq_1, fastq_2 = line.split(",")
    key_str = fastq_1[8:13].strip("-")
    key_arr.append(key_str)
    with open("scripts/" + str(key_str) + "_alignment.sh", "w") as f:
        print>> f, """#!/bin/bash
#PBS -M swapdaul@iu.edu
#PBS -l nodes=1:ppn=16,walltime=0:10:0:00
#PBS -l vmem=16gb
#PBS -m abe
#PBS -N %s_alignment
#PBS -j oe


module load samtools/1.9
module load hisat2/2.1.0

cd /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/3.alignment
hisat2 --rna-strandness RF --dta -q -p 16 -x /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/3.alignment/rn6_HISAT2_index/rn6/genome -1 /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/1.Data/raw_fastqs/%s -2 /N/dc2/projects/CancerFight/Vidhur/Boris_LRAP/1.Data/raw_fastqs/%s -S %s.sam
samtools view -S -b %s.sam > %s.bam
samtools sort %s.bam %s.sorted
samtools index %s.sorted.bam

""" % (str(key_str), str(fastq_1), str(fastq_2), str(key_str), str(key_str), str(key_str), str(key_str), str(key_str), str(key_str))

key_arr = set(key_arr)
k = open("qsub_alignment_code.txt", "w")

for i in key_arr:
    i = i.strip()
    k.write("dos2unix %s_alignment.sh\n" % (str(i)))

for i in key_arr:
    i = i.strip()
    k.write("qsub %s_alignment.sh\n" % (str(i)))

