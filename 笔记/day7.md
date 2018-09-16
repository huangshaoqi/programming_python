## 字符串的操作方法

```python
+  字符串连接操作
str1 = "大金链子"
str2 = "小手表"
str3 = str1 + str2
print(str3)
*  字符串复制操作
str1 = "大金链子"
str2 = "小手表"
str3 = str1*3
print(str3)
[] 字符串索引操作，通过索引访问指定位置的字符，索引从0开始
[::] 字符串取片操作
    完整格式：[开始索引:结束索引:间隔值]
    [:结束索引]  从开头截取到结束索引之前
    [开始索引:]  从开始索引截取到字符串的最后
    [开始索引：结束索引]  从开始索引截取到结束索引之前
    [:]  截取所有字符串
    [开始索引:结束索引:间隔值]  从开始索引截取到结束索引之前按照指定的间隔截取字符
r'字符串'   元字符串，所有字符串中的转义字符不会转义，当作普通字符
str1 = "大金链子小手表，一天三顿小烧烤，青春献给小酒桌，怎么澎湃怎么喝！"

print(str1[:7])
print(str1[12:15])
print(str1[-8:])
print(str1[36:])
print(str1[::3])
print(str1[::-2])
#截取"烤烧小"
print(str1[11:14:-1])
#截取 桌小献
print(str1[-10:-15:-2])
print(str1[22:17:-2])
```

### 字符串函数

#### capitalize()

```
功能：首字母大写
格式：字符串.capitalize()
返回值：新字符串
```

```python
str2 = str1.capitalize()
str3 = str1.title()
print(str2)
print(str3)
```

#### upper()将所有小写字母变成大写   lower()将所有大写字母小写

```python
# str2 = str1.upper()
# print(str2)
# str3 = str2.lower()
# print(str3)
```

#### swapcase()大小写互换

```python
# str2 = str1.swapcase()
# print(str2)
```

#### len() 计算字符串的长度

```python
# val = len(str1)
# print(val)
```

#### count() 统计字符串中某个元素的数量

```python
# val = str1.count("a")
# print(val)
```

#### find() 查找某个字符串第一次出现的索引位置

```python
# str2 = str1.find("t",2,10)
# print(str2)
```

#### startswith() 判断是否以某个字符为开头

```python
# str2 = str1.startswith("t",4)
# print(str2)
```

#### endswith()  判断是否以某个字符结尾

```python
# str2 = str1.endswith("T")
# print(str2)
```

#### isupper() 判断字符串是否都是大写字母

```python
# str3 = "THIS Is A"
# str2 = str3.isupper()
# print(str2)
```

#### islower() 判断字符串是否都是小写字母

```python
# str3 = "this is "
# str2 = str3.islower()
# print(str2)
```

#### isalnum() 判断字符串是否是由数字、字母、汉字组成

```python
# str3 = "thisisa12"
# str2 = str3.isalnum()
# print(str2)
```

#### isalpha() 判断字符串是否由字母和文字组成

```python
# str3 = "thisisπ"
# str2 = str3.isalpha()
# print(str2)
```

#### isdigit() 判断是否是由十进制数字组成的

```python
# str2 = "15"
# str3 = str2.isdigit()
# print(str3)
```

#### isnumeric() 判断是否是数字组成的字符串

```python
# str2 = "123"
# str3 = str2.isnumeric()
# print(str3)
```

#### isdecimal() 判断是否是数值组成的字符串

```python
# str2 = "123"
# str3 = str2.isdecimal()
# print(str3)

# L = ["A","1","bc","26","89",22]
# sum1 = 0
# for val in L:
#     if val.isdigit():
#         val1 = int(val)
#         sum1 += val1
# print(sum1)
```

#### isspace() 判断字符串是否由空白符组成

```python
# str3 = "\r\n"
# str2 = str3.isspace()
# print(str2)
```

#### istitle() 判断字符串是否每个单词都首字母大写

```python
# str3 = "This Is a Test"
# str2 = str3.istitle()
# print(str2)
```

#### split() 按照指定的字符进行切分，默认按照空格

```python
# str2 = str1.split()
# print(str2)
# str3 = str1.split("T")
# print(str3)
```

#### splitlines() 按照换行来进行切分

```python
# str3 = "this is \n a \n test"
# str2 = str3.splitlines()
# print(str2)

# str3 = """this is
# a
# test"""
# str2 = str3.splitlines()
# print(str2)
```

#### join() 字符串拼接

```python
# str1 = "@"
# str2 = "this"
# str3 = str1.join(str2)
# print(str3)
# str4 = " ".join(str2)
# print(str4)
# str5 = ["this "," is","a","test"]
# str6 = str1.join(str5)
# print(str6)
```

#### zfill() 填充字符串

```python
# str1 = "this"
# str2 = str1.zfill(10)
# print(str2)
```

#### center() 填充字符串  然后字符串居中

```python
# str1 = "this"
# str2 = str1.center(10,"#")
# print(str2)
```

#### ljust() 字符串居左填充

```python
# str1 = "this"
# str2 = str1.ljust(10,"$")
# print(str2)
```

#### rjust() 字符串居右填充

```python
# str1 = "this"
# str2 = str1.rjust(10,"%")
# print(str2)
```

#### strip() 去掉指定的字符串  默认去掉换行

```python
# str1 = "this"
# print(str1)
# str2 = str1.strip("t").strip("h")
# print(str2)
```

#### rstrip() 从右边去掉某个字符

```python
# str1 = "this"
# print(str1)
# str2 = str1.rstrip("s")
# print(str2)
```

#### lstrip() 从左边去掉某个字符

```python
# str1 = "this"
# print(str1)
# str2 = str1.lstrip("t")
# print(str2)
```

#### maketrans() 和 translate()

```python
"""
maketrans()
    功能：制作用于字符串替换的映射表
    格式: 字符串.maketrans('查找字符','替换字符')    两个字符必须长度相等
    返回值：字典

translate()
    功能：进行字符串替换操作
    格式：字符串.translate(映射表)
    返回值：替换之后的字符串
"""

# str1 = "this is a test"
# str2 = str1.maketrans("t","Y")
# print(str2)
# str3 = str1.translate(str2)
# print(str3)
```

### format 格式化字符串

> **语法：** 它通过{}和:来代替%。
>
> **注意：** 字符串的format函数可以接受无限个参数，位置可以不按顺序，可以不用或者用多次，不过2.6不能为空{}，2.7才可以。

#### 顺序传参

```python
# str1 = "{} say hello to {}"
# str2 = str1.format("jack","jerry")
# print(str2)
```

#### 按照索引值进行传参 注意：大括号中传递得是Index值，不要超出索引范围

```python
# str1 = "{1} say hello to {0}"
# str2 = str1.format("jack","jerry")
# print(str2)
```

#### 按照索引来进行传参

```python
# str1 = "{0[1]} say hello to {0[0]}"
# str2 = str1.format(["jack","jerry"])
# print(str2)
```

#### 关键字来进行传参

```python
# str1 = "{name} is {age} years old!"
# str2 = str1.format(name = "tom",age = 100)
# print(str2)
```

#### 填充

```python
"""
居中 ^
左对齐 <
右对齐 >
"""
# 填充格式写在前边  要填充的字符在format参数中
# str1 = "this"
# str2 = "{:$^10}".format(str1)
# print(str2)

# str1 = "this"
# str2 = "{:$<10}".format(str1)
# print(str2)

# str1 = "this"
# str2 = "{:$>10}".format(str1)
# print(str2)
```

#### 调整精度(四舍五入)

```python
# str1 = "{:.2f}".format(1.2434)
# print(str1)
```

#### 进制转换

```python
# str1 = "{:b}".format(17)
# print(str1)
#
# str1 = "{:o}".format(17)
# print(str1)
#
# str1 = "{:d}".format(17)
# print(str1)
#
# str1 = "{:x}".format(17)
# print(str1)
```

#### **逗号,还能用来做金额的千位分隔符：** 

```python
# str1 = "{:,}".format(123456789)
# print(str1)
```

### 内建函数

### 类型相关

**int()**

```
创建或者将其他数据转化为整型
```

**float()**

```
创建或者将其他数据转化为浮点型
```

**bool()**

```
创建或者将其他数据转化为布尔型
```

**complex()**

```
创建或者将其他数据转化为复数
```

**str()**

```
创建或者将其他数据转化为字符串
```

**list()**

```
创建或者将其他数据转化为列表
```

**tuple()**

```
创建或者将其他数据转化为元组
```

**set()**

```
创建或者将其他数据转化为集合
```

**dict()**

```
创建或者将其他数据转化为字典
```

### 变量相关

**id()**

```
获取变量的id标志
```

**type()**

```
获取变量的类型字符串
```

**print()**

```
打印变量的值
```

**locals()**

```
打印当前环境中所有的变量
```

### 数学相关：

------

**abs()**

```
获取一个数值的绝对值
```

```python
user = "小明"
# def func():
#     name = "小红"
#     age = 99
#     sex = "girl"
#
#     result = locals()
#     print(result)
#
# func()

print(locals())
```

**sum()**

```
计算一个序列的数值和
```

```
# L = [1,2,3,4,5]
# sum1 = sum(L)
# print(sum1)
#
# L1 = range(1,101)
# sum2 = sum(L1)
# print(sum2)
```

**max()**

```
获取最大值
格式1：max(序列)
    返回值：序列中的最大值
格式2：max(参数1,参数2...)
    返回值：多个参数中的最大值
```

```
# L = [2,44,12,423,572,32]
# print(max(L))
# L1 = sorted(L)
# L2 = L1[-1]
# print(L2)
```

**min()**

```
获取最小值
格式1：min(序列)
    返回值：序列中的最小值
格式2：min(参数1,参数2...)
    返回值：多个参数中的最小值
```

```
# L = [2,44,12,423,572,32,0,-65]
# print(min(L))
```

**pow()**

```
获取一个数值的N次方
```

```
#前两个数先进行运算  然后再取第三个数的余数
# print(pow(2,3,3))
```

**round()**

```
对一个数值进行四舍五入操作
```

```
# num = round(3.1255,2)
# print(num)
```

**range()**

```
产生连续数据的序列
格式1：range(结束值)
    返回值:0-结束值之间的序列
格式2：range(开始值,结束值)
    返回值:开始-结束值之间的序列
格式3：range(开始值，结束值，间隔值)
    返回值:开始-结束值之间指定间隔的数据的序列
```

```
# num = range(1,11,2)
# for val in num:
#     print(val)
```

### 进制相关：

------

**hex()**

```
将十进制转化为16进制
print(hex(22))
```

**oct()**

```
将十进制转化为8进制
print(oct(22))
```

**bin()**

```
将十进制转化为2进制字符串相关:
print(bin(22))
```

**chr()**

```
将ascii编码转化为字符
print(chr(65))
```

**ord()**

```
将字符转化为ascii编码
print(ord("A"))
```

**repr()**

```
获取任意数据的原始格式字符串
```

**eval()**

```
将一个字符串当作python代码执行，字符串需要符合代码规范和repr配合
```

```python
# num = 10
# str1 = "num+1"
# print(eval(str1))

num = int(input(">>>"))
print(num,type(num))
```



































