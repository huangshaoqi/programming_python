from gui6 import Hello
from tkinter import *
from sys import exit

parent = Frame()
parent.pack()

Hello(parent).pack(side=RIGHT)
Button(parent, text="ATTACH", command=exit).pack(side=LEFT)
parent.mainloop()
