def filter_reads(reads, threshold): 
    for read in list(reads): 
        if read.count('N') >= threshold: 
            reads.remove(read)

reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']
filter_reads(reads, 1)
assert reads == ['ATCGTAC']

reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']
filter_reads(reads, 2)
assert reads == ['ATCGTAC', 'ACTGNTTACGT']

reads = ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']
filter_reads(reads, 3)
assert reads == ['ATCGTAC', 'ACTGNTTACGT', 'ACTGNNTACTG']