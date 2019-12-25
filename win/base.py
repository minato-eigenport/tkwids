import tkinter as tk


class baseWin():
    def __init__(self,):
        window = tk.Toplevel()
        self.root = window
        self.root.resizable(False, False)
        self.root.grab_set()
