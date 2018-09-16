from tkinter import *

"""
组件尺寸调整
expand 要求打包几何管理器为组件扩展空间，通常可以是父组件中任何未被占用的地方（是组件居中）
fill 可以用来拉伸组件，使其充满分配的空间 （垂直拉伸为Y，水平拉伸为X，同时为BOTH）
"""
Label(text='Hello GUI world').pack(expand=YES, fill=BOTH)
mainloop()
