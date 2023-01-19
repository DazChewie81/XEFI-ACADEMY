import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
from View.Frame_Header import header
from View.Page_Dashboard import Dashboard
from View.Page_TestsDebit import TestsDebit
from View.Page_Scan import Scan_page


class FenetrePrincipale(tk.Tk):

    def __init__(self):
        super().__init__()
        
        # Fonctions de la fenêtre et du style
        self.window()
        self.style()
        
        # Création du NoteBook
        self.notebook = ttk.Notebook(self)
        self.FDashboard = tk.Frame(self.notebook, bg=self.page_background)
        self.FDebit = tk.Frame(self.notebook, bg=self.page_background)
        self.FScan = tk.Frame(self.notebook, bg=self.page_background)
        
        # Fonctions placements
        self.place()
        
        # Fonctions affichage header
        header(self, self.FDashboard)
        header(self, self.FDebit)
        header(self, self.FScan)
        
        # Fonction affichage du Dashboard
        
        # Importe l'image rond vert pour etat connection
        self.img_vert = Image.open("img/Rond_vert.png")
        self.resized_image_vert = self.img_vert.resize((10,10))
        self.new_image_vert = ImageTk.PhotoImage(self.resized_image_vert)

        # Importe l'image rond rouge pour etat connection
        self.img_rouge = Image.open("img/Rond_rouge.png")
        self.resized_image_rouge = self.img_rouge.resize((10,10))
        self.new_image_rouge = ImageTk.PhotoImage(self.resized_image_rouge)

        # Importation le rond des tests de ping
        self.imgValeurs = Image.open("img/rond_tr.png")
        self.resized_imgValeurs= self.imgValeurs.resize((250,250))
        self.new_imageValeurs= ImageTk.PhotoImage(self.resized_imgValeurs)

        Dashboard(self)
        TestsDebit(self)
        Scan_page(self)

        # Caractéristiques de la fenêtre
    def window(self):
        self.title("SemaOS")
        self.iconphoto(False, tk.PhotoImage('img/logo.png'))
        self.geometry("2000x2000")
        #self.attributes("-alpha", 1)
        #self.wm_attributes("-transparentcolor", 'grey')


    # Style des Frames
    def style(self):
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
    def place(self):
        self.notebook.add(self.FDashboard, text='Dashboard')
        self.notebook.add(self.FDebit, text='Test débit')
        self.notebook.add(self.FScan, text='Scan réseau')
        self.notebook.pack(anchor='nw', expand=True, fill ="both")