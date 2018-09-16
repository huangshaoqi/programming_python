"""
图形化用户界面
"""
from tkinter import Label  # 导入组件对象

widget = Label(None, text='Hello GUI World!')  # 生成（标签类）
widget.pack()  # 布置(打包新标签)
widget.mainloop()  # 开始事件循环（调用主循环、显示窗口）
