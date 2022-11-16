
import tkinter as tk
from tkinter import ttk
from controller.Jeu import *

class FenetrePrincipale(tk.Tk):
    def __init__(self):
        super().__init__()

        self.jeu = Jeu()
        self.style = ttk.Style()
        self.geometry("200x200")
        self.fInformations = ttk.Frame()
        self.fValidation = ttk.Frame()
        self.fInformations.pack(fill=tk.X)
        self.fValidation.pack(fill=tk.X)
        self.get_menu_frame()
        self.mainloop()
        
        
    def get_menu_frame(self):
        self.style = ttk.Style()
        self.style.configure('stylequitter.TButton', background='red')
        self.lMenu = tk.Label(self.fInformations, text='Menu', font=("Helvetica", 16))
        self.bCommencer = ttk.Button(self.fValidation, text='Commencer', command = self.__Chargement, style = 'stylelabel.TButton')
        self.lPseudo = ttk.Label(self.fValidation, text='',font=("Helvetica", 2))

        #BOUTTONS DE CLASSES
        self.bPaladin = ttk.Button(self.fValidation, text='Paladin', command = lambda:[self.Clean(), self.jeu.choixclasse(1)], style = 'stylelabel.TButton')
        self.bMage = ttk.Button(self.fValidation, text='Mage', command = lambda:[self.Clean(), self.jeu.choixclasse(2)], style = 'stylecharger.TButton')
        self.bAssassin = ttk.Button(self.fValidation, text='Assassin', command = lambda:[self.Clean(), self.jeu.choixclasse(3)], style = 'stylecharger.TButton')
        self.bArcher = ttk.Button(self.fValidation, text='Archer', command = lambda:[self.Clean(), self.jeu.choixclasse(4)], style = 'stylecharger.TButton')

        #Boutton pour quitter
        self.bQuitter = ttk.Button(self.fValidation, text='Quitter', command = self.quit, style = 'stylequitter.TButton')

        #Champ de pseudo plus validation
        self.ePseudo = ttk.Entry(self.fValidation)
        self.bValider = ttk.Button(self.fValidation, text='Valider', command = self.setPseudo)
        self.Menu()


    #Affichage fenetre au lancement
    def Menu(self):
        self.lMenu.pack()
        self.lPseudo.pack()
        self.bCommencer.pack()


    #Affiche le champ de pseudo
    def Pseudo(self):
        self.ePseudo.pack()
        self.bValider.pack()
        self.bQuitter.pack()

    #Affiche les choix de classes
    def BouttonClasse(self):     
        self.bPaladin.pack()
        self.bAssassin.pack()
        self.bMage.pack()
        self.bArcher.pack()
        
    #Lance la partie
    def __Chargement(self, event=None):
        self.Pseudo()
        self.bCommencer.destroy()
        self.jeu.lancement()

    #recupere le pseudo de l'entry
    def setPseudo(self):
        self.lPseudo.configure(text='Pseudo : '+self.ePseudo.get(), font=('Vivaldi',12))
        self.jeu.pseudo = self.ePseudo.get()
        self.ePseudo.destroy()
        self.bValider.destroy()
        self.bQuitter.destroy()
        self.BouttonClasse()

    #enleve les bouttons apres le choix de la classe
    def Clean(self ,event=None):
        self.bArcher.destroy()
        self.bPaladin.destroy()
        self.bMage.destroy()
        self.bAssassin.destroy()
        


        
    






#app = FenetrePrincipale()
#app.mainloop()
