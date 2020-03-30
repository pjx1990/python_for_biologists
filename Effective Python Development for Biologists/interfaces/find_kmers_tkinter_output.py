import Tkinter

def analyse():  
    output_text.insert(Tkinter.END, dna_entry.get() + "\n")
    output_text.insert(Tkinter.END, kmer_length_entry.get() + "\n")
    output_text.insert(Tkinter.END, threshold_entry.get() + "\n")

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

analyse_button = Tkinter.Button(window, text="Analyse", width=10, command=analyse) 
analyse_button.pack() 

output_text = Tkinter.Text(window, height=10, width=25)
output_text.pack()

window.mainloop()