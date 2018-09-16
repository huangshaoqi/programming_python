## 流程控制

**流程：** 计算机执行代码的顺序，就是流程。

**流程控制：** 对计算机代码执行顺序的控制，就是流程控制。

**流程分类：** 流程控制一共分为三类，分别是 **顺序结构**、**分支(选择)结构**、**循环结构**。

### 顺序结构

顺序结构就是代码一种自上而下执行的结构，这是Python默认的流程。

### 分支(选择)结构

分支结构一共分为4类，分别是 **单项分支**、**双项分支**、**多项分支**、**巢状分支**

#### 单项分支

```python
"""
if 条件语句:
    语句1
    语句2
    语句3
    ...
如果条件语句成立  那么就执行语句1、语句2、语句3...如果条件语句不成立，那么就结束
"""
```

示例代码：

```python
str1 = input("请输入您的用户名:")
print(str1,type(str1))

name = input("请输入您的用户名:")
if name == "admin":
    print("欢迎回家~~~")
```

> **特征：**
>
> 1.if条件表达式结果为真，则执行if之后所控制的代码组，如果为假，则不执行后面的代码组
>
> 2.冒号:之后下一行的内容必须缩进，否则语法错误
>
> 3.if之后的代码中如果缩进不一致，则可能缩进不一致的代码不会受到if条件表达式的控制
>
> 4.冒号:后面的代码是在条件表达式结果为真的情况下执行，所以称之为真区间 或 if区间

#### 双向分支

```python
"""
双向分支
如果判断条件成立，那么执行if下面的代码，
如果条件不成立，那么执行else下面代码
"""
```

实例代码：

```python
name = input("请输入您的用户名:")
if name == "admin":
    print("欢迎回家~~~")
else:
    print("你是坏人~~~")

name = input("请输入您的用户名:")
pwd = int(input("请输入您的密码:"))

if name == "admin" and pwd == 123:
    print("登陆成功。。。")
else:
    print("用户名或者密码不正确！")
```

> **特征：**
>
> 1.双项分支有两个区间，分别是 True控制的if区间 和 False控制的else区间
>
> 2.if区间的内容在双项分支中必须缩进，否则语法错误

#### 多向分支

```python
"""
多向分支
如果if判断成功，那么执行if下面语句，
如果if判断不成功,那么开始判断elif条件语句，
判断成功，执行下面语句，判断不成功，继续判断下一个elif条件，直到有一个elif条件判断成功为止，
elif条件判断成功之后，不再向下执行后边的elif语句
如果所有elif语句都不成功，那么执行else语句
"""
```

实例代码:

```python
#需要输入一个分数
score = int(input("请输入您的分数:"))
#如果分数大于等于90分
if score >= 90:
#那么我就这样输出
    print("优秀")
#如果分数大于等于70分小于90分
elif score >= 70 and score < 90:
#那么我就这样输出
    print("良")
#如果分数大于等于60分小于70分
elif score >= 60 and score < 70:
#那么我就这样输出
    print("及格")
#所有小于60分的
else:
#我就这样输出
    print("不及格")
```

#### 小试牛刀

```python
"""
用户输入一个年份
判断生肖
2000年龙年
将年份对12取余  得8的都是龙年
"""
year = int(input("请输入一个年份:"))
#判断如果输入的年份对12取余  余数的8
if year % 12 == 8:
#那么就输出龙年
    print("辰龙")
elif year % 12 == 9:
    print("巳蛇")
elif year % 12 == 10:
    print("午马")
elif year % 12 == 11:
    print("未羊")
elif year % 12 == 0:
    print("申猴")
elif year % 12 == 1:
    print("酉鸡")
elif year % 12 == 2:
    print("戌狗")
elif year % 12 == 3:
    print("亥猪")
elif year % 12 == 4:
    print("子鼠")
elif year % 12 == 5:
    print("丑牛")
elif year % 12 == 6:
    print("寅虎")
else:
    print("卯兔")
```

彩票程序:

```python
import random

# 生成一个随机两位数  作为一个中奖号码
luck_num = random.randint(10,99)
print(luck_num)
luck_num_g = luck_num % 10
luck_num_s = luck_num // 10
# 用户输入一个购买的数字
buy_num = int(input("请输入要购买的两位幸运数字:"))
buy_num_g = buy_num % 10
buy_num_s = buy_num // 10
# 一等奖    两个数字全对  而且顺序一样
if luck_num == buy_num:
    print("一等奖,奖品《python从入门到升仙》")
# 二等奖     两个数字全对  但是顺序不一样
    # 购买的个位数字和幸运数字的十位相同 并且 购买的十位数字和幸运数字的个位相同
elif buy_num_g == luck_num_s and buy_num_s == luck_num_g:
    print("二等奖,奖品《Python从入门到放弃》")
# 三等奖     只对一个数字
    # 购买的个位数字可能和幸运数字的个位数字相同   或者
    # 购买的个位数字可能和幸运数字的十位相同      或者
    # 购买的十位数字可能和幸运数字的个位相同     或者
    # 购买的十位数字可能和幸运数字的十位相同
elif buy_num_g == luck_num_g or buy_num_g == luck_num_s or buy_num_s == luck_num_g or buy_num_s == luck_num_s:
    print("三等奖,奖品《Python从入门到住院》")
# 其它的没有奖 一个数字都不对
else:
    print("又挣你两块钱~~~")
```

# 循环结构

循环结构可以减少源程序重复书写的工作量(代码量)，用来描述重复执行某段算法的问题，这是程序设计中最能发挥计算机特长的程序结构。

Python中循环结构分为两类，分别是 **while** 和 **for .. in**

### while 循环

```python
"""
while 条件判断:
    语句

如果条件成立   程序会循环执行语句  直到条件判断失败
while循环  最主要的是要给程序一个终止的条件
"""
```

```python
 count = 0
 while count < 5:
     print("%s I love Python "%(count))
     count += 1
```
### break

```python
翻译：破坏，结束
作用：在循环中break的作用是终止当前循环结构的后续所有操作，一点程序运行了break，循环也就终止了。
```

### continue

```python
翻译：继续
作用：在循环中continue的作用是跳过本次循环，开始下一次循环。continue执行之后本次循环的后续代码不再执行，直接进入下一次循环
```

### pass

```python
翻译：忽略
作用：pass是没有任何意义的空语句，主要用来占位用，避免语法错误。
```

