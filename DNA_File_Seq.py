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
                
    #Translate DNA to RNA
    def DNA_to_RNA(self, something):
        #some code, handle Thymine/Uracil
        return RNA
    
    def Codon_Table(self):
        AminoAcids = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
        }
        return AminoAcids
