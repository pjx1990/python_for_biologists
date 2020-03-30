from __future__ import division
import collections
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_filename", help="the name of your DNA sequence file")
args = parser.parse_args()

kmer_length = 4
threshold = 0.01

dna = open(args.input_filename).read().rstrip("\n") 

all_kmers = []
for start in tqdm(range(len(dna) - kmer_length + 1)):
    kmer = dna[start:start+kmer_length]
    all_kmers.append(kmer)

kmer_counts = collections.Counter(all_kmers)
total_count = len(all_kmers)

for kmer, count in kmer_counts.items():
    fraction = count / total_count
    if fraction > threshold:
        print(kmer, count, fraction)