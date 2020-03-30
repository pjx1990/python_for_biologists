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

parser.add_argument(
    "-o",
    "--output_type",
    choices=['count', 'proportion', 'percentage'],
    default = 'proportion'
    )


threshold_group = parser.add_mutually_exclusive_group(required=True) 
 
threshold_group.add_argument( 
    "--proportion_threshold", 
    help="minimum proportion of a kmer to be printed (between 0 and 1)", 
    type=float 
    ) 
 
threshold_group.add_argument( 
    "--percentage_threshold", 
    help="minimum percentage of a kmer to be printed (between 0 and 100)", 
    type=float 
    ) 
 
threshold_group.add_argument( 
    "--count_threshold", 
    help="minimum count of a kmer to be printed (positive integer)", 
    type=int 
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

    # figure out the count threshold 
    if args.count_threshold is not None: 
        print("Using count threshold " + str(args.count_threshold)) 
        count_threshold = args.count_threshold 

    elif args.proportion_threshold is not None: 
        print("Using proportion threshold " + str(args.proportion_threshold)) 
        count_threshold = total_count * args.proportion_threshold 

    elif args.percentage_threshold is not None: 
        print("Using percentage threshold " + str(args.percentage_threshold)) 
        count_threshold = total_count * (args.percentage_threshold / 100)
     
    for kmer, count in kmer_counts.items(): 
        fraction = count / total_count 
        if count > count_threshold: 
            if args.output_type == 'proportion': 
                print(kmer, count / total_count) 
            elif args.output_type == 'percentage': 
                print(kmer, (count / total_count) * 100) 
            elif args.output_type == 'count': 
                print(kmer, count)