from Bio.Seq import Seq
import tkinter as tk
from tkinter import filedialog, messagebox

class DNAStuff(object):
    
    #Get file
    def DNAfile(self):
        root = tk.Tk()
        messagebox.showinfo("DNA", "Click OK to Choose your File.")
        root.withdraw()
        file_path = filedialog.askopenfilename()
        return file_path

    #Isolate codon triplets
    def triplet_codon(self, line):
        while line:
            data = line.read(3)
            
    #Shift reading frame 
    def frame_shift_mutation(self):
        #start codon +1 char ahead
        
    #Start Codon detection
    def start_codon(self, frame):
        start_code = ['AUG']
        if frame in start_code:
           return True
    
    #Stop Codon Detection
    def stop_codon(self, frame):
        stop_codes = ['UAA', 'UAG', 'UGA']
        if frame in stop_codes
            return True
    
    def DNA_strand(self, file):
        with open(file) as data:
            for line in data:
                codon = self.triplet_codon(line)
                seq = Bio.Seq(line)
                print(seq)
    
