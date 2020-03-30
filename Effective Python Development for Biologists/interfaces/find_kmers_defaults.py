from __future__ import division
import collections
from tqdm import tqdm
import argparse

def check_float(threshold):
    result = float(threshold)
    if not 0 < result < 1:
        raise argparse.ArgumentTypeError("Threshold must be between 0 and 1")
    return result

def check_kmer_length(kmer_length):
    result = int(kmer_length)
    if result < 1:
        raise argparse.ArgumentTypeError("Kmer length must be greater than 0")
    return result  

parser = argparse.ArgumentParser()
parser.add_argument("input_filename", help="the name of your DNA sequence file")

parser.add_argument( 
    "-k", 
    "--kmer_length", 
    help="length of the kmers (default: 4)", 
    type=check_kmer_length, 
    default=4 
    ) 

parser.add_argument( 
    "-t", 
    "--threshold", 
    help="minimum fraction of a kmer to be printed (default: 0.01)", 
    type=check_float, 
    default=0.01)



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