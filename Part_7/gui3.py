from tkinter import *


def quit():
    print('I exit !')
    sys.exit()


root = Tk()

widget = Button(root, text='press this', command=quit)
widget.pack(expand=YES, side=TOP)
root.title('gui3.py')
root.mainloop()
