## 循环

### for...in...循环

语法：`for 变量 in 容器:`  for循环也可以称之为遍历

```python
# str = "这周末母亲节别再问你妈需要什么了，她可能需要的是像我这样的女婿"
#
# for var in str:
#     print(var)

#for循环列表
# list1 = ["鲁智深","孙悟空","唐僧","沙和尚","八戒"]
#
# for var in list1:
#     print(var)

#for循环元组

# tuple1 = ("鲁智深","孙悟空","唐僧","沙和尚","八戒")
#
# for var in tuple1:
#     print(var)

#for循环集合
# tuple1 = {"鲁智深","孙悟空","唐僧","沙和尚","八戒"}
#
# for var in tuple1:
#     print(var)

#for循环字典

dict = {"斗战胜佛":"孙悟空","净坛使者":"八戒","金身罗汉":"沙和尚","功德佛":"唐僧"}

# for key in dict:
#     print(key)

# for value in dict:
#     print(dict[value])
#
# for value in dict.values():
#     print(value)

# for key,value in dict.items():
#     print(key,value)

#二级列表的循环

# list1 = [
#     ["a","b","c"],
#     ["1","2","3"],
#     ["A","B","C"]
#         ]
#
# for a,b,c in list1:
#     print(a,b,c)


# tuple1 = (
#     ("a","b","c"),
#     ("1","2","3"),
#     ("A","B","C")
#         )
#
# for a,b,c in tuple1:
#     print(a)
#
# for var in tuple1:
#     print(var)


# set1 = {(1,2,3),(4,5,6),(7,8,9)}
# print(set1)
```

## 函数

语法

> def 函数名(参数1，参数2，参数3...参数n):
>
> ​	功能语句
>
> ​	return 表达式
>
> 函数名(参数1，参数2，参数3...参数n)

- def   这个是定义函数的关键字，当Python检测到你的代码里边有`def`这三个字母，那么Python就认为你要定义函数
- 函数名：要遵循变量的定义规则
- ()：括号是用来传递参数的，括号内的参数必须用逗号分开，在定义函数的时候传递的参数叫做形参，初学阶段我们可以把形参理解为变量名，他的值是从函数的调用者那里获取
- 功能语句：我们要打包的功能
- return：返回值，返回给函数调用者的值
- 表达式：返回给函数调用者的信息， 表达式可以位空，如果为空，默认返回一个None
- 函数调用：函数名+()，注意:括号不要丢掉，不带括号表示函数对象

```python
# print("一万行代码")
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%sx%s=%s"%(i,j,i*j),end=" ")
#         j += 1
#     print()
#     i += 1
#
#
# print("==========================一万行代码====================================")
#
# i = 1
# while i < 10:
#     j = 1
#     while j <= i:
#         print("%sx%s=%s"%(i,j,i*j),end=" ")
#         j += 1
#     print()
#     i += 1
#
# print("****************************一万行代码*********************************")

# def mut99():
#     #打印九九乘法表
#     i = 1
#     while i < 10:
#         j = 1
#         while j <= i:
#             print("%sx%s=%s"%(i,j,i*j),end=" ")
#             j += 1
#         print()
#         i += 1
# mut99()
#
# mut99()
#
# mut99()

# for var in range(100):
#     if var == 33:
#         pass
#     elif var == 55:
#         pass
#     elif var == 77:
#         pass
#     else:
#         print(var)

# def name():
#     print("周瑜打黄盖，看谁跑得快！")
#
# name()

#我们在定义函数的时候传递的参数叫做形参
# def name(user):
#     print("hello ",user)
# name("jack")
# #在调用函数的时候传递的参数叫做实参
# name("rose")

"""
多个参数：
位置参数:我们传递的实参是和形参一一对应关系
关键字参数:我们传递的实参如果和形参顺序不一致，那么我们的实参需要添加关键字来调整形参的值的顺序
默认值参数:我们在定义函数的时候可以给形参一个默认值，但是，默认值参数必须放到参数列表的最后，
            如果带默认值的参数在函数调用的时候又一次被赋值，那么就会覆盖掉默认值参数的值
"""

# def name(f_name, l_name="rose"):
#     print(f_name + " " + l_name)
# name("ada")

def func(user,name):
    print(user+" say hello to "+name)
# 关键字参数
func(name="jack",user="rose")

def operation(a,b,c,d):
    sum1 = a+b+c+d
    return sum1

op = operation(1,2,3,4)
print(op)
```

### 全局变量和局部变量

```python
# A = "我是全局变量A"
# def name():
#     global B
#     B = "我是局部变量B"
#     print(A)
#     print(B)
# name()
# print(A)
# print(B)

# A = "我是全局变量A"
# def name():
#     A = "我是局部变量A"
#     print(A)
# name()
```

### 不定长参数

```python
"""
普通参数：
1、可以接收关键字
2、顺序是一一对应的
3、带默认值的参数要放到最后
"""
# def operation(a,b,c,d,e):
#     sum1 = a + b + c + d + e
#     return sum1
# op = operation(1,2,3,4,5)
# print(op)
"""
不定长参数：
1、可以接收多个没人接收的参数
2、不能接收关键字参数
3、以元组的形式接收
"""
#不定长参数(参数收集)

# def operation(*args):
#     sum1 = 0
#     for var in args:
#         sum1 += var
#     return sum1
# op = operation(1,2,3,4,5,6,7,8,9)
# print(op)

# 当var = 1   sum1 = sum1 + var
#                     0      1   sum1 = 1
# 当var = 2   sum1 = sum1 + var
#                     1      2   sum1 = 3
# 当var = 3   sum1 = sum1 + var
#                     3      3   sum1 = 6
#。。。。。。。。
# 当var = 9   sum1 = sum1 + var
#                     36     9    sum1 = 45

# *args   垃圾回收站  不能接收关键字参数
# def operation(a,b,c,d,*args):
#     print(a)
#     print(b)
#     print(c)
#     print(d)
#     print(args)
# operation(1,2,3,4,5,6,7,8,9)

"""
不定长关键字参数:
可以接受关键字参数，以字典的形式接收
注意：三种参数尽量避免一起使用
"""
# 接收不定长关键字参数
# def operation(**kwargs):
#     print(kwargs)
# operation(a=1,b=2,c=3)

#传递参数顺序:普通参数，不定长参数，不定长关键字参数
# def operation(A,B,C,D,*args,**kwargs):
#     print(A,B,C,D)
#     print(args)
#     print(kwargs)
# operation(1,2,3,4,5,6,7,a=1,b=2,c=3)

# list1 = ["1","2","3","4","5"]
# for i in list1:
#     for j in list1:
#         for k in list1:
#             if i != j and i != k and j != k:
#                 print(i+j+k)
```

### 函数嵌套和闭包

```python
# 闭包：内部函数使用外部函数的局部变量，那么我们就称内部函数为闭包
# 闭包就是调用一个函数，它返回了另一个函数给你  那么返回的这个函数就叫做闭包

# def outer(num):
#     def inner(val):
#         return num + val
#     return inner
#
# res = outer(10)  #outer(10) ===> inner   res = inner
# result = res(10)   #res(10) == inner(10)
# print(result)


# def foo():
#     m = 1
#     def foo1():
#         m = 2
#         print(m)
#     print(m)
#     foo1()
#     print(m)
# foo()

# 闭包引用外部函数的局部变量的前提是：内部没有这个变量
# def outer():
#     a = [1]
#     def inner():
#         a[0] = a[0] + 1
#         return a[0]
#     return inner
# res = outer()()  # outer() == inner    outer()() == inner()
# print(res)
```

















