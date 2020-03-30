dna = "ATGCGTGATGC" 
print("original:           " + dna) 

dna = dna.replace("A", "T") 
print("first replacement:  " + dna) 

dna = dna.replace("C", "G") 
print("second replacement: " + dna) 

dna = dna.replace("G", "C") 
print("third replacement:  " + dna) 

dna = dna.replace("T", "A") 
print("fourth replacement: " + dna)   