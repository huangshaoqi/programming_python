import tkinter

win = tkinter.Tk()

win.title("GUI")
win.geometry("400x400+600+20")


def func():
    message = ""
    if result1.get():
        message += "小红\n"
    if result2.get():
        message += "小军\n"
    if result3.get():
        message += "小黑\n"
    text.delete(0.0, tkinter.END)
    text.insert(tkinter.INSERT, message)

result1 = tkinter.BooleanVar()
checkbutton = tkinter.Checkbutton(
    win, text="小红", variable=result1, command=func)
checkbutton.pack()

result2 = tkinter.BooleanVar()
checkbutton2 = tkinter.Checkbutton(
    win, text="小军", variable=result2, command=func)
checkbutton2.pack()

result3 = tkinter.BooleanVar()
checkbutton3 = tkinter.Checkbutton(
    win, text="小黑", variable=result3, command=func)
checkbutton3.pack()

text = tkinter.Text(win, width=100, height=50)
text.pack()

scroll = tkinter.Scrollbar()
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)


scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


win.mainloop()
