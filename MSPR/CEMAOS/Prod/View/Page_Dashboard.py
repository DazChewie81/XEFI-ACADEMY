import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from View.Frame_Performances_Co import StatCo
from Controller.EtatDeConnexion import *
from Controller.TestCo import FctTestCODashboard
from Controller.Scan import scan_network

# Elments du Dashboard
def Dashboard(self):
    connexion()

    # Frame de l'état de la connexion
    fDashco = tk.Frame(self.FDashboard, bg=self.page_selectionnee)
    fDashco.pack(fill ='both')
    
    # Columnspan permet de ne pas étendre une colonne, ce qui évite de décaler les colonnes des autres lignes
    LEtat = ttk.Label(fDashco, text='Etat de la connexion', background = self.page_selectionnee )
    LEtat.grid(column=0, row=0, sticky=tk.W, columnspan = 2)
    
    # Si on a la connexion on a un rond vert, sinon rouge self.new_image est généré dans GUI.py
    if co == "Connecté":
        LImageCO = ttk.Label(fDashco, image = self.new_image_vert, background = self.page_selectionnee)
        LImageCO.grid(column=0, row=1, sticky=tk.W)
    else:
        LImageCO = ttk.Label(fDashco, image = self.new_image_rouge, background = self.page_selectionnee)
        LImageCO.grid(column=0, row=1, sticky=tk.W)
    
    #Connecté -> WI-FI / Ethernet / Ip publique /  Nom domaine'
    EtatCo=str(co+ " -> " +is_connected()+" / Ip publique: "+IpPublique())
    LConnexion = ttk.Label(fDashco, text=EtatCo, background = self.page_selectionnee )
    LConnexion.grid(column=1, row=1, sticky=tk.W)

    # Frame statistique co
    self.fDashCO = tk.Frame(self.FDashboard, bg=self.page_background)
    self.fDashCO.pack(fill ='both')
    self.testdashboard=StatCo(self, self.fDashCO, self.page_background, '---', '---', '---')
    FctTestCODashboard(self)

    # Frame des listes équipements
    fDashList = tk.Frame(self.FDashboard, bg = self.page_selectionnee)
    fDashList.pack(fill ='both', expand='TRUE')

    fDashList.columnconfigure(0, weight=1)
    fDashList.columnconfigure(1, weight=1)
    fDashList.columnconfigure(2, weight=1)

    LList = ttk.Label(fDashList, text='Liste des machines sur le réseau', background = self.page_selectionnee)
    LList.grid(column=0, row=0, sticky=tk.W, columnspan = 2)

    col = 0
    ro = 1
    for cle, valeur in scan_network().items():

        # Si on a plus de 5 ou 10 machines dans une colonne, on change de colonne
        Str = f" - {cle} : {valeur}"
        if ro != 6:
            LMachine = ttk.Label(fDashList, text=Str, background = self.page_selectionnee )
            LMachine.grid(column=col, row=ro, sticky=tk.W, padx=[50,0])
            ro+=1
        else:
            ro=1
            col+=1
            LMachine = ttk.Label(fDashList, text=Str, background = self.page_selectionnee )
            LMachine.grid(column=col, row=ro, sticky=tk.W, padx=[50,0])
            ro+=1