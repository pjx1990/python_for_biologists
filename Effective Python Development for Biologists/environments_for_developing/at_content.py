from __future__ import division

sequences = [
'ATCGTAGTCGA',
'ATCGTTAGCT',
'ATCGTAGCGTGTAC'
]

for dna in sequences:
    total_at = 0
    for base in dna:
        if base == 'A' or base == 'T':
            total_at = total_at + 1

total_length = sum(map(len, sequences))

print("average AT content: " + str(total_at/total_length))