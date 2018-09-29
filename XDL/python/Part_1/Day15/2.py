import tkinter

win = tkinter.Tk()
win.title("GUI")
win.geometry("400x400+800+50")


def myfun():
	print("Welcome to GUI World!")

button = tkinter.Button(win,
                        text="Press",
                        command=myfun,
                        width=5,
                        height=2,
                        )

button.pack()
win.mainloop()
