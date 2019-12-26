import tkinter as tk


class baseWin():
    def __init__(self,):
        window = tk.Toplevel()
        self.root = window
        self.root.resizable(False, False)
        self.root.grab_set()

    def center(self):
        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(
            self.root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(
            self.root.winfo_screenheight()/2 - windowHeight/2)
        self.root.geometry("+{}+{}".format(positionRight, positionDown))

    def noWinBar(self):
        self.root.overrideredirect(1)
