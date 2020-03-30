from nose.tools import assert_equal 
 
def find_common_kmers(dna, k, threshold): 
    result = [] 
    for start in range(len(dna) + 1 - k): 
        kmer = dna[start:start+k] 
        if dna.count(kmer) >= threshold and kmer not in result: 
            result.append(kmer) 
    return result 
 
def test_3mers(): 
    assert_equal(find_common_kmers('atgaatgcaaatga', 3, 3), ['atg']) 
 
def test_low_threshold(): 
    assert_equal(find_common_kmers('atgaatgc', 3, 2) , ['atg']) 
 
def test_single_bases(): 
    assert_equal(find_common_kmers('aattggcc', 1, 2) , 
                  ['a', 't', 'g', 'c']) 
 
def test_whole_sequence(): 
    assert_equal(find_common_kmers('tagctagtcg', 10, 1) , ['tagctagtcg']) 
 
def test_long_sequence(): 
    assert_equal(find_common_kmers('ctagctgctcgtgactgtcagtgtacg', 2, 4),
                  ['ct', 'tg', 'gt']) 
 
def test_long_sequence_4mers(): 
    assert_equal(find_common_kmers('cccaaaacccaaaacccaaaacccaaaa',4, 4) ,
                  ['ccca', 'ccaa', 'caaa', 'aaaa']) 
 
def test_zero_length_kmer(): 
    assert_equal(find_common_kmers('tagctagtcg', 0, 2) , []) 
 
def test_negative_length_kmer(): 
    assert_equal(find_common_kmers('tagctagtcg', -3, 2) , []) 