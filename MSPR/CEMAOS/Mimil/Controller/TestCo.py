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


def FctTestCOTestDebit(self):
    self.BTest.configure(state=tk.DISABLED)
    for j in range(10):
        DL=random.choice(l)
        UL=random.choice(l)
        Pi=get_ping_latency('8.8.8.8')
        self.testsdebit.ValeursDl.configure(text=DL)
        self.testsdebit.ValeursUl.configure(text=UL)
        self.testsdebit.ValeursPing.configure(text=Pi)
        self.update()
        sleep(1)
    self.BTest.configure(state=tk.NORMAL)

def FctTestCODashboard(self):
    DL=random.choice(l)
    UL=random.choice(l)
    Pi=get_ping_latency('8.8.8.8')
    self.testdashboard.ValeursDl.configure(text=DL)
    self.testdashboard.ValeursUl.configure(text=UL)
    self.testdashboard.ValeursPing.configure(text=Pi)
    self.update()
