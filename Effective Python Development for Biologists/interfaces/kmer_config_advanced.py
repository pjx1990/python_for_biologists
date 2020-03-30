# path to the input file name, which must contain a DNA sequence 
input_filename = "dna.txt" 
 
# a list of kmer lengths to analyse, separated with commas 
# each number must be a positive integer 
# don't remove the square brackets! 
kmer_lengths = [4,5,8] 
 
# minimum proportion of the sequence that a kmer must represent to be displayed 
# must be a floating point number between 0 and 1 
threshold = 0.01 
 
# change this to False if you don't want to see the progress bar 
show_progressbar = True