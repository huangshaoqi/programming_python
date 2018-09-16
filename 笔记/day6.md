## 高阶函数

### map()函数

```python
map(func,lsd)
func:可以是一个python内置函数，也可以是我们的自己定义的函数
lsd:必须是一个序列，也可以说是一个容器
功能: lsd这个容器里边的数据，会依次作用在前边的func上
```

```python
# str1 = ["1","3","5","8","2","4"]
# print(str1)
# # print(int(str1))
# map1 = map(int,str1)
# # int("1")  int("3") int("5")  int("8")   int("2")  int("4")
# #map是一个惰性序列
# print(list(map1))

def func(value):
    dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,}
    return dict[value]
res = func("1")
print(res,type(res))
map1 = map(func,str1)
#把str1里边的所有元素依次赋值给前边的func函数
print(list(map1))

例2：
list1 = [1,4,2,6,3,4,7,9]
dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,}
dict1 = {}
for key,value in dict.items():
    dict1[value] = key
# print(dict1)

def func(key1):
    dict = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,}
    dict1 = {}
    for key, value in dict.items():
        dict1[value] = key
    return dict1[key1]

map1 = map(func,list1)
print(list1)
print(list(map1))
```

### reduce()函数

```python
reduce(fn,lsd)
fn:一个函数  但是这个函数必须有两个参数
lsd:是一个序列  也可以说是一个容器
功能: 把容器里边的前两个元素作用在fn上，
    然后得出的结果再和容器里边的第三位数作用在fn上，
    一直到容器里边的所有元素全部计算完毕
lsd = [1,2,3,4,5,6]
fn(fn(fn(fn(fn(1,2),3),4),5),6)
```

```python
# lsd = {1,3,6,4,5,8,7,2}
# lsd = ["2","4","5","7"]

# lsd1 = map(int,lsd)
# def func(a,b):
#     return a*10 + b
# res = reduce(func,lsd)
# print(res,type(res))

# func(1,3) ===> 13
# func(func(1,3),6) == func(13,6) == 136
# func(func(func(1,3),6),4) == func(func(13,6),4) = func(136,4) = 1364

# 1、[5,3,7,2,1,6]  转换成 "537216"

lsd1 = [5,3,7,2,1,6]

# print(dict1)

# def func(key1):
#     dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
#     dict1 = {}
#     for key, value in dict.items():
#         dict1[value] = key
#     return dict1[key1]
# res = map(func,lsd1)
# a = list(res)
# def func1(str1,str2):
#     return str1+str2
# b = reduce(func1,a)
# print(b,type(b))
```

### sorted函数

```python
sorted(lsd)
用来排序的函数,参数必须是一个序列
```

```python
#默认按照升序排列
# L = [4,2,5,3,6,1]
# print(L)
# L1 = sorted(L)
# print(L1)

#通过设置参数进行降序排列
# L = [4,2,5,3,6,1]
# print(L)
# L1 = sorted(L,reverse = True)
# print(L1)

#负数的排列
# L = [1,-5,9,-23,0,33]
# print(L)
# L1 = sorted(L)
# print(L1)

#通过绝对值来排列
# L = [1,-5,9,-23,0,33]
# print(L)
# L1 = sorted(L,key=abs)
# print(L1)

#字符串的排序
# L = ["acccc","dlksajf","fjks","ioej","中","daaa"]
# print(L)
# L1 = sorted(L,key=len)
# print(L1)
```

### filter()函数

```python
filter(fn,lsd)
fn：判断后面序列作用在前面函数的时候返回的bool值，如果True，返回这个数值，如果为False，过滤掉这个数值
lst:一个序列
功能:过滤
```

```python
lsd = [1,2,3,4,5,6,7,8,9]

def func(key):
    if key % 2 == 0:
        return True
    else:
        return False
#filter 同样是一个惰性序列
res = filter(func,lsd)
print(list(res))
```

### lambda匿名函数

> lambda表达式是一种简洁格式的函数。该表达式不是正常的函数结构，而是属于表达式的类型。 **基本格式：**

```
lambda 参数,参数...：函数功能代码
如：lambda x,y:x + y    获取2个值的和的lambda函数
```

**带分支格式:**

```
lambda 参数,参数... :值1  if 条件表达式  else 值2
如：lambda sex : '有胡子' if sex == 'man' else '没胡子'
```

**调用函数格式：**

```
lambda 参数,参数...:其他函数(...)
如：lambda x:type(x)
```

**lambda表达式的优缺点:**

```
优点：
    书写简单不需要def关键字
    不需要费脑子想函数名(匿名函数)看起来高大上！

缺点：
    lambda表达式功能受限，无法使用循环和多项分支
    复杂的操作，不适合lambda表达式
```

**示例**

```python
#方式1.声明一个简单的lambda表达式
mylamb = lambda x,y:x+y
#调用函数
result = mylamb(4,5)
print(result)

#方式2.声明一个带有分支的lambda表达式
mylamb= lambda sex : '有胡子' if sex == 'man' else '没胡子'
#调用函数
result = mylamb('woman')
print(result)

#方式3.声明一个调用函数的lambda表达式
mylamb = lambda x:type(x)
#调用函数
result = mylamb('拾元')
print(result)
```

###小试牛刀

```
需求：
    有列表["1","4","7","3","2","6","5","8","9"]
    1、求出这个列表由所有偶数组成的最大整数
    2、求出这个列表由所有奇数组成的最小奇数
```

```python
lsd = ["1","4","7","3","2","6","5","8","9"]

#把字符串变成整型
dict1 = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,}
str1 = lambda str0:dict1[str0]
i = list(map(str1,lsd))
print(i)
#过滤掉所有奇数
j = lambda i:i if i % 2 == 0 else 0
j1 = list(filter(j,i))
print(j1)
#降序排序
j1 = sorted(j1,reverse = True)
print(j1)
#将数据进行整合
a1 = lambda a,b:a*10+b
s = reduce(a1,j1)
print(s,type(s))
```

