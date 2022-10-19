import tkinter as tk
from tkinter import ttk
import subprocess
from ui import Ui
import Arme
import Classe
import Personnage
import Monstre
import Guerrier
import Mage
import Sauvegarde


class Main(Ui): 
    #def __init__(self):
        
        #super().__init__()
        #self.button = ttk.Button(self, text='Nouvelle partie')
        #self.button.pack()
        #self.__bind()
    
    #def __bind(self):
        #self.button.bind("<Button-1>", self.newgame)
    
    #def newgame(self, event=None):
        #orc = Monstre.Monstre("Orc", 15 ,3)
        #baton = Arme.Arme("baton phénix", 5)
        #mage = Mage.Mage(baton)
        #simon = Personnage.Personnage("Pendaroue", 30, mage)
        #print(simon.pseudo)
        #print(f"Il reste {orc.pv} à l'orc")
        #simon.classe.attaque(baton, orc)
        #print(f"Il reste {orc.pv} à l'orc")
        
 

    save1 = Sauvegarde.Sauvegarde("save1")

    save1.save()


ui=ui()
ui.mainloop()
main=main()
start.mainloop()
