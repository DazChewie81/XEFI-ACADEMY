import tkinter as tk
from tkinter import ttk

def StatCo(self, frame, couleurbg, vDl, vUl, VPing):
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