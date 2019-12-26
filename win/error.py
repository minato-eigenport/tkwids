import tkinter as tk
from base import baseWin


class errWin(baseWin):
    def __init__(self, msg, title='Message', okBtnTxt='OK'):
        # init
        super().__init__()
        self.root.title(title)
        # widget
        frame = tk.Frame(self.root)
        label = tk.Label(
            frame, foreground='red',
            text=msg, justify="left")
        okButton = tk.Button(
            frame,
            text=okBtnTxt,
            command=self.root.destroy)
        # pack
        frame.pack(fill='both', expand=True)
        label.pack(padx=20, pady=10)
        okButton.pack(fill='x', expand=True)


class critErrWin(baseWin):
    def __init__(self, msg, title='Message', okBtnTxt='OK'):
        # init
        super().__init__()
        self.root.title(title)
        # widget
        frame = tk.Frame(self.root)
        label = tk.Label(
            frame, foreground='red',
            text=msg, justify="left")
        okButton = tk.Button(
            frame,
            text=okBtnTxt,
            command=quit)
        # pack
        frame.pack(fill='both', expand=True)
        label.pack(padx=20, pady=10)
        okButton.pack(fill='x', expand=True)


def show(msg):
    errWin(msg).root.wait_window()
    return True


def showCrit(msg):
    critErrWin(msg)