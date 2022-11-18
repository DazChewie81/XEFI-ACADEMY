import tkinter as tk
from tkinter import ttk

def header(app, page):
    #self.Lname = f"L + {page}"
    Fheader = tk.Frame(page, bg=app.page_background)
    Fheader.pack(fill ='x')
    
    Fheader.columnconfigure(0, weight=1)
    Fheader.columnconfigure(1, weight=1)
    
    Lname = ttk.Label(Fheader, text='Nom de la SemaBox')
    
    Lip = ttk.Label(Fheader, text='Adresse IP')


    Lname.grid(column=0, row=0, sticky=tk.W)
    Lip.grid(column=1, row=0, sticky=tk.E)