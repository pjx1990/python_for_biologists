from __future__ import division

dna = raw_input("Enter a DNA sequence:\n")
at = dna.count('A') + dna.count('T') / len(dna)
print("AT content is " + str(at))