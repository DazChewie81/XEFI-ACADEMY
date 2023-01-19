import tkinter as tk
from tkinter import ttk
from Controller.InfoBox import *

def header(self, page):
    #self.Lname = f"L + {page}"
    Fheader = tk.Frame(page, bg=self.page_background)
    Fheader.pack(fill ='x')
    
    Fheader.columnconfigure(0, weight=1)
    Fheader.columnconfigure(1, weight=1)
    
    Lname = ttk.Label(Fheader, text=hostname)
    Lip = ttk.Label(Fheader, text=ip_address)


    Lname.grid(column=0, row=0, sticky=tk.W)
    Lip.grid(column=1, row=0, sticky=tk.E)