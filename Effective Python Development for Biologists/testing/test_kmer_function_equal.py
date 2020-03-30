from nose.tools import assert_equal 

def find_common_kmers(dna, k, threshold): 
    result = [] 
    for start in range(len(dna)): 
        kmer = dna[start:start+k] 
        if dna.count(kmer) >= threshold: 
            result.append(kmer) 
    return result 
 
 
def test_3mers(): 
    assert_equal(find_common_kmers('atgaatgcaaatga', 3, 3), ['atg']) 