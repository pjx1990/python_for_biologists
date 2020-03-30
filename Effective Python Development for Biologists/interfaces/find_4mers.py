from __future__ import division
import collections

dna = open("dna.txt").read().rstrip("\n")
all_fourmers = []

for start in range(len(dna) - 3):
    fourmer = dna[start:start+4]
    all_fourmers.append(fourmer)
    
fourmer_counts = collections.Counter(all_fourmers)
total_count = len(all_fourmers)

for fourmer, count in fourmer_counts.items():
    fraction = count / total_count
    if fraction > 0.01:
        print(fourmer, count, fraction)