from __future__ import division
import Tkinter
import collections

def analyse(): 
    output_text.delete("1.0", Tkinter.END) 
    # get the parameters 
    dna = dna_entry.get() 
    kmer_length = int(kmer_length_entry.get()) 
    threshold = float(threshold_entry.get()) 
 
    all_kmers = [] 
 
    for start in range(len(dna) - kmer_length + 1): 
        kmer = dna[start:start+kmer_length] 
        all_kmers.append(kmer) 
 
    kmer_counts = collections.Counter(all_kmers) 
    total_count = len(all_kmers) 
 
    for kmer, count in kmer_counts.items(): 
        proportion = count / total_count 
        if proportion > threshold: 
            line = kmer + "," + str(count) + "," + str(proportion) + "\n" 
            output_text.insert(Tkinter.END,  line)

window = Tkinter.Tk()

dna_label = Tkinter.Label(window, text="Enter DNA sequence:")
dna_label.pack()
dna_entry = Tkinter.Entry(window)
dna_entry.pack()

kmer_length_label = Tkinter.Label(window, text="Enter kmer length:") 
kmer_length_label.pack() 
kmer_length_entry = Tkinter.Spinbox(window, from_=1, to=20)
kmer_length_entry.pack() 
 
threshold_label = Tkinter.Label(window, text="Enter threshold:") 
threshold_label.pack() 
threshold_entry = Tkinter.Scale(
    window, 
    from_=0, 
    to=1, 
    orient=Tkinter.HORIZONTAL, 
    resolution=0.01)
threshold_entry.pack()

analyse_button = Tkinter.Button(window, text="Analyse", width=10, command=analyse) 
analyse_button.pack() 

output_text = Tkinter.Text(window, height=10, width=25)
output_text.pack()

window.mainloop()