## os模块

**os.name**

**输出字符串指示正在使用的平台。如果是window 则用'nt'表示，对于Linux/Unix用户，它是'posix'。**

```python
result = os.name
print(result)
```

**os.getcwd()**

**函数得到当前工作目录(就是你的进程所工作的目录)，即当前Python脚本工作的目录路径。**

**运行目录：执行程序的路径**

**工作目录：程序运行时，程序中我们要操作的一系列相对路径（相对路径需要参照），以运行时目录为参照。并且可在程序运行时更改**

```python
result = os.getcwd()
print(result)
```

**os.listdir()**

**返回指定目录下的所有文件和目录名的一个列表**，**但是并没有列出来什么是目录，什么是文件。**

```python
result = os.listdir("D:\兄弟连\python12期\一阶段\代码和笔记\day11")
print(result)
```

**os.remove(＇file_name＇)**

**删除指定文件**

**os.rmdir(＇dir_name＇)**

**删除指定目录**

```python
os.rmdir("day12")
```

**os.mkdir(＇dir_name＇)**

**创建目录**

```python
os.mkdir("../day12")
```

**os.makedirs(＇a/b/c＇)**

**递归创建目录**

```python
os.makedirs("day12/day13/day14")
```

**os.system(＇command＇)**

**执行shell命令**

```python
os.system("ping www.baidu.com")
```

**os.chdir(＇file_path＇)**

**改变工作目录**

```python
result = os.listdir("../")
print(result)
print(os.getcwd())
os.chdir("../day10")
print(os.getcwd())
```

**os.rename**

**更改文件名**

```python
os.rename("02.py","01.py")
```

**os.walk(top, topdown=True, onerror=None, followlinks=False)**

**这个函数会返回三个返回值，(dirpath,dirnames,filenames)**

**dirpath:目录的路径**

**dirnames:你要查找目录下面所有的目录名**

**filenames:你要查找目录下面所有的文件名**

**os.sep 是当前路径分隔符号**

**我们使用这个os.walk也可以起到遍历一个目录的效果。**

```python
result = os.walk("../")
for path,dirname,filename in result:
    print(filename)
```

## os.path

**os.path.abspath(＇file_name＇)**

**返回file_name的绝对路径**

```python
result = os.path.abspath("01.py")
print(result)
```

**os.path.split(＇file_path＇)**

**返回file_path分隔成目录和文件名，并用一个元组返回**

```python
result = os.path.split("D:\兄弟连\python12期\一阶段\代码和笔记\day11\\01.py")
print(result)
```

**os.path.exists(＇file_path＇)**

**如果file_path存在，则返回True，反之返回False**

```python
result = os.path.exists("D:\兄弟连\python12期\一阶段\代码和笔记\day12")
print(result)
```

**os.path.join(＇file_path＇，＇file_name＇)**

**链接目录与文件名或目录**

```python
result = os.path.join("D:\兄弟连\python12期\一阶段\代码和笔记","day12")
print(result)
```

**os.path.isdir(＇name＇)**  **bool**

**判断是否为目录**

```python
result = os.path.isdir("../01.py")
print(result)
```

**os.path.isfile(＇name＇)**  **bool**

**判断是否为文件**

```python
result = os.path.isfile("../day1")
print(result)
```

**os.path.getsize(＇path＇)**

**返回文件大小，如果文件不存在，就返回错误**

```python
result = os.path.getsize("D:/兄弟连/python12期/一阶段/代码和笔记/day11/02.py")
print(result)
```

## 递归函数

**所谓的函数递归调用，就是函数可以在其声明的执行顺序之中调用执行自己。**

**函数递归的好处：精简程序执行中的重复调用**

 

**一个经典的递归实例：求阶乘**

```python
def func(n):
#如果 n == 1 的时候 返回 1
    if n == 1:
        return 1
    else:
        return func(n-1)*n
result = func(5)
print(result)

"""
执行流程:
func(5)
func(4)*5 --> func(3)*4*5 --> func(2)*3*4*5 --> func(1)*2*3*4*5 --> 1*2*3*4*5 ---> 120
"""
```

**尾递归**

```python
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(997))
```

**递归方式，计算1到100之和**

```python
# def func(n):
#     if n == 1:
#         return 1
#     else:
#         return func(n-1)+n
# result = func(100)
# print(result)
```

**斐波那契数列即著名的兔子数列：**

**1、1、2、3、5、8、13、21、34、……n?**

```python
def func(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return func(n-1)+func(n-2)
result = func(10)
print(result)
```

**汉诺塔游戏：**

**上帝创造世界的时候做了三根金刚石柱子，在一根柱子上从下往上安大小顺序摞着64片黄金圆盘。上帝命令婆罗门把圆盘从下面开始按大小顺序重新摆放在另一根柱子上。并且规定，在小圆盘上不能放大圆盘，在三根柱子之间一次只能移动一个圆盘。**

```python
# 参数:n代表盘子的个数   a,b,c分别代表三个柱子
def hannoi(n,a,b,c):
    # 给递归一个出口  只有一个盘子的时候 直接从a移动到c
    if n == 1:
        print(a,"--->",c)
    else:
        # 除了最大的圆盘  其它的圆盘全部通过c柱子移动到b柱子
        hannoi(n-1,a,c,b)
        # 把a柱子上最大的圆盘移动到c柱子上  此时a柱子上没有圆盘了
        print(a,"--->",c)
        # 把b柱子上的n-1个圆盘  通过a移动到c
        hannoi(n-1,b,a,c)
hannoi(64,"a","b","c")
```

