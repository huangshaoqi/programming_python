from tkinter import *
from tkinter.messagebox import *


def callback():
    if askyesno('Verify', 'Do you really want to quit?'):
        showwarning('Yes', 'Quit not yet implemeted')
    else:
        showinfo('No', 'Quit has been cancelled')


errmsg = 'Sorry ,no Spam allowed!'
Button(text='Quit', command=callback).pack()
Button(text='Spam', command=(lambda: showerror('Spam', errmsg))).pack()
mainloop()
