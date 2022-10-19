
import tkinter as tk
from tkinter import ttk
from Jeu import JeuPrincipal 

class FenetrePrincipale(tk.Tk, JeuPrincipal):
    def __init__(self):
        super().__init__()

        self.style = ttk.Style()
        self.style.configure('lfBlocInfosPersos.TLabelframe')
        self.style.configure('lfBlocMotsDePasse.TLabelframe')

        self.fInformations = ttk.Frame()
        self.fValidation = ttk.Frame()

        self.fInformations.pack(fill=tk.X)
        self.fValidation.pack(fill=tk.X)
        self.get_menu_frame()

    def get_menu_frame(self):
        self.style = ttk.Style()
        self.style.configure('stylelabel', background='yellow')
        self.style.configure('stylebouvelle.TButton', color='lightgreen')
        self.style.configure('stylecharger.TButton', background='#7AC5CD')
        self.style.configure('stylequitter.TButton', background='#7a6fcf')
        
        
        self.lMenu = tk.Label(self.fInformations, text='Menu', font=("Helvetica", 16))
        self.bNew = ttk.Button(self.fValidation, text='Nouvelle partie', style = 'stylelabel.TButton')
        self.bCharger = ttk.Button(self.fValidation, text='Charger une partie', style = 'stylecharger.TButton')
        self.bQuitter = ttk.Button(self.fValidation, text='Quitter', command = self.quit, style = 'stylequitter.TButton')

        self.__place()
        self.__bind()

        
    def __place(self):
        self.lMenu.pack()
        self.bNew.pack()
        self.bCharger.pack()
        self.bQuitter.pack()
        
    def __bind(self):
        self.bNew.bind("<Button-1>", self.__Lien)
        
    def __Lien(self, event=None):
        super().jeu()
        
        
    






app = FenetrePrincipale()
app.mainloop()
