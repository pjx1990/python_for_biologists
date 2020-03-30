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
    help="length of the kmers (greater than 0)", 
    type=check_kmer_length, 
    nargs = '*',
    default=[4,6,8] 
    )

parser.add_argument( 
    "-t", 
    "--threshold", 
    help="minimum fraction of a kmer to be printed (default: 0.01)", 
    type=check_float, 
    default=0.01)

parser.add_argument( 
    "-p", 
    "--progress", 
    help="show progress bar (T or F)", 
    action="store_true" 
    )

args = parser.parse_args()

for kmer_length in args.kmer_length:
    print("Counting kmers of length " + str(kmer_length))
    dna = open(args.input_filename).read().rstrip("\n") 

    kmer_counts = collections.Counter() 

    if args.progress: 
        iterable = tqdm(range(len(dna) - kmer_length + 1)) 
    else: 
        iterable = range(len(dna) - kmer_length + 1)

    for start in iterable: 
        kmer = dna[start:start+kmer_length] 
        kmer_counts.update([kmer]) 
     
    total_count = sum(kmer_counts.values()) 
     
    for kmer, count in kmer_counts.items(): 
        fraction = count / total_count 
        if fraction > args.threshold: 
            print(kmer, count, fraction)