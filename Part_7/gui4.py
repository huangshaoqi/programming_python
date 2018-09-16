from tkinter import *


def greeting():
    print("Hello GUI")


win = Frame()
win.pack()

Label(win, text="Hello gui world").pack(side=TOP)
Button(win, text="hello", command=greeting).pack(side=LEFT)
Button(win, text="quit", command=win.quit).pack(side=RIGHT)
win.mainloop()
