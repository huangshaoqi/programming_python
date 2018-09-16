## 基本数据类型

### 列表

列表就是一系列元素的顺序组合，标识符是[ ]，里边的每个元素要用逗号区分，列表里的元素可以随时修改。

```python
#         0   1   2   3  正向序号  (索引-->index)
list1 = ["a","b","c","d"]
#        -4  -3  -2  -1  反向序号  (索引-->index)
print(list1)
print(type(list1))

print(list1[0],list1[-4])
print(list1[3],list1[-1])
list1[2] = "e"
print(list1)

list2 = ["a","b",1,2,["c",3]]
print(list2,type(list2))

#         0   1       2
list3 = ["a","b",[1,2,["c","d"]]]
# print(list3,type(list3))
# list4 = list3[2]
# print(list4,type(list4))
# list5 = list4[2]
# print(list5,type(list5))
# list5[1] = "f"
list3[2][2][1] = "f"
print(list3)
```

### 元组

元组是一系列元素的顺序组合，标识符是逗号，初始化之后元组内的元素不能再做修改

```python
#          0   1   2   3  (正向序号)
tuple1 = ("a","b","c","d")
# #         -4  -3  -2  -1  (反向序号)
tuple2 = ("c","d")
print(tuple1,type(tuple1))
print(tuple2,type(tuple2))

print(tuple1[0],tuple1[-1])

#组合后的元组不能进行修改
# tuple1[3] = "f"
# print(tuple1)

tuple3 = ("a",1,("c","2"))
print(tuple3,type(tuple3))
tuple4 = tuple3[2][1]
print(tuple4)

tuple5 = ("a","b",[1,2])
print(tuple5,id(tuple5))
tuple5[2][0] = "c"
print(tuple5,id(tuple5))

tuple1 = ()
print(tuple1,type(tuple1))
tuple2 = (1,)
print(tuple2,type(tuple2))
tuple3 = (1,2)
print(tuple3,type(tuple3))
```

### 集合

一组特定数据的无序组合 ，所有的元素不能重复，标识符：无

```python
set1 = {1,2,3,"a","b",3,1}
print(set1,type(set1))

# set2 = {1,2,{3,4,"a"}}
# print(set2)

# set2 = {}
# print(set2,type(set2))

set2 = set()
print(set2,type(set2))

#补集  交集  差集  并集
```

### 字典

字典就是具有键值映射关系的一组无序数据组合，可以修改 字典的标志符号：{} 字典格式 

```python
#冒号左边为字典的键   冒号右边为键对应的值
# dict1 = {"及时雨":"宋江","花和尚":"鲁智深","九纹龙":"史进","小李广":"花荣"}
# print(dict1,type(dict1))

# print(dict1["豹子头"])

# dict2 = {"a":1,"b":2,"c":3}
# print(dict2)

# dict1["九纹龙"] = "屎尽"
# print(dict1)

dict1 = {"韩寒":"三重门","四大名著":{"吴承恩":"西游记","曹雪芹":"红楼梦","施耐庵":"水浒传","罗贯中":"三国演义"}}

print(dict1["韩寒"])
# dict2 = dict1["四大名著"]
# print(dict2["曹雪芹"])
print(dict1["四大名著"]["曹雪芹"])

dic	={'k1':"v1","k2":"v2","k3":[11,22,33]}
dic["k1"] = "alex"
print(dic)

dic["k4"] = "v4"
print(dic)

print(dic["k5"])

"""
容器类数据类型：
string 字符串    有序容器
list  列表       有序容器
tuple 元组       有序容器
set   集合       无序容器
dict  字典       无序容器
"""
```



### 小试牛刀



>1、li=["hello",'seven',["mon",["h","kelly"],'all'],123,446]
>
>​	a. 请输出 “all”
>		b. 请输出“kelly”
>		c. 请输出123
>
>2、tu=("alex",[11,22,{"k1":'v1',"k2":["age","name"],"k3":(11,22,33)},44])
>
>​	a.tu变量中的第一个元素"alex"是否可以被修改，如果可以请修改为"ALEX"
>
>3、dict={'k1':"v1","k2":"v2","k3":[11,22,33]}
>
>​	a.请在修改字典中 “k1” 对应的值为 “alex”，输出修改后的字典



## 数据类型转换

### 自动转换

自动转换是说不需要人工干预，程序会自动转换。

- 程序会朝着更精确的方向进行转换
- 一般是在运算或者进行判断的时候进行转换

### 手动转换

手动转换是说随着我们开发者的意志进行转换

#### int 整数型转换

- int               不用转换
- float            转换之后去掉小数点
- complext   不能进行转换
- bool            True变成1  False变成0
- str                只有由整数组成的字符串才能进行转换
- 列表、元祖、集合、字典都不能进行转换

```python
# val = 1
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = 1.6
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = 1+1j
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = False
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = "-1"
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = [1]
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = (1,)
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

# val = {1}
# print(val,type(val))
#
# val1 = int(val)
# print(val1,type(val1))

val = {"a":1}
print(val,type(val))

val1 = int(val)
print(val1,type(val1))
```

#### float类型转换

- float不需要转换
- int可以转换  转换之后在末尾添加`.0`
- complex  不可以转换
- bool      转换之后  True变成1.0   False变成0.0
- str         只能由整数或者浮点数组成的字符串可以转换
- 列表、元组、集合、字典都不能进行转换

```python
# val = 5
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))

# val = 5+0j
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))

# val = False
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))

# val = "1.23"
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))

# val = [1,2]
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))

# val = (1,)
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))

# val = {2,3,4}
# print(val,type(val))
# val1 = float(val)
# print(val1,type(val1))
#
val = {"a":1}
print(val,type(val))
val1 = float(val)
print(val1,type(val1))
```

#### complex转换

- int  转换之后  在整数后边加`0j`
- float 转换之后在浮点数后边加`0j`
- str     只有由整数和浮点数组成的字符串能进行转换
- bool   True变成`1+0j`  False变成`0j`

```python
# val = 6
# print(val,type(val))
# val1 = complex(val)
# print(val1,type(val1))

# val = 6.6
# print(val,type(val))
# val1 = complex(val)
# print(val1,type(val1))

# val = "1.2"
# print(val,type(val))
# val1 = complex(val)
# print(val1,type(val1))


# val = True
# print(val, type(val))
# val1 = complex(val)
# print(val1, type(val1))

# val = False
# print(val,type(val))
# val1 = complex(val)
# print(val1,type(val1))
```

#### bool值的转换

- int    只有 0 变成False
- float   只有0.0变成False
- complex  只有 `0j` 变成False
- str      空字符串 `""` 变成False
- list      空列表`[]`变成False
- tuple  空元组`()`变成False
- set      空元组`set()`变成False
- dict     空字典`{}`变成False

```python
# val = 3j
# print(val,type(val))
# val1 = bool(val)
# print(val1,type(val1))

# val = ""
# print(val,type(val))
# val1 = bool(val)
# print(val1,type(val1))

# val = [ ]
# print(val,type(val))
# val1 = bool(val)
# print(val1,type(val1))

# val = (1,)
# print(val,type(val))
# val1 = bool(val)
# print(val1,type(val1))

val = set()
print(val,type(val))
val1 = bool(val)
print(val1,type(val1))
```

#### 列表的转换

- int  不可以转换
- float 不可以转换
- complex 不可以转换
- bool   不可以转换
- str     把每个字当作一个元素添加到列表当中
- tuple   直接把元组内的元素放到列表当中
- set    直接把集合里边的元素放到列表当中
- dict   只把字典的键取出来放到列表当中

```python
# val = 1
# print(val,type(val))
# val1 = list(val)
# print(val1,type(val1))

# val = 1.6
# print(val,type(val))
# val1 = list(val)
# print(val1,type(val1))

# val = True
# print(val,type(val))
# val1 = list(val)
# print(val1,type(val1))

# val = "大金链子小手表，一天三顿小烧烤，青春献给小酒桌，怎么澎湃怎么喝~~~"
# print(val,type(val))
# val1 = list(val)
# print(val1,type(val1))

# val = (1,2)
# print(val,type(val))
# val1 = list(val)
# print(val1,type(val1))


# val = {1,2,3,4}
# print(val,type(val))
# val1 = list(val)
# print(val1,type(val1))

val = {"a":1,"b":2,"c":3}
print(val,type(val))
val1 = list(val)
print(val1,type(val1))
```





