from __future__ import division
import collections

input_filename = "dna.txt"
kmer_length = 4
threshold = 0.01

dna = open(input_filename).read().rstrip("\n")
all_kmers = []
for start in range(len(dna) - kmer_length + 1):
    kmer = dna[start:start+kmer_length]
    all_kmers.append(kmer)

kmer_counts = collections.Counter(all_kmers)
total_count = len(all_kmers)

for kmer, count in kmer_counts.items():
    fraction = count / total_count
    if fraction > threshold:
        print(kmer, count, fraction)