from tkinter import *

root = Tk()

label_font = ("times", 20, "bold")
widget = Label(root, text="Hello config world")
widget.config(bg='black', fg='yellow')
widget.config(font=label_font)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.title("GUI")
root.mainloop()
