from tkinter import *

root = Tk()
widget = Label(root)
widget.config(text='Hello GUI world')
widget.pack(expand=YES, fill=BOTH, side=TOP)
root.title('gui1g.py')
root.mainloop()
