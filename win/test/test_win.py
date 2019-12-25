

import tkinter as tk
import os
import sys


def testMessageWin():
    return message.show('This is Message window')


def testConfirmWin():
    return confirm.show('This is Confirm window')


def runTest():
    if testConfirmWin():
        if testMessageWin():
            runTest()


if __name__ == "__main__":
    # path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    # import
    import message
    import confirm
    root = tk.Tk()
    b = tk.Button(root, text='this is the button to start',
                  command=runTest)
    b.pack()
    #
    root.mainloop()
