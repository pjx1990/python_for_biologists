from __future__ import division 
 
def at_count(dna): 
    return (dna.count('a') + dna.count('t')) / len(dna) 
 
def at_iter(dna): 
    a_count = 0 
    t_count = 0 
    for base in dna: 
        if base == 'a': 
            a_count = a_count + 1 
        elif base == 't': 
            t_count = t_count + 1 
    return (a_count + t_count) / len(dna) 
 
 
test_dna = 'atcgatcgatcatgatcggatcgtagctagcatctagtc' 
assert(at_count(test_dna) == at_iter(test_dna)) 