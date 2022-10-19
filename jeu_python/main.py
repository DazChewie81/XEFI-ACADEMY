import tkinter as tk
from tkinter import ttk
import subprocess
from Jeux import Jeux
#from Jeux.Jeux import Jeux

class start(tk.Tk): 
    def __init__(self):
        
        super().__init__()
        self.button = ttk.Button(self, text='Nouvelle partie')
        self.button.pack()
        self.__bind()
    
    def __bind(self):
        self.button.bind("<Button-1>", self.newgame())
    

start=start()
start.mainloop()
