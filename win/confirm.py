import tkinter as tk
from base import baseWin


class cfmWin(baseWin):
    def __init__(self, msg, title='Confirm', okBtnTxt='OK', ngBtnTxt='cancel'):
        # init
        super().__init__()
        self.root.title(title)
        self.bool = False
        # widget
        frame = tk.Frame(self.root)
        label = tk.Label(
            frame,
            text=msg, justify="left")
        ngBotton = tk.Button(
            frame,
            text=ngBtnTxt,
            command=self.root.destroy)
        okButton = tk.Button(
            frame,
            text=okBtnTxt,
            command=self.endWithTrue)
        # pack
        frame.pack(fill='both', expand=True)
        label.pack(padx=20, pady=10)
        ngBotton.pack(side='left', fill='x', expand=True)
        okButton.pack(side='left', fill='x', expand=True)

    def endWithTrue(self):
        self.bool = True
        self.root.destroy()

    def getBool(self):
        self.root.wait_window()
        return self.bool


def show(msg):
    return cfmWin(msg).getBool()
