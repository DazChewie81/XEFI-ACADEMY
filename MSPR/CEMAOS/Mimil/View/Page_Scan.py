import tkinter as tk
from tkinter import ttk
from Controller.Scan import *


def Scan_page(self):
    # Bouton qui lance le scan du reseau
    self.BScan = ttk.Button(self.FScan, text="Lancer le test", command=lambda:{Scaneur(self)})
    self.BScan.pack(anchor=tk.W, padx=[15,15], pady=[15,15])

def Scaneur(self):
    self.fScan = tk.Frame(self.FScan, bg=self.page_selectionnee)
    self.fScan.pack(fill ='both')
    col = 0
    ro = 1
    for cle, valeur in scan_network().items():

        # Si on a plus de 5 ou 10 machines dans une colonne, on change de colonne
        Str = f" - {cle} : {valeur}"
        if ro != 6:
            #print("if",ro,col)
            LMachine = ttk.Label(self.fScan, text=Str, background=self.page_selectionnee)
            LMachine.grid(column=col, row=ro, sticky=tk.W, padx=[50,0])
            ro+=1
        else:
            ro=1
            col+=1
            #print("else",ro,col)
            LMachine = ttk.Label(self.fScan, text=Str, background=self.page_selectionnee)
            LMachine.grid(column=col, row=ro, sticky=tk.W, padx=[50,0])
            ro+=1