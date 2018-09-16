from tkinter import *


class Hello(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack()
        self.data = 42
        self.make_widgets()

    def make_widgets(self):
        widget = Button(self, text="Hello GUI World", command=self.message)
        widget.pack(side=LEFT)

    def message(self):
        self.data += 1
        print("Hello Fram world %s !" % self.data)


if __name__ == '__main__':
    Hello().mainloop()
