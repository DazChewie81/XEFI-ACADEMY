import tkinter as tk
from tkinter import ttk
from Jeux.Jeux import Jeux



class Ui(tk.Tk):
    def __init__(self):
        
        super().__init__()
        self.jeux=Jeux()
        self.button = ttk.Button(self, text='Nouvelle partie')
        self.button.pack()
        self.__bind()
        
        
    def __bind(self):
        self.button.bind("<Button-1>", Jeux.newgame)
        
app = Ui()
app.mainloop()