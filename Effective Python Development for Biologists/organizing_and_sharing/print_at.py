import at_calculator

# open the input file, read the contents and remove the newline
dna = open('dna.txt').read().rstrip("\n")

# print the output
print("AT content is " + str(at_calculator.calculate_at(dna)))


