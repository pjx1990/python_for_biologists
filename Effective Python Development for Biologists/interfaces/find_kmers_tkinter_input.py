import Tkinter


window = Tkinter.Tk()

dna_label = Tkinter.Label(window, text="Enter DNA sequence:")
dna_label.pack()
dna_entry = Tkinter.Entry(window)
dna_entry.pack()

kmer_length_label = Tkinter.Label(window, text="Enter kmer length:") 
kmer_length_label.pack() 
kmer_length_entry = Tkinter.Entry(window) 
kmer_length_entry.pack() 
 
threshold_label = Tkinter.Label(window, text="Enter threshold:") 
threshold_label.pack() 
threshold_entry = Tkinter.Entry(window) 
threshold_entry.pack()



window.mainloop()