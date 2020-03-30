from __future__ import division
import collections
import sys
import logging
import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-v", "--verbosity", action="count",
                    help="increase output verbosity")

args = parser.parse_args()

if args.verbosity == None:
    logging.basicConfig(level=logging.ERROR)
elif args.verbosity == 1:
    logging.basicConfig(level=logging.WARN)
elif args.verbosity == 2:
    logging.basicConfig(level=logging.INFO)
elif args.verbosity == 3:
    logging.basicConfig(level=logging.DEBUG)

input_filename = "dna.txt"
kmer_length = 3
count_threshold = 50
output_filename = "test.out"

if kmer_length < 1:
    logging.critical("kmer length must be positive")
    sys.exit()

if count_threshold < 100:
    logging.warning("a low threshold produces a lot of output")

dna = open(input_filename).read().replace("\n", "")

kmer_counts = collections.Counter()

logging.info("counting kmers of length " + str(kmer_length))

for start in range(len(dna) - kmer_length + 1):
    kmer = dna[start:start+kmer_length]
    kmer_counts.update([kmer])

total_count = sum(kmer_counts.values())

with open(output_filename, "w") as output:
    for kmer, count in kmer_counts.items():
        logging.debug("count for " + kmer + " is " + str(count))
        if count > count_threshold:
                output.write(kmer + " " + str(count) + "\n")