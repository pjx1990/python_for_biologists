from __future__ import division
import pdb 

dna = raw_input("Enter a DNA sequence:\n")
pdb.set_trace() 
at = dna.count('A') + dna.count('T') / len(dna)
print("AT content is " + str(at))