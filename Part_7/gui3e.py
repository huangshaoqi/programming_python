from tkinter import *
import sys


def hello(event):
    print("press twice to exit")


def quit(event):
    print("Hello ,i must be going...")
    sys.exit()


widget = Button(text="Press")
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit)
widget.pack(side=TOP)
mainloop()
