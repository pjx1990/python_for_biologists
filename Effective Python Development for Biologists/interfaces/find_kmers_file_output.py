from __future__ import division
import collections
import sys

input_filename = sys.argv[1] 
kmer_length = int(sys.argv[2])
count_threshold = int(sys.argv[3])
output_filename = sys.argv[4]

dna = open(input_filename).read().replace("\n", "") 

kmer_counts = collections.Counter()

for start in range(len(dna) - kmer_length + 1): 
    kmer = dna[start:start+kmer_length]
    kmer_counts.update([kmer]) 

total_count = sum(kmer_counts.values())

with open(output_filename, "w") as output:
    for kmer, count in kmer_counts.items():
        if count > count_threshold:
                output.write(kmer + " " + str(count) + "\n")