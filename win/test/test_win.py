

import tkinter as tk
import os
import sys


def testMessageWin():
    return message.show('This is Message window')


def testConfirmWin():
    return confirm.show('This is Confirm window')


def testErrorWin():
    return error.show('This is Error window')


def testCritErrorWin():
    return error.showCrit('This is Crit Error window')


def testAskYnWin():
    return askyn.show('This is askyn window')


def runTest1():
    if testConfirmWin():
        if testMessageWin():
            runTest1()


def runTest2():
    testErrorWin()


def runTest3():
    testCritErrorWin()


def runTest4():
    bool = testAskYnWin()
    message.show('You got '+str(bool))


def runTest5():
    cp.show('this message will copied')


if __name__ == "__main__":
    # path
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    # import
    import message
    import confirm
    import error
    import askyn
    import cp
    #
    root = tk.Tk()
    b1 = tk.Button(root,
                   text='this is the button to test cfm and msg ',
                   command=runTest1)
    b2 = tk.Button(root,
                   text='this is the button to test err',
                   command=runTest2)
    b3 = tk.Button(root,
                   text='this is the button to test crit err',
                   command=runTest3)
    b4 = tk.Button(root,
                   text='this is the button to test askyn err',
                   command=runTest4)
    b5 = tk.Button(root,
                   text='this is the button to test cp',
                   command=runTest5)
    b1.pack(fill='x', pady=8)
    b2.pack(fill='x', pady=8)
    b3.pack(fill='x', pady=8)
    b4.pack(fill='x', pady=8)
    b5.pack(fill='x', pady=8)
    #
    root.mainloop()
