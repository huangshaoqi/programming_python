import tkinter

win = tkinter.Tk()
win.title("GUI")
win.geometry("400x400+800+50") #设置窗体大小和位置
lable = tkinter.Label(win, text="Hello Gui!",
                      bg="yellow",			# 背景颜色
                      font=("黑体", 20),		# 字体类型
                      fg="red",				# 字体颜色
                      width=15, height=2, # 宽度、高度
                      # wraplength=15,		# 每行的宽度，超过宽度换行
                      # justify="left", # left、right 对齐方式
                      # anchor="nw"		# GUI位于屏幕方位
                      )

lable.pack()

win.mainloop()
