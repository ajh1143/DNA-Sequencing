from Bio.Seq import Seq
import tkinter as tk
from tkinter import filedialog, messagebox

class DNAStuff(object):

    def DNAfile(self):
        root = tk.Tk()
        messagebox.showinfo("DNA", "Click OK to Choose your File.")
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    def triplet_codon(self, line):
        while line:
            data = line.read(3)
            
    def frame_shift_mutation(self):
        #start codon +1 char ahead
        
    def DNA_strand(self, file):
        with open(file) as data:
            for line in data:
                codon = self.triplet_codon(line)
                seq = Bio.Seq(line)
                print(seq)
