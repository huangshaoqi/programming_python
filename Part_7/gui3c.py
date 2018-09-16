from tkinter import *
import sys


class HelloGUI:
    def __init__(self):
        widget = Button(None, text="press", command=self.quit)
        widget.pack(side=TOP)

    def quit(self):
        print("I exit ...")
        sys.exit()


HelloGUI()
mainloop()
