from __future__ import division
import collections
from tqdm import tqdm
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_filename", help="the name of your DNA sequence file")
parser.add_argument(
    "kmer_length", 
    help="length of the kmers", 
    type=int)
parser.add_argument( 
    "threshold", 
    help="minimum fraction of a kmer to be printed", 
    type=float)
args = parser.parse_args()



dna = open(args.input_filename).read().rstrip("\n") 

kmer_counts = collections.Counter() 
for start in tqdm(range(len(dna) - args.kmer_length + 1)): 
    kmer = dna[start:start+args.kmer_length] 
    kmer_counts.update([kmer]) 
 
total_count = sum(all_kmers.values) 
 
for kmer, count in kmer_counts.items(): 
    fraction = count / total_count 
    if fraction > args.threshold: 
        print(kmer, count, fraction)