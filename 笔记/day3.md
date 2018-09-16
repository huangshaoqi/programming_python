## 基本数据类型

### 字符串转换

- 所有类型都可以进行转换

```python
# val = 1
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

# val = 1.6
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

# val = 1+1j
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

# val = False
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

# val = [1,2,3]
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

# val = (1,2,3)
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

# val = {1,2,3}
# print(val,type(val))
# val1 = str(val)
# print(val1,type(val1))

val = {"a":1,"b":2,"c":3}
print(val,type(val))
val1 = str(val)
print(val1,type(val1))
```

### 元组转换

- 数字类型都不能进行转换
- 容器类型可以转换，但是注意字典只有键能转换

```python
# val = 12345
# print(val,type(val))
# val1 = tuple(val)
# print(val1,type(val1))

# val = 1.2345
# print(val,type(val))
# val1 = tuple(val)
# print(val1,type(val1))

# val = 1+2j
# print(val,type(val))
# val1 = tuple(val)
# print(val1,type(val1))

# val = "I love Python"
# print(val,type(val))
# val1 = tuple(val)
# print(val1,type(val1))

# val = {1,2,3,4,3}
# print(val,type(val))
# val1 = tuple(val)
# print(val1,type(val1))

val = {"a":1,"b":2,3:"c"}
print(val,type(val))
val1 = tuple(val)
print(val1,type(val1))
```

### 集合的转换

- 数字类型都不能进行转换

- 容器类型可以转换，但是注意字典只有键能转换

  

```python
# val = "静如瘫痪，动若癫痫~"
# print(val,type(val))
# val1 = set(val)
# print(val1,type(val1))


# val = [1,2,3]
# print(val,type(val))
# val1 = set(val)
# print(val1,type(val1))

# val = (1,2,3)
# print(val,type(val))
# val1 = set(val)
# print(val1,type(val1))

val = {"a":1,"b":2,3:"c"}
print(val,type(val))
val1 = set(val)
print(val1,type(val1))
```

### 字典类型转换

- 数字类型都不能进行转换
- 其它数据类型要按照指定格式才能进行转换

```python
# val = "静如瘫痪，动若癫痫~"
# print(val,type(val))
# val1 = set(val)
# print(val1,type(val1))


# val = [1,2,3]
# print(val,type(val))
# val1 = set(val)
# print(val1,type(val1))

# val = (1,2,3)
# print(val,type(val))
# val1 = set(val)
# print(val1,type(val1))

val = {"a":1,"b":2,3:"c"}
print(val,type(val))
val1 = set(val)
print(val1,type(val1))
```

## 运算

### 算数运算

```python
"""
加运算      +
减运算      -
乘运算      *
除运算      /  2/5
取余运算    %
取整（商）运算    //
幂运算      **
"""
# num1 = 5
# num2 = 6
# result = num1 + num2
# result = num2 - num1
# result = num1 * num2
# result = num1 / num2  #结果转换成浮点数
# result = num1 % num2
# result = num1 // num2
# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(result)

result = 2 ** 10
print(result)
```

### 关系比较运算

```python
"""
大于        >
小于        <
等于       ==
不等于     !=
小于等于   <=
大于等于   >=
"""

num1 = 5
num2 = 5
# result = (num1 > num2)
# result = num1 < num2
result = (num1 == num2)
# result = num1 != num2
# result = num1 >= num2
# result = num1 <= num2
print(result)
```

### 赋值运算

```python
=     普通赋值运算
+=    加法赋值运算
-=    减法赋值运算
*=    乘法赋值运算
/=    除法赋值运算
%=    取余赋值运算
//=   取商赋值运算
**=   幂赋值运算

val = 12
val += 10 #val = val + 10
print(val)

val = 12
val -= 10 #val = val - 10
print(val)

val = 12
val *= 9 #val = val * 9
print(val)

val = 12
val /= 9 #val = val / 9
print(val)

val = 12
val %= 9 #val = val % 9
print(val)

val = 12
val **= 3 #val = val ** 3
print(val)

val = 12
val //= 5 #val = val // 5
print(val)
```

### 逻辑运算

```python
"""
逻辑与运算     and
逻辑或运算     or
逻辑非运算     not
逻辑异或运算   xor
"""

num2 = True
num1 = True
#逻辑与运算 有假则假
# result = num1 and num2
# print(result)

#逻辑或运算 有真则真
# result = num1 or num2
# print(result)

#逻辑非运算 真变假  假变真
# result = not num2
# print(result)

#逻辑异或运算
"""
Ture   Ture   假
True   False  真
False  True   真
False  False  假
"""
```

### 成员运算

------

**检测一个数据是否在指定的容器(复合数据)当中**

```python
检测数据1是否在数据2中
    格式：数据1 in 数据2

检测数据1是否不在数据2中
    格式：数据1 not in 数据2
```

### 身份检测

------

**检测两个变量在内存中是否是同一个值**

```python
检测两个变量在内存中是不是同一个值
    格式：数据1 is 数据2

检测两个变量在内存中是否不是同一个值
    格式：数据1 is not 数据2
```

### 运算优先级的问题

------

**运算的优先级**

```python
例如：在数学中，1+5x2，乘法会优先运算。
我们的Python程序也是一样的，一个运算中存在多个运算符时，系统也有它自己的一套优先级的规则。
Python的运算优先级规则如下，从上向下按照优先级的由高向低依次排序
但是我们并不推荐各位死记硬背，因为我们自己写程序遇到优先级问题可以使用()解决，更方便，也更易读。

**                         指数(最高优先级)
~ + -                      按位翻转， 一元加号和减号(最后两个的方法名为 +@ 和 -@)
* / % //                   乘，除，取模和取整除
+ -                        加法减法
>> <<                      右移，左移运算符
&                          位 'AND'
^ |                        位运算符
<= < > >=                  比较运算符
<> == !=                   等于运算符
= %= /= //= -= += *= **=   赋值运算符
is is not                  身份运算符
in not in                  成员运算符
not or and                 逻辑运算符
```

### 按位运算符

**按位运算符是把数字看作二进制来进行计算的。Python中的按位运算法则如下：**

**下表中变量 a 为 60，b 为 13。**

| **运算符** | **描述**                                                     | **实例**                                                     |
| ---------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **&**      | **按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0** | **(a & b) 输出结果 12 ，二进制解释： 0000 1100**             |
| **\|**     | **按位或运算符：只要对应的两个二进位有一个为1时，结果位就为1。** | **(a \| b) 输出结果 61 ，二进制解释： 0011 1101**            |
| **^**      | **按位异或运算符：当两个对应的二进位相异时，结果为1**        | **(a ^ b) 输出结果 49 ，二进制解释： 0011 0001**             |
| **~**      | **按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1** | **(~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。** |
| **<<**     | **左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。** | **a << 2 输出结果 240 ，二进制解释： 1111 0000**             |
| **>>**     | **右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数** |                                                              |











