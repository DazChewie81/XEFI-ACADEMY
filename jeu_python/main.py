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
 


#instantiation amre
baton = Arme.Arme("baton phénix", 5)
#instantiation de mage
mage = Mage.Mage(baton)

#instantiation amre
epee = Arme.Arme("epee du débutant", 3)
#instantiation de guerrier
guerrier = Guerrier.Guerrier(epee)

guerrierMage = Classe.Classe([mage, guerrier])

#création objet classe
testClasse = Classe.Classe(mage) 
orc = Monstre.Monstre("Orc", 15)
print(orc.nom)

#simon = Personnage.Personnage("Pendaroue", 30)
#print(simon.pseudo)
#print(orc.pv)
#simon.attaque(baton, orc)
#print(orc.pv)

def __init__(self):
        
    super().__init__()
    self.button = ttk.Button(self, text='Nouvelle partie')
    self.__bind()
    
def __bind(self):
    self.button.bind("<Button-1>", self.newgame)
    
def newgame(self, event=None):
    simon = Personnage.Personnage("Pendaroue", 30)
    print(simon.pseudo)
    print(orc.pv)
    simon.attaque(baton, orc)
    print(orc.pv)
        
