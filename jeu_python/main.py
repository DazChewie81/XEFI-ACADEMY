import tkinter as tk
from tkinter import ttk
import subprocess
import Arme
import Classe
import Personnage
import Monstre
import Guerrier
import Mage
import Sauvegarde

class start(tk.Tk): 
    def __init__(self):
        
        super().__init__()
        self.button = ttk.Button(self, text='Nouvelle partie')
        self.button.pack()
        self.__bind()
    
    def __bind(self):
        self.button.bind("<Button-1>", self.newgame)
    
    def newgame(self, event=None):
        simon = Personnage.Personnage("Pendaroue", 30)
        print(simon.pseudo)
        print(orc.pv)
        simon.attaque(baton, orc)
        print(orc.pv)
        
 

    save1 = Sauvegarde.Sauvegarde("save1")

    save1.save()
    #instantiation amre
    baton = Arme.Arme("baton phénix", 5)
    #instantiation de mage
    mage = Mage.Mage(baton)

     #arc = Arme.Arme("baton phénix", 2)
     #instantiation amre
     #epee = Arme.Arme("epee du débutant", 3)
     #instantiation de guerrier
     #guerrier = Guerrier.Guerrier(epee)

     #archer = Archer.Archer(arc)
     orc = Monstre.Monstre("Orc", 15 ,3)
     print(orc.nom)

     simon = Personnage.Personnage("Pendaroue", 30, mage)
     print(simon.pseudo)
     print(orc.pv)
     simon.classe.attaque(baton, orc)
     print(orc.pv)
     orc.attaque(simon)
     print(simon.pv)
start=start()
start.mainloop()
