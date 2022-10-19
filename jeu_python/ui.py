import tkinter as tk
from tkinter import ttk
from jeux import *


class Ui(tk.Tk):
    def __init__(self):
        
        super().__init__()
        self.jeux=Jeux()
        self.button = ttk.Button(self, text='Nouvelle partie')
        self.button.pack()
        self.__bind()
        
        
    def __bind(self):
        self.button.bind("<Button-1>", self.newgame)
    
    def newgame(self, event=None):
        orc = Monstre.Monstre("Orc", 15 ,3)
        baton = Arme.Arme("baton phénix", 5)
        mage = Mage.Mage(baton)
        simon = Personnage.Personnage("Pendaroue", 30, mage)
        print(simon.pseudo)
        print(f"Il reste {orc.pv} à l'orc")
        simon.classe.attaque(baton, orc)
        print(f"Il reste {orc.pv} à l'orc")
        