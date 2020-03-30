import random

def random_dna(length):
    return "".join([random.choice(['A','T','G','C']) for _ in range(length)])

# long_dna has ten million characters
long_dna = random_dna(10000000)

 # short_dna has one million characters
short_dna = random_dna(1000000)
 
@profile
def count_As(): 
    long_count = long_dna.count('A') 
    short_count = short_dna.count('A') 
 
count_As()