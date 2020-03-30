def find_common_kmers(dna, k, threshold):
    result = []
    for start in range(len(dna)):
        kmer = dna[start:start+k]
        if dna.count(kmer) >= threshold and kmer not in result:
            result.append(kmer)
    return result

assert find_common_kmers('atgaatgc', 3, 2) == ['atg']