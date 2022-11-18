from View.GUI import FenetrePrincipale

class App:
    def __init__(self):
        self.gui = FenetrePrincipale()


if __name__ == "__main__":
    from tkinter import Tk
    app = App()
    app.mainloop()