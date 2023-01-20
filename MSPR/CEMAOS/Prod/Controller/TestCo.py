import tkinter as tk
from tkinter import ttk
from View.Frame_Performances_Co import StatCo
from time import sleep
from Controller.ping import get_ping
from Controller.Upload_Download_script import get_speed


def FctTestCOTestDebit(self):
    self.BTest.configure(state=tk.DISABLED)
    download_speed, upload_speed = get_speed()
    Pi=get_ping('8.8.8.8')
    print(download_speed)
    self.testsdebit.ValeursDl.configure(text=download_speed)
    self.testsdebit.ValeursUl.configure(text=upload_speed)
    self.testsdebit.ValeursPing.configure(text=Pi)
    self.update()
    self.BTest.configure(state=tk.NORMAL)

def FctTestCODashboard(self):
    download_speed, upload_speed = get_speed()
    Pi=get_ping('8.8.8.8')
    self.testdashboard.ValeursDl.configure(text=download_speed)
    self.testdashboard.ValeursUl.configure(text=upload_speed)
    self.testdashboard.ValeursPing.configure(text=Pi)
    self.update()