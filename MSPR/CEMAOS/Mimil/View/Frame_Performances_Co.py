import tkinter as tk
from tkinter import ttk

# On initie une classe pour recupérer facilement les labels afin de les modifier
class StatCo:
    def __init__(self, app, frame, couleurbg, vDl, vUl, VPing):
        # Frame des tests de connections
        
        #fTestco = tk.Frame(frame, bg=couleurbg)
        #fTestco.pack(fill ='both')
        
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        
        self.LMesure = ttk.Label(frame, text='Performances connexion internet', background = couleurbg)
        self.LMesure.grid(column=0, row=0, sticky=tk.W, columnspan = 2)
        
        self.LDownload = ttk.Label(frame, text='Download', background=couleurbg, font=('Source Sans Pro Black', '22', 'bold'))
        self.LDownload.grid(column=0, row=1)
        
        self.LUpload = ttk.Label(frame, text='Upload', background=couleurbg, font=('Source Sans Pro Black', '22', 'bold'))
        self.LUpload.grid(column=1, row=1)
        
        self.LPing = ttk.Label(frame, text='Ping', background=couleurbg, font=('Source Sans Pro Black', '22', 'bold'))
        self.LPing.grid(column=2, row=1)

        # Positionnement des stats (cercles + valeurs)
        self.LRondValeursDl = ttk.Label(frame, image=app.new_imageValeurs, background=couleurbg)
        self.LRondValeursDl.grid(column=0, row=2)

        # pady=[x,y] -> x décalage avec le haut (descend le label) et y avec le bas
        self.ValeursDl = ttk.Label(frame, text=vDl, background=couleurbg, font=('Source Sans Pro Black', '28', 'bold'))
        self.ValeursDl.grid(column=0, row=2, pady=[0,50])

        self.LValeursDl = ttk.Label(frame, text="MBIT/S", background=couleurbg, font=('Source Sans Pro Black', '15', 'bold'))
        self.LValeursDl.grid(column=0, row=2, pady=[50,0])



        self.LRondValeursUl = ttk.Label(frame, image=app.new_imageValeurs, background=couleurbg)
        self.LRondValeursUl.grid(column=1, row=2)

        self.ValeursUl = ttk.Label(frame, text=vUl, background=couleurbg, font=('Source Sans Pro Black', '28', 'bold'))
        self.ValeursUl.grid(column=1, row=2, pady=[0,50])

        self.LValeursUl = ttk.Label(frame, text="MBIT/S", background=couleurbg, font=('Source Sans Pro Black', '15', 'bold'))
        self.LValeursUl.grid(column=1, row=2, pady=[50,0])



        self.LRondValeursPing = ttk.Label(frame, image=app.new_imageValeurs, background=couleurbg)
        self.LRondValeursPing.grid(column=2, row=2)

        self.ValeursPing = ttk.Label(frame, text=VPing, background=couleurbg, font=('Source Sans Pro Black', '28', 'bold'))
        self.ValeursPing.grid(column=2, row=2, pady=[0,50])

        self.LValeursPing = ttk.Label(frame, text="MS", background=couleurbg, font=('Source Sans Pro Black', '15', 'bold'))
        self.LValeursPing.grid(column=2, row=2, pady=[50,0])