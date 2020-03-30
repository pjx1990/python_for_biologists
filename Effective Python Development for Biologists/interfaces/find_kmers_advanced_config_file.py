from __future__ import division
import collections
from tqdm import tqdm
import kmer_config_advanced as cfg

dna = open(cfg.input_filename).read().rstrip("\n")

for kmer_length in cfg.kmer_lengths:
    print("Counting kmers of length " + str(kmer_length))
    all_kmers = []

    if cfg.show_progressbar:
        iterable = tqdm(range(len(dna) - kmer_length + 1))
    else:
        iterable = range(len(dna) - kmer_length + 1)

    for start in iterable:
        kmer = dna[start:start+kmer_length]
        all_kmers.append(kmer)

    kmer_counts = collections.Counter(all_kmers)
    total_count = len(all_kmers)

    for kmer, count in kmer_counts.items():
        fraction = count / total_count
        if fraction > cfg.threshold:
            print(kmer, count, fraction)