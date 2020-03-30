from __future__ import division
import collections
from tqdm import tqdm
import sys


if len(sys.argv) != 4: 
    sys.exit("Usage: python count_kmers.py input_filename kmer_length threshold") 
 
input_filename = sys.argv[1] 
try: 
    dna = open(input_filename).read().rstrip("\n") 
except IOError as ex: 
    sys.exit("Sorry, couldn't open the file: " + ex.strerror) 
 
try: 
    kmer_length = float(sys.argv[2]) 
    if not kmer_length.is_integer(): 
        sys.exit("Kmer length must be an integer") 
    kmer_length = int(kmer_length) 
except ValueError as ex: 
    sys.exit("Invalid input for the kmer length" ) 
    
try: 
    threshold = float(sys.argv[3]) 
    if not 0 < threshold < 1: 
        sys.exit("Threshold must be between 0 and 1") 
except ValueError as ex: 
    sys.exit("Invalid input for the threshold" ) 
 
kmer_counts = collections.Counter() 
for start in tqdm(range(len(dna) - kmer_length + 1)): 
    kmer = dna[start:start+kmer_length] 
    kmer_counts.update([kmer]) 
 
total_count = sum(kmer_counts.values())
 
for kmer, count in kmer_counts.items(): 
    fraction = count / total_count 
    if fraction > threshold: 
        print(kmer, count, fraction)