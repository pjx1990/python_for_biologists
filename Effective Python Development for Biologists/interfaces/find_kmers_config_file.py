from __future__ import division
import collections
import kmer_config


dna = open(kmer_config.input_filename).read().rstrip("\n") 
all_kmers = [] 
for start in range(len(dna) - kmer_config.kmer_length + 1): 
    kmer = dna[start:start+kmer_config.kmer_length] 
    all_kmers.append(kmer) 
 
kmer_counts = collections.Counter(all_kmers) 
total_count = len(all_kmers) 
 
for kmer, count in kmer_counts.items(): 
    fraction = count / total_count 
    if fraction > kmer_config.threshold: 
        print(kmer, count, fraction)