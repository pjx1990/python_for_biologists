def find_common_kmers(dna, k, threshold):
    result = [] 
    for start in range(len(dna)): 
        kmer = dna[start:start+k] 
        if dna.count(kmer) >= threshold: 
            result.append(kmer)
    return result

print(find_common_kmers('atgaatgc', 3, 2))