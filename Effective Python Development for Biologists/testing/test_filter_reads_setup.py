from nose.tools import assert_equal 
from nose.tools import with_setup 
 
def filter_reads(reads, threshold): 
    for read in list(reads): 
        if read.count('N') >= threshold: 
            reads.remove(read) 
 
reads = [] 
def create_reads(): 
    global reads 
    reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG'] 
 
@with_setup(create_reads) 
def test_threshold_one(): 
    filter_reads(reads, 1) 
    assert_equal(reads,  ['ATCGTAC']) 

@with_setup(create_reads)  
def test_threshold_two(): 
    filter_reads(reads, 2) 
    assert_equal(reads,  ['ATCGTAC', 'ACTGNTTACGT']) 

@with_setup(create_reads)  
def test_threshold_three(): 
    filter_reads(reads, 3) 
    assert_equal(reads,['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']) 