"""
Functions for calculating metrics of DNA sequences

A collection of functions for calculating properties of DNA sequences. Note: all functions assume upper case DNA sequence inputs. 
"""

def calculate_at(dna): 
    """Return the AT content of the argument. 
    Only works for uppercase DNA sequences
    """
    length = len(dna)
    a_count = dna.count('A')
    t_count = dna.count('T')
    at_content = (a_count + t_count) / length
    return at_content

# other functions go here...