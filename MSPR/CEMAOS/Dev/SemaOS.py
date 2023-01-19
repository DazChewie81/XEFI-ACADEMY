"""
A faire !!

Aligner, centrer le texte des pages notebook

__header -> Variable pour Nom + Ip
"""
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class FenetrePrincipale(tk.Tk):

    def __init__(self):
        super().__init__()
        
        # Fonctions de la fenêtre et du style
        self.__window()
        self.__style()
        
        # Création du NoteBook
        self.notebook = ttk.Notebook(self)
        self.FDashboard = tk.Frame(self.notebook, bg=self.page_background)
        self.FDebit = tk.Frame(self.notebook, bg=self.page_background)
        self.FScan = tk.Frame(self.notebook, bg=self.page_background)
        
        # Fonctions placements
        self.__place()
        
        # Fonctions affichage header
        self.__header(self.FDashboard)
        self.__header(self.FDebit)
        self.__header(self.FScan)
        
        # Fonction affichage du Dashboard
        # Importe l'image rond pour connection

        self.img = Image.open("img/Rond_vert.png")
        self.resized_image = self.img.resize((10,10))
        self.new_image = ImageTk.PhotoImage(self.resized_image)

        # Importation le rond des tests de ping
        self.imgValeurs = Image.open("img/rond_tr.png")
        self.resized_imgValeurs= self.imgValeurs.resize((250,250))
        self.new_imageValeurs= ImageTk.PhotoImage(self.resized_imgValeurs)

        self.__Dashboard()

        self.__TestsDebit()
        
        self.__bind()



    # Caractéristiques de la fenêtre
    def __window(self):
        self.title("SemaOS")
        self.iconphoto(False, tk.PhotoImage('img/logo.png'))
        self.geometry("2000x2000")
        #self.attributes("-alpha", 1)
        #self.wm_attributes("-transparentcolor", 'grey')


    # Style des Frames
    def __style(self):
        self.style = ttk.Style()
        
        # Création d'un thème
        # Définition des couleurs
        self.notebook_background = '#8C0C0C'
        self.page_background = '#D00202'
        # Page sélectionnée + Dégradé de couleur dans la page
        self.page_selectionnee = '#AE1313'
        self.page_non_selectionnee = '#FD0101'
        
        self.defa = self.style.theme_use('default')
        
        # ! Justifier les textes
        self.style.theme_create( "themeNote", settings={
            # Paramètres du notebook
            "TNotebook": {"configure": {"background": self.notebook_background, "tabposition":'wn' } },
            
            # Paramètres des fenêtres
            "TNotebook.Tab": {
                "configure": {"padding": [15, 15], "width":11, "background": self.page_non_selectionnee, "foreground":'#FFFFFF', "font" : ('Source Sans Pro Black', '15', 'bold'), "align": "RIGHT"},
                "map":       {"background": [("selected", self.page_selectionnee)] }
                },
            
            # Paramètre Label
            "TLabel":{
                "configure":{"font" : ('Source Sans Pro Black', '14', 'bold'), "padding": [20,15], "background": self.page_background, "foreground":'#FFFFFF'
                    }
                },

                # Paramètres butoon
            "TButton":{
                "configure":{"foreground":'#FFFFFF', "background": self.page_background, "font" : ('Source Sans Pro Black', '25', 'bold'), "padding" : [15,15]
            }
            }
            } )

        self.style.theme_use('themeNote')


    # Positionnement des Frames
    def __place(self):
        self.notebook.add(self.FDashboard, text='Dashboard')
        self.notebook.add(self.FDebit, text='Test débit')
        self.notebook.add(self.FScan, text='Scan réseau')
        self.notebook.pack(anchor='nw', expand=True, fill ="both")

    # J'ai rajouter des arguments ca marche plus
    def __StatCo(self, frame, couleurbg, vDl, vUl, VPing):
            # Frame des tests de connections
            
            #fTestco = tk.Frame(frame, bg=couleurbg)
            #fTestco.pack(fill ='both')
            
            frame.columnconfigure(0, weight=1)
            frame.columnconfigure(1, weight=1)
            frame.columnconfigure(2, weight=1)
            
            LMesure = ttk.Label(frame, text='Dernière mesure du débit il y a X minutes', background = couleurbg)
            LMesure.grid(column=0, row=0, sticky=tk.W, columnspan = 2)
            
            LDownload = ttk.Label(frame, text='Download', background = couleurbg, font=('Source Sans Pro Black', '22', 'bold'))
            LDownload.grid(column=0, row=1)
            
            LUpload = ttk.Label(frame, text='Upload', background = couleurbg, font=('Source Sans Pro Black', '22', 'bold'))
            LUpload.grid(column=1, row=1)
            
            LPing = ttk.Label(frame, text='Ping', background = couleurbg, font=('Source Sans Pro Black', '22', 'bold'))
            LPing.grid(column=2, row=1)

            # Positionnement des stats (cercles + valeurs)
            LRondValeursDl = ttk.Label(frame, image = self.new_imageValeurs, background = couleurbg)
            LRondValeursDl.grid(column=0, row=2)

            # pady=[x,y] -> x décalage avec le haut (descend le label) et y avec le bas
            ValeursDl = ttk.Label(frame, text=vDl, background = couleurbg, font=('Source Sans Pro Black', '28', 'bold'))
            ValeursDl.grid(column=0, row=2, pady=[0,50])

            LValeursDl = ttk.Label(frame, text="MBIT/S", background = couleurbg, font=('Source Sans Pro Black', '15', 'bold'))
            LValeursDl.grid(column=0, row=2, pady=[50,0])



            LRondValeursUl = ttk.Label(frame, image = self.new_imageValeurs, background = couleurbg)
            LRondValeursUl.grid(column=1, row=2)

            ValeursUl = ttk.Label(frame, text=vUl, background=couleurbg, font=('Source Sans Pro Black', '28', 'bold'))
            ValeursUl.grid(column=1, row=2, pady=[0,50])

            LValeursUl = ttk.Label(frame, text="MBIT/S", background = couleurbg, font=('Source Sans Pro Black', '15', 'bold'))
            LValeursUl.grid(column=1, row=2, pady=[50,0])



            LRondValeursPing = ttk.Label(frame, image = self.new_imageValeurs, background = couleurbg)
            LRondValeursPing.grid(column=2, row=2)

            ValeursPing = ttk.Label(frame, text=VPing, background = couleurbg, font=('Source Sans Pro Black', '28', 'bold'))
            ValeursPing.grid(column=2, row=2, pady=[0,50])

            LValeursPing = ttk.Label(frame, text="MS", background = couleurbg, font=('Source Sans Pro Black', '15', 'bold'))
            LValeursPing.grid(column=2, row=2, pady=[50,0])

    def FctTestCO(self):
        self.__StatCo(self.FTestDebit, self.page_selectionnee, '1000', '250', '30')


    def __header(self, page):
        #self.Lname = f"L + {page}"
        Fheader = tk.Frame(page, bg=self.page_background)
        Fheader.pack(fill ='x')
        
        Fheader.columnconfigure(0, weight=1)
        Fheader.columnconfigure(1, weight=1)
        
        Lname = ttk.Label(Fheader, text='Nom de la SemaBox')
        
        Lip = ttk.Label(Fheader, text='Adresse IP')
    

        Lname.grid(column=0, row=0, sticky=tk.W)
        Lip.grid(column=1, row=0, sticky=tk.E)

    # Elments du Dashboard
    def __Dashboard(self):
        #self.FDashboard
        # Frame de l'état de la connexion
        fDashco = tk.Frame(self.FDashboard, bg=self.page_selectionnee)
        fDashco.pack(fill ='both')
        
        """fDashco.columnconfigure(0, weight=1)
        fDashco.columnconfigure(1, weight=2)"""
        
        # Columnspan permet de ne pas étendre une colonne, ce qui évite de décaler les colonnes des autres lignes
        LEtat = ttk.Label(fDashco, text='Etat de la connexion', background = self.page_selectionnee )
        LEtat.grid(column=0, row=0, sticky=tk.W, columnspan = 2)
        
        # Pour le rond vert, faire une condition si connecter -> C:/image_vert.png sinon c:/image_rouge.png
        # Variable Connecté ou non, variable WIFI ou Ethernet ...


        LImageCO = ttk.Label(fDashco, image = self.new_image, background = self.page_selectionnee)
        LImageCO.grid(column=0, row=1, sticky=tk.W)
        
        
        LConnexion = ttk.Label(fDashco, text='Connecté -> WI-FI / Ethernet / Ip publique /  Nom domaine', background = self.page_selectionnee )
        LConnexion.grid(column=1, row=1, sticky=tk.W)

        # Frame statistique co

        self.fDashCO = tk.Frame(self.FDashboard, bg=self.page_background)
        self.fDashCO.pack(fill ='both')
        self.__StatCo(self.fDashCO, self.page_background, '---', '---', '---')

        # Frame des listes équipements
        fDashList = tk.Frame(self.FDashboard, bg = self.page_selectionnee)
        fDashList.pack(fill ='both')

        fDashList.columnconfigure(0, weight=1)
        fDashList.columnconfigure(1, weight=1)
        fDashList.columnconfigure(2, weight=1)

        LList = ttk.Label(fDashList, text='Liste des machines sur le réseau', background = self.page_selectionnee)
        LList.grid(column=0, row=0, sticky=tk.W, columnspan = 2)

        liste_machine={"Machineapp001" :"192.168.10.1", "Machineapp002" :"192.168.10.2", "Machineapp003" :"192.168.10.3", "Machineapp004" :"192.168.10.4", "Machineapp005" :"192.168.10.5", "Machineapp006" :"192.168.10.6", "Machineapp007" :"192.168.10.7", "Machineapp008" :"192.168.10.8", "Machineapp009" :"192.168.10.9", "Machineapp0010" :"192.168.10.10", "Machineapp0011" :"192.168.10.11", "Machineapp0012" :"192.168.10.12"}
        col = 0
        ro = 1
        for cle, valeur in liste_machine.items():

            # Si on a plus de 5 ou 10 machines dans une colonne, on change de colonne
            Str = f" - {cle} : {valeur}"
            if ro != 6:
                #print("if",ro,col)
                LMachine = ttk.Label(fDashList, text=Str, background = self.page_selectionnee )
                LMachine.grid(column=col, row=ro, sticky=tk.W, padx=[50,0])
                ro+=1
            else:
                ro=1
                col+=1
                #print("else",ro,col)
                LMachine = ttk.Label(fDashList, text=Str, background = self.page_selectionnee )
                LMachine.grid(column=col, row=ro, sticky=tk.W, padx=[50,0])
                ro+=1




    def __TestsDebit(self):
        self.FTestDebit = tk.Frame(self.FDebit, bg=self.page_selectionnee)
        self.FTestDebit.pack(fill ='both')
        self.__StatCo(self.FTestDebit, self.page_selectionnee, '---', '---', '---')

        # Bouton qui lance le test de débit
        self.BTest = ttk.Button(self.FDebit, text="Lancer le test", command=self.FctTestCO)
        self.BTest.pack(anchor=tk.W, padx=[15,15], pady=[15,15])

    # ? Liens
    def __bind(self):
        pass
        #command=lambda: get_game_frame()


app = FenetrePrincipale()
app.mainloop()