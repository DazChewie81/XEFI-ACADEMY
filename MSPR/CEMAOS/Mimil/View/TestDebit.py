import tkinter as tk
from tkinter import ttk
from statdebit import StatCo

def TestsDebit(self):
    self.FTestDebit = tk.Frame(self.FDebit, bg=self.page_selectionnee)
    self.FTestDebit.pack(fill ='both')
    self.StatCo(self.FTestDebit, self.page_selectionnee, '---', '---', '---')

    # Bouton qui lance le test de débit
    self.BTest = ttk.Button(self.FDebit, text="Lancer le test", command=self.FctTestCO)
    self.BTest.pack(anchor=tk.W, padx=[15,15], pady=[15,15])

def FctTestCO(self):
    self.StatCo(self.FTestDebit, self.page_selectionnee, '1000', '250', '30')