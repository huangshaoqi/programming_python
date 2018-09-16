from tkinter import *

root = Tk()
widget = Button(root, text='Press', command=root.quit)
widget.pack(side=LEFT, expand=YES)
mainloop()
