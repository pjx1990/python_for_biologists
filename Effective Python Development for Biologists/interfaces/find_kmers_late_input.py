from __future__ import division
import collections

input_filename = raw_input("Enter the input file name:\n")
kmer_length = int(raw_input("Enter the kmer length:\n"))

dna = open(input_filename).read().rstrip("\n")
all_kmers = []
for start in range(len(dna) - kmer_length + 1):
    kmer = dna[start:start+kmer_length]
    all_kmers.append(kmer)

kmer_counts = collections.Counter(all_kmers)
total_count = len(all_kmers)

threshold = float(raw_input("Enter the threshold:\n"))
for kmer, count in kmer_counts.items():
    fraction = count / total_count
    if fraction > threshold:
        print(kmer, count, fraction)