from __future__ import division
import collections
import sys

input_filename = sys.argv[1] 
kmer_length = int(sys.argv[2])
count_threshold = int(sys.argv[3])
output_filename = sys.argv[4]

if kmer_length < 1:
    print("kmer length must be positive") 
    sys.exit()

if count_threshold < 100:
    print("warning: a low threshold produces a lot of output") 

dna = open(input_filename).read().replace("\n", "")

kmer_counts = collections.Counter()

print("counting kmers of length " + str(kmer_length)) 
for start in range(len(dna) - kmer_length + 1):
    kmer = dna[start:start+kmer_length]
    kmer_counts.update([kmer])

total_count = sum(kmer_counts.values())

with open(output_filename, "w") as output:
    for kmer, count in kmer_counts.items():
        print("count for " + kmer + " is " + str(count)) 
        if count > count_threshold:
                output.write(kmer + " " + str(count) + "\n")