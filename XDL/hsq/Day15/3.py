import tkinter

win = tkinter.Tk()
win.title("GUI")
win.geometry("400x400+800+50")

e = tkinter.Variable()

def myfun():
	print(e.get())

entry = tkinter.Entry(win,show="#",textvariable=e)
entry.pack(side=tkinter.LEFT,fill=)

button1 = tkinter.Button(win,text="提交",command=myfun)
button1.pack()

button2 = tkinter.Button(win,text="退出",command=win.quit)
button2.pack()

win.mainloop()