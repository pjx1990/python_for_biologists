def find_common_kmers(dna, k, threshold):
    if k < 1:
        return []
    kmer2count = {}
    for start in range(len(dna) + 1 - k):
        kmer = dna[start:start+k]
        old_count = kmer2count.get(kmer, 0)
        kmer2count[kmer] = old_count + 1
    
    result = []
    for kmer, count in kmer2count.items():
        if count >= threshold:
            result.append(kmer)
    return result

assert set(find_common_kmers('atgaatgcaaatga', 3, 3)) == set(['atg'])
assert set(find_common_kmers('atgaatgc', 3, 2)) == set(['atg'])
assert set(find_common_kmers('aattggcc', 1, 2)) == set(['a', 't', 'g', 'c'])
assert set(find_common_kmers('tagctagtcg', 10, 1)) == set(['tagctagtcg'] )
assert set(find_common_kmers('ctagctgctcgtgactgtcagtgtacg', 2, 4)) == set(['ct', 'tg', 'gt'])
assert set(find_common_kmers('cccaaaacccaaaacccaaaacccaaaa', 4, 4)) == set(['ccca', 'ccaa', 'caaa', 'aaaa'])
assert set(find_common_kmers('tagctagtcg', 0, 2)) == set([])
assert set(find_common_kmers('tagctagtcg', -3, 2)) == set([])