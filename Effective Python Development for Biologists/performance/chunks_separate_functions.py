from __future__ import division
import random
import cProfile 

# function to generate a random DNA sequence
def random_dna(length):
	return "".join([random.choice(['A','T','G','C']) for _ in range(length)])

# a random long DNA sequence
dna = random_dna(10000)

# a collection of random DNA chunks
motifs = [random_dna(4) for _ in range(100)]

def get_frequent_chunks(dna): 
	frequent_chunks = [] 
	for start in range(len(dna) - 3): 
		chunk = dna[start:start + 4] 
		if dna.count(chunk) > 50: 
			frequent_chunks.append(chunk) 
	return frequent_chunks 
 
def print_chunks(chunks): 
	for chunk in chunks: 
		if chunk in motifs: 
			print(chunk + " is frequent and interesting") 
		else: 
			print(chunk + " is frequent but not interesting") 
 
 
def classify_chunks(): 
	frequent_chunks = get_frequent_chunks(dna) 
	print_chunks(frequent_chunks) 
 
cProfile.run("classify_chunks()") 