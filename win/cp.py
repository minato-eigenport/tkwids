import tkinter as tk
from base import baseWin


class copyWin(baseWin):
    def __init__(self, msg, title='About', okBtnTxt='OK', cpBtnTxt='COPY', nobar=False):
        # init
        super().__init__()
        self.root.title(title)
        if nobar:
            self.root.overrideredirect(1)
        # widget
        frame = tk.Frame(self.root)
        label = tk.Label(
            frame,
            text=msg, justify="left")
        ngBotton = tk.Button(
            frame,
            text=cpBtnTxt,
            command=lambda: self.copy2Clipboard(msg))
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

    def copy2Clipboard(self, msg):
        self.root.clipboard_clear()
        self.root.clipboard_append(msg)


def show(msg):
    return copyWin(msg).getBool()
