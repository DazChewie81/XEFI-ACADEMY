import tkinter as tk
from tkinter import ttk
from View.Frame_Performances_Co import StatCo
from time import sleep
from Controller.ping import get_ping_latency


#! Juste pour faire des essais
import random
l=[]
for i in range(500):
    l.append(i)
#! Juste pour faire des essais

def TestsDebit(self):
    self.FTestDebit = tk.Frame(self.FDebit, bg=self.page_selectionnee)
    self.FTestDebit.pack(fill ='both')
    self.testsdebit=StatCo(self, self.FTestDebit, self.page_selectionnee, '---', '---', '---')

    # Bouton qui lance le test de débit
    self.BTest = ttk.Button(self.FDebit, text="Lancer le test", command=lambda:{FctTestCO(self)})
    self.BTest.pack(anchor=tk.W, padx=[15,15], pady=[15,15])

def FctTestCO(self):
    print("CA COMMENCE")
    self.BTest.configure(state=tk.DISABLED)
    for j in range(10):
        DL=random.choice(l)
        UL=random.choice(l)
        Pi=get_ping_latency('8.8.8.8')
        self.testsdebit.ValeursDl.configure(text=DL)
        self.testsdebit.ValeursUl.configure(text=UL)
        self.testsdebit.ValeursPing.configure(text=Pi)
        print(self.testsdebit.ValeursPing.cget("text"))
        sleep(1)
        self.update()
    self.BTest.configure(state=tk.NORMAL)
        

