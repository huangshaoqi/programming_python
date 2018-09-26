# tkinter模块
## 组件1 按钮(button)
### 具备以下属性
```
anchor  设置按钮中文字的对齐方式，相对于按钮的中心位置
background(bg) 设置按钮的背景颜色
foreground(fg) 设置按钮的前景色(文字的颜色)
borderwidth(bd) 设置按钮边框的宽度
cursor  设置鼠标再按钮上的样式
command 设置按钮点击时触发的函数
bitmap   设置按钮上显示的位图
font 设置按钮上文本的字体
width 设置按钮的宽度(字符个数)
height 设置按钮的高度(字符个数)
state 设置按钮的状态
text 设置按钮上的文字
image 设置按钮上的图片
```

## 组件2 文本框(Entry)和多行文本(Text)
### 具备以下属性
```
background(bg) 设置文本框的背景色
foreground(fg) 设置文本框的前景色
borderwidth(bd) 设置文本输入框的边框
font 设置文本框中的字体
width 设置文本框的宽度(字符个数)
height 设置文本框的高度(字符个数),仅限于text
state 设置文本框的状态
selectbackground 选中文字时文本框的背景色
selectforeground 选中文字时文字的颜色
show 指定文本框显示的字符,若为*,则表示为密码框
textvariable 设置文本对应的变量《可以通过修改变量改变文字显示,必须使用tkinter.Invar()或tkinter.StringVar()产生的变量，entry可以使用
```

## 组件3 标签(Lebal)
### 具备以下属性
```
anchor 设置文本相对于标签中心的位置
foreground 设置标签的前景色
background 设置标签的背景色
borderwidth 设置标签的前景色
width 设置标签的宽度(字符个数)
height 设置标签的高度(字符个数)
text 设置表中的文本内容
font 设置标签文字的字体类型
bitmap 设置标签的显示的位图
image 设置标签中显示的图片
justify 是设置标签中多行文本的对齐方式
textvariable 设置对应的变量,可以通过修改变量改变文字显示,必须使用tkinter.Invar()或者tkinter.StringVar()产生变量
```

## 事件绑定
### 鼠标事件类型
```
<Button-1>          按下了鼠标左键        <ButtonPress-1>
<Button-2>          按下了鼠标中键        <ButtonPress-2>
<Button-3>          按下了鼠标右键        <ButtonPress-3>
<Enter>             鼠标进入组件区域
<Leave>             鼠标离开组件区域
<ButtonRelease-1>   释放了鼠标左键
<ButtonRelease-2>   释放了鼠标中键
<ButtonRelease-3>   释放了鼠标右键
<B1-Moion>          按住鼠标左键移动
<B2-Moion>          按住鼠标中键移动
<B3-Moion>          按住鼠标右键移动 
<Double-Button-1>   双击鼠标左键
<Double-Button-2>   双击鼠标中键
<Double-Button-3>   双击鼠标右键
<MouseWheel>        滚动鼠标滚轮
```
### 键盘事件类型
```
<KeyPress>                 表示任何键盘按下
<KeyPress-A>               表示按下键盘A键    A可以设置为其他的按键
<Alt-KeyPress-A>           表示同时按下Alt和A键    A可以设置为其他的按键
<Control-KeyPress-A>       表示同时按下Ctrl和A键    A可以设置为其他的按键
<Shift-KeyPress-A>         表示同时按下Shift和A键    A可以设置为其他的按键
<Double-KeyPress-A>        表示双击键盘A键    A可以设置为其他的按键
<Lock-KeyPress-A>          表示开启大写之后键盘A键    A可以设置为其他的按键
<Alt-Control-KeyPress-A>   表示同时按下alt+Ctrl和A键    A可以设置为其他的按键
注意：键盘事件除了entry和text组件其他组件的事件最好绑定在主界面上
```
### 事件对象中包含的信息
```
x,y              当前触发事件时鼠标相对触发事件的组件的坐标值
x_root,y_root    当前触发事件时鼠标相对于屏幕的坐标值
char             获取当前键盘事件时按下的键对应的字符
keycode          获取当前键盘事件时按下的键对应的的ascii码
type             获取事件的类型
num              获取鼠标按键类型  123 左中右
widget           触发事件的组件
width/height     组件改变之后的大小和configure()相关
```

### 事件对象中包含的信息
```
x,y              当前触发事件时鼠标相对触发事件的组件的坐标值
x_root,y_root    当前触发事件时鼠标相对于屏幕的坐标值
char             获取当前键盘事件时按下的键对应的字符
keycode          获取当前键盘事件时按下的键对应的的ascii码
type             获取事件的类型
num              获取鼠标按键类型  123 左中右
widget           触发事件的组件
width/height     组件改变之后的大小和configure()相关
```

### 窗口和组件相关事件类型
```
Activate         当中组件由不可以用变为可用时  针对于state的变值
Deactivate       当组件由可用变为不可用时触发
Configure        当组件大小发生变化时触发
Destory          当组件销毁时触发
FocusIn          当组件获取焦点时触发 针对于Entry和Text有效
Map              当组件由隐藏变为显示时触发
UnMap            当组件由显示变为隐藏时触发
Perproty         当窗口属性发生变化时触发
```
