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


# 全部删除
def Clean():
    text.delete(0.0, tkinter.END)


# 一个字符一个字符的删除
def Del():
    content = text.get(0.0, tkinter.END)[:-2]
    text.delete(0.0, tkinter.END)
    text.insert(0.0, content)


# 删除上一次的输入
def Clean_last():
    content = text.get(0.0, tkinter.END)[:-1]
    for symbol in ["+", "-", "*", "÷"]:
        if content.find(symbol) != -1:
            content = content.split(symbol)[0]
            text.delete(0.0, tkinter.END)
            text.insert(0.0, content + symbol)


# 打印字符
def print_symbol(symbol):
    def Symbol():
        content = text.get(0.0, tkinter.END)[:-1]
        text.delete(0.0, tkinter.END)
        content += symbol
        text.insert(0.0, content)

    return Symbol


# 等于号计算
def calc():
    content = text.get(0.0, tkinter.END)[:-1]
    text.delete(0.0, tkinter.END)
    text.insert(0.0, eval(content))


# 正负号添加
def add_sub():
    content = text.get(0.0, tkinter.END)[:-1]
    if content.startswith("-"):
        content = text.get(0.0, tkinter.END)[:-1][1:]
    else:
        content = "-" + text.get(0.0, tkinter.END)[:-1]
    text.delete(0.0, tkinter.END)
    text.insert(0.0, content)


# 按钮样式
style = {
    "bg": "#F8F8F8",
    "font": ("楷体", 22),
    "width": 5,
    "height": 1
}

# 定义各按钮
button_Clean_last = tkinter.Button(fram1, text="CE", command=Clean_last, **style)
button_Clean = tkinter.Button(fram1, text="C", command=Clean, **style)
button_delete = tkinter.Button(fram1, text="del", command=Del, **style)
button_division = tkinter.Button(fram1, text="÷", command=print_symbol("÷"), **style)
button_7 = tkinter.Button(fram1, text="7", command=print_symbol("7"), **style)
button_8 = tkinter.Button(fram1, text="8", command=print_symbol("8"), **style)
button_9 = tkinter.Button(fram1, text="9", command=print_symbol("9"), **style)
button_multiplication = tkinter.Button(fram1, text="*", command=print_symbol("*"), **style)
button_4 = tkinter.Button(fram1, text="4", command=print_symbol("4"), **style)
button_5 = tkinter.Button(fram1, text="5", command=print_symbol("5"), **style)
button_6 = tkinter.Button(fram1, text="6", command=print_symbol("6"), **style)
button_subtraction = tkinter.Button(fram1, text="-", command=print_symbol("-"), **style)
button_1 = tkinter.Button(fram1, text="1", command=print_symbol("1"), **style)
button_2 = tkinter.Button(fram1, text="2", command=print_symbol("2"), **style)
button_3 = tkinter.Button(fram1, text="3", command=print_symbol("3"), **style)
button_addition = tkinter.Button(fram1, text="+", command=print_symbol("+"), **style)
button_a_s = tkinter.Button(fram1, text="±", command=add_sub, **style)
button_0 = tkinter.Button(fram1, text="0", command=print_symbol("0"), **style)
button_spot = tkinter.Button(fram1, text=".", command=print_symbol("."), **style)
button_equal = tkinter.Button(fram1, text="=", command=calc, **style)

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
