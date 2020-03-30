from nose.tools import assert_raises


def find_common_kmers(dna, k, threshold):

    if not isinstance(k, int):
        raise TypeError("k-mer length must be an integer")
    if k < 1:
        raise ValueError("k-mer length must be a positive integer")
    
    result = []
    
    kmer2count = {}
    for start in range(len(dna) + 1 - k):
        kmer = dna[start:start+k]
        old_count = kmer2count.get(kmer, 0)
        kmer2count[kmer] = old_count + 1

    
    for kmer, count in kmer2count.items():
        if count >= threshold:
            result.append(kmer)
   
    return result

def test_non_integer_input():
    assert_raises(TypeError, find_common_kmers, "atcgttactaac", 1.5, 2)

def test_invalid_integer():
    assert_raises(ValueError, find_common_kmers, "atcgttcgctaac", -2, 2)