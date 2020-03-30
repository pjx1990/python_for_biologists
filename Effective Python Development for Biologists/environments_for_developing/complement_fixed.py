dna = "ATGCGTGATGC" 
print("original:           " + dna) 

dna = dna.replace("A", "t") 
print("first replacement:  " + dna) 

dna = dna.replace("C", "g") 
print("second replacement: " + dna) 

dna = dna.replace("G", "c") 
print("third replacement:  " + dna) 

dna = dna.replace("T", "a") 
print("fourth replacement: " + dna)   

dna = dna.upper()
print("finally:            " + dna)