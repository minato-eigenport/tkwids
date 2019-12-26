

import tkinter as tk
import os
import sys


if __name__ == "__main__":
    # path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    # import
    import error

    #
    try:
        raise(Exception())
        root = tk.Tk()
        b1 = tk.Button(root,
                       text='close',
                       command=quit)
        b1.pack(fill='x', pady=8)

        root.mainloop()
    except:
        error.showInitError("error has happend")
