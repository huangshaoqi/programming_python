import tkinter

win = tkinter.Tk()

win.geometry("400x400+600+20")


def myfunc():
    if value.get():
        text.delete(0.0, tkinter.END)
        text.insert(tkinter.INSERT, "按钮%s被选中\n" % value.get())
        print("按钮%s被选中" % value.get())



value = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(
    win, text="按钮1", value=1, variable=value, command=myfunc)


radiobutton2 = tkinter.Radiobutton(
    win, text="按钮2", value=2, variable=value, command=myfunc)


radiobutton3 = tkinter.Radiobutton(
    win, text="按钮3", value=3, variable=value, command=myfunc)


text = tkinter.Text(win, width=200, height=50)

radiobutton1.pack()
radiobutton2.pack()
radiobutton3.pack()
text.pack()
win.mainloop()
