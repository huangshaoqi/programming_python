import tkinter
import os
win = tkinter.Tk()

win.title("文件读取")
win.geometry("500x500+600+20")

fram1 = tkinter.Frame(win)
fram2 = tkinter.Frame(win)
fram1.pack(side=tkinter.TOP,anchor="w",fill=tkinter.X,ipadx=1.0,ipady=1.0)
fram2.pack(side=tkinter.TOP)

text_content = tkinter.Variable()


def open_file():

    file_path = os.path.abspath(text_content.get())
    text.delete(0.0,tkinter.END)
    with open(file_path, "r",encoding="utf-8") as f:
        content = f.read()
    text.insert(tkinter.INSERT, content)


def save_file():
    file_path = os.path.abspath(text_content.get())
    content = text.get(0.0,tkinter.END)
    with open(file_path, "w",encoding="utf-8") as f:
    	content = f.write(content)


entry = tkinter.Entry(fram1, textvariable=text_content,width=30)
open_button = tkinter.Button(fram1, text="Open", command=open_file)
read_button = tkinter.Button(fram1, text="Save", command=save_file)
text = tkinter.Text(fram2, width=200, height=50)


entry.pack(side=tkinter.LEFT)
open_button.pack(side=tkinter.LEFT)
read_button.pack(side=tkinter.LEFT)
text.pack()


win.mainloop()
