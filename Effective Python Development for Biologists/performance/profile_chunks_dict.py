import random

# function to generate a random DNA sequence
def random_dna(length):
    return "".join([random.choice(['A','T','G','C']) for _ in range(length)])

# a random long DNA sequence
dna = random_dna(10000)

# a collection of random DNA chunks
motifs = [random_dna(4) for _ in range(100)]

@profile 
def classify_chunks(): 
    chunk_count = {}
    for start in range(len(dna) - 3):
        chunk = dna[start:start + 4]
        current_count = chunk_count.get(chunk, 0)
        new_count = current_count + 1 
        chunk_count[chunk] = new_count

    for chunk, count in chunk_count.items():
        if count > 50: 
            if chunk in motifs:
                print(chunk + " is frequent and interesting")
            else:
                print(chunk + " is frequent but not interesting")
 
classify_chunks()