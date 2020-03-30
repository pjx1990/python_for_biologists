def find_common_kmers(dna, k, threshold):
    if k < 1:
        return []
    result = []
    for start in range(len(dna) + 1 - k):
        kmer = dna[start:start+k]
        if dna.count(kmer) >= threshold and kmer not in result:
            result.append(kmer)
    return result

assert find_common_kmers('atgaatgcaaatga', 3, 3) == ['atg']
assert find_common_kmers('atgaatgc', 3, 2) == ['atg']
assert find_common_kmers('aattggcc', 1, 2) == ['a', 't', 'g', 'c']
assert find_common_kmers('tagctagtcg', 10, 1) == ['tagctagtcg'] 
assert find_common_kmers('ctagctgctcgtgactgtcagtgtacg', 2, 4) == ['ct', 'tg', 'gt']
assert find_common_kmers('cccaaaacccaaaacccaaaacccaaaa', 4, 4) == ['ccca', 'ccaa', 'caaa', 'aaaa']
assert find_common_kmers('tagctagtcg', 0, 2) == []
assert find_common_kmers('tagctagtcg', -3, 2) == []