import tkinter

win = tkinter.Tk()

win.title("GUI")
win.geometry("400x400+600+20")


text = tkinter.Text(win, width=100, height=50)


scroll1 = tkinter.Scrollbar()
scroll1.pack(side=tkinter.RIGHT, fill=tkinter.Y)

scroll2 = tkinter.Scrollbar()
scroll2.pack(side=tkinter.BOTTOM, fill=tkinter.X)

text.pack()


scroll1.config(command=text.yview)
text.config(yscrollcommand=scroll1.set)

scroll2.config(command=text.xview)
text.config(xscrollcommand=scroll2.set)


win.mainloop()
