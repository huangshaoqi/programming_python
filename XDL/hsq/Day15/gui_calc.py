import tkinter

# 定义主窗口
root = tkinter.Tk()
root.title("Python计算器")
root.iconbitmap("calc.ico")

# 固定窗口大小
root.maxsize(380,405)
root.minsize(380,405)
# 窗口位置
root.geometry("380x405+800+100")

# 创建框架
fram1 = tkinter.Frame(root, height=480)

# 输入内容与计算结果通过Entry输入框显示
# content = tkinter.WtringVar()
text = tkinter.Text(fram1, font=("楷体", 22), bg="#D0D0D0", width=25, height=5)
text.grid(row=0, column=0, columnspan=4)
text.grid_propagate(0)

# 按钮样式
style = {
    "bg": "#F8F8F8",
    "font": ("楷体", 22),
    "width": 5,
    "height": 1
}

# 定义各按钮
button_Clean_last = tkinter.Button(fram1, text="CE", command="", **style)
button_Clean = tkinter.Button(fram1, text="C", command="", **style)
button_delete = tkinter.Button(fram1, text="del", command="", **style)
button_division = tkinter.Button(fram1, text="÷", command="", **style)
button_7 = tkinter.Button(fram1, text="7", command="", **style)
button_8 = tkinter.Button(fram1, text="8", command="", **style)
button_9 = tkinter.Button(fram1, text="9", command="", **style)
button_multiplication = tkinter.Button(fram1, text="×", command="", **style)
button_4 = tkinter.Button(fram1, text="4", command="", **style)
button_5 = tkinter.Button(fram1, text="5", command="", **style)
button_6 = tkinter.Button(fram1, text="6", command="", **style)
button_subtraction = tkinter.Button(fram1, text="-", command="", **style)
button_1 = tkinter.Button(fram1, text="1", command="", **style)
button_2 = tkinter.Button(fram1, text="2", command="", **style)
button_3 = tkinter.Button(fram1, text="3", command="", **style)
button_addition = tkinter.Button(fram1, text="+", command="", **style)
button_a_s = tkinter.Button(fram1, text="±", command="", **style)
button_0 = tkinter.Button(fram1, text="0", command="", **style)
button_spot = tkinter.Button(fram1, text=".", command="", **style)
button_equal = tkinter.Button(fram1, text="=", command="", **style)

# 按钮列表，后面循环绑定事件用
buttons = [
    button_Clean_last,
    button_Clean,
    button_delete,
    button_division,
    button_7,
    button_8,
    button_9,
    button_multiplication,
    button_4,
    button_5,
    button_6,
    button_subtraction,
    button_1,
    button_2,
    button_3,
    button_addition,
    button_a_s,
    button_0,
    button_spot,
    button_equal
]


# 输入进入事件
def Enter(event):
    event.widget.config(bg="#B8B8B8")


# 鼠标离开时间
def Leave(event):
    event.widget.config(bg="#F8F8F8")

# 绑定事件
for button in buttons:
    button.bind("<Enter>", Enter)
    button.bind("<Leave>", Leave)
    button.grid_propagate(0)


# 输入内容和计算结果显示区域
fram1.pack(side=tkinter.TOP, fill=tkinter.X)

# 网格布局按钮
sticky = tkinter.N + tkinter.E + tkinter.W

button_Clean_last.grid(row=1, column=0, sticky=sticky)
button_Clean.grid(row=1, column=1, sticky=sticky)
button_delete.grid(row=1, column=2, sticky=sticky)
button_division.grid(row=1, column=3, sticky=sticky)
button_7.grid(row=2, column=0, sticky=sticky)
button_8.grid(row=2, column=1, sticky=sticky)
button_9.grid(row=2, column=2, sticky=sticky)
button_multiplication.grid(row=2, column=3, sticky=sticky)
button_4.grid(row=3, column=0, sticky=sticky)
button_5.grid(row=3, column=1, sticky=sticky)
button_6.grid(row=3, column=2, sticky=sticky)
button_subtraction.grid(row=3, column=3, sticky=sticky)
button_1.grid(row=4, column=0, sticky=sticky)
button_2.grid(row=4, column=1, sticky=sticky)
button_3.grid(row=4, column=2, sticky=sticky)
button_addition.grid(row=4, column=3, sticky=sticky)
button_a_s.grid(row=5, column=0, sticky=sticky)
button_0.grid(row=5, column=1, sticky=sticky)
button_spot.grid(row=5, column=2, sticky=sticky)
button_equal.grid(row=5, column=3, sticky=sticky)


root.mainloop()
