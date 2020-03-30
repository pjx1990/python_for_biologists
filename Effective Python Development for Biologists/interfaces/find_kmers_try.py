from __future__ import division
import collections
from tqdm import tqdm
import sys 

if len(sys.argv) != 4: 
    sys.exit("Usage: python find_kmers_usage.py input_filename kmer_length threshold")

# if we get to here, then the input is valid
input_filename = sys.argv[1] 
kmer_length = int(sys.argv[2]) 
threshold = float(sys.argv[3]) 

try:
    dna = open(input_filename).read().rstrip("\n")
except IOError as ex:
    sys.exit("Sorry, couldn't open the file: " + ex.strerror) 

print("counting kmers, this may take a while...")

dna = open(input_filename).read().rstrip("\n")
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