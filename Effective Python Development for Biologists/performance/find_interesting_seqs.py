from __future__ import division
import random


# function to generate a random DNA sequence
def random_dna(length):
    return "".join([random.choice(['A','T','G','C']) for _ in range(length)])


# a collection of random DNA sequences
seqs = [random_dna(1000) for _ in range(1000)]

def at_content(dna): 
    return (dna.count('A') + dna.count('T')) / len(dna) 

def same_start(dna1, dna2): 
    return dna1[0:5] == dna2[0:5]


def find_interesting(dnas, cutoff):
    interesting = set()
    for one in dnas:
        at = at_content(one)
        if at > cutoff:
            for two in dnas:
                if one != two and same_start(one, two):
                    interesting.add(one)
 
    return(interesting)

print(find_interesting(seqs, 0.545))