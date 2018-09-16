from tkinter import *
import sys


class GUICALLABLE:
    def __init__(self):
        self.msg = "this is __call__"

    def __call__(self):
        print(self.msg)
        sys.exit()


widget = Button(text="press", command=GUICALLABLE())
widget.pack(side=TOP)
mainloop()
