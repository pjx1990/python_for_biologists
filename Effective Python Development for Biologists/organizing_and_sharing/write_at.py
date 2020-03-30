import at_calculator

# ask the user for a DNA sequence and filename
dna = raw_input("Enter a DNA sequence:\n").rstrip("\n")
output_filename = raw_input("Enter a filename:\n").rstrip("\n")

# write the AT content to the output file
with open(output_filename, "w") as out:
    out.write(str(at_calculator.calculate_at(dna)))

