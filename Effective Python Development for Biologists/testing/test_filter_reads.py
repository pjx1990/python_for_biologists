from nose.tools import assert_equal 
 
def filter_reads(reads, threshold): 
    for read in list(reads): 
        if read.count('N') >= threshold: 
            reads.remove(read) 
 
reads = [] 
def create_reads(): 
    global reads 
    reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG'] 
 
def test_threshold_one(): 
    create_reads() 
    filter_reads(reads, 1) 
    assert_equal(reads,  ['ATCGTAC']) 
 
def test_threshold_two(): 
    create_reads() 
    filter_reads(reads, 2) 
    assert_equal(reads,  ['ATCGTAC', 'ACTGNTTACGT']) 
 
def test_threshold_three(): 
    create_reads() 
    filter_reads(reads, 3) 
    assert_equal(reads,['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']) 