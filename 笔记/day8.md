## 列表的操作

**列表相加操作**

```
格式：变量 = 列表1 + 列表2
结果：新的列表
注意：+两侧都要是列表类型
```

```python
# L = [1,2,3]
# L1 = [4,5,6]
# print(L+L1)

```

**列表相乘操作**

```python
格式：变量 = 列表 * 整数
结果：新的列表

```

```python
# L = [1,2,3]
# print(L*2)
```

**索引操作**

```
变量[索引]
```

**分片操作**

```python
格式：变量 = 列表[:]
    获取整个列表

格式：变量 = 列表[:结束索引]
    获取列表开头到结束索引之前的数据组成的列表

格式：变量 = 列表[开始索引:]
    获取列表开始索引到列表末尾的数据组成的列表

格式：变量 = 列表[开始索引:结束索引]
    获取开始索引和结束索引之间的数据组成的列表（包含开始索引，不包含结束索引）

格式：变量 = 列表[开始索引:结束索引:间隔值]
    获取开始索引和结束索引之间的数据（按照间隔值来获取）组成的列表（包含开始索引，不包含结束索引）
```

```python
# L = [1,2,3,4,5,6,7,8,9]
# L1 = L[6:3:-1]
# print(L1)
```

**成员检测**

```
检测一个数据是否在列表中
    格式：值 in 列表
    结果：布尔值

检测一个数据是否不在列表中
    格式：值 not in 列表
    结果：布尔值
```

### 列表的遍历操作

------

**for...in**

```
for 变量 in 列表：
    使用变量
```

```python
# L = [1,2,3,4,5]
# for val in L:
#     print(val)
```

**while**

```
i = 0
while i<len(列表):
    使用列表中的元素(列表[i])
    i += 1
```

```python
# L = [1,2,3,4,5,6,7]
# i = 0
# while i<len(L):
#     print(L[i])
#     i += 1
```

**遍历同等长度的二级列表**

```
列表 = [[值1,值2],[值1,值2],....]
for 变量1,变量2 in 列表:
    使用变量1和变量2
#注意：变量1取二级列表中的第一个值，变量2取第二个值
```

```python
# L = [[1,2],[3,4],[5,6]]
# for val,var in L:
#     print(val,var)
```

**遍历非同等长度的二级列表**

```
列表 = [[值1，值2]，[值1，值2,值3],[值]...]
for 变量1 in 列表:
    for 变量2 in 变量1:
        使用变量2(变量2是二级列表中的每个值)
```

```python
# L = [[1,2],[3,4],[5,6,7]]
# for val in L:
#     print(val,type(val))
#     for var in val:
#         print(var,type(var))
```

### 列表的十一种操作方法

**append()**

```
功能：向列表的末尾添加新的元素
格式：列表.append(值)
返回值：None
注意：新添加的值在列表的末尾，该函数直接操作原有列表
```

```python
# L.append(8)
# L.append(7)
# print(L)
```

**insert()**

```
功能：在指定位置之前插入元素
格式：列表.insert(索引,值)
返回值:None
注意：直接改变原有列表
```

```python
# L.insert(0,1)
# print(L)
```

**extend()**

```
功能：将一个列列表继承另一个列表
格式：列表.extend(序列)
返回值：None
注意：直接改变原有列表
```

```python
# L.append(L1)
# print(L)
# L.extend(L1)
# print(L)
```

**pop()**

```
功能：在列表中移除一个元素
格式：列表.pop([索引])
返回值：删除的元素
注意：没有指定索引，默认移除最后一个元素
```

```python
# L.pop()
# L.pop(0) #可以传递索引值  来删除指定的元素
# print(L)
```

**remove()**

```
功能：移除指定的值
格式：列表.remove(值)
返回值：无
注意：如果有索引的清空下推荐使用POP移除，效率比remove高
```

```python
# L.remove([7,8,9])
# L.remove(8) #如果有多个相同的元素  默认删除第一个
# print(L)
```

**index()**

```
功能：获取某个值在列表中的索引
格式：列表.index(值)
返回值：整数
注意：值不存在与列表时抛出异常错误！
```

```python
# print(L.index(8))
# print(L.index(7,5))
# L = [2,1,5,4,2,4,6,4,2,1,5]
# print(L.pop(L.index(5,L.index(5)+1)))
# print(L)
```

**count()**

```
功能：计算某个元素出现的次数
格式：列表.count(值)
返回值：整数
```

```python
# L = [2,1,5,4,2,4,6,4,2,1,5]
# print(L.count(2))
# print(L.count(5))
# print(L.count(6))
```

**sort()**

```
功能：列表排序

格式：列表.sort()                      按照从小到大排序（数字）
格式：列表.sort(reverse=True)          按照从大到小排序（数字）
格式：列表.sort(key=函数)               对值进行指定的函数处理之后在从小到大排序
格式：列表.sort(key=函数，reverse=True)  对值进行指定的函数处理之后在从大到小排序

返回值：None
注意：直接改变原有列表
```

```python
# L = [2,1,4,3,7,6]
# L.sort()
# print(L)
# L = [2,1,4,3,7,6]
# L1 = L.sort()
# L1 = sorted(L)
# print(L)
# print(L1)

L = [
    {"name":"jack","age":18},
    {"name":"rose","age":22},
    {"name":"tom","age":102},
    {"name":"jerry","age":19}
    ]
L.sort(key=lambda x:x["name"])
print(L)
```

**reverse()**

```
功能：列表反转操作
格式：列表.reverse()
返回值：None
```

```python
# L = [2,1,4,3,7,6]
# L.reverse()
# print(L)
```

### 列表推导式

**例1：已知`L = [1,2,3,4,5,6,7,8,9]`,求变量L内所有元素的平方组成的列表**

**for循环写法：**

```python
# L1 = []
# for val in L:
#     L1.append(val**2)
# print(L1)
```

**列表推导式**

```python
# L1 = [var**2 for var in L]
# print(L1)
```

**例2：求L中所有偶数的平方**

**for循环写法**

```python
# L1 = []
# for val in L:
#     if val % 2 == 1:
#         L1.append(val**2)
# print(L1)
```

**列表推导式**

```python
# L1 = [val**2 for val in L if val%2==1]
# print(L1)
```

**例3：`L = ["jack","ada","tom","WE","file","continue","break"]`求列表中所有元素的长度组成的列表**

```python
# L1 = [len(i) for i in L]
# print(L1)
```

**例4：已知`str="abc" str2="ABC"`  求两个字符串中的元素的所有组合**

```python
# L1 = [x+y for x in str1 for y in str2 ]
# print(L1)
```

**例5：求x,y组成的元组  x是1~5之间的偶数  y是1~6之间的奇数**

```python
# L1 = [x for x in range(1,5) if x % 2==0]
# print(tuple(L1))
# L2 = [y for y in range(1,6) if y % 2==1]
# print(tuple(L2))
#
# list1 = [(x,y) for x in range(2,6,2) for y in range(1,7,2)]
# print(list1)

# L = [(x,y) for x in range(1,5) if x%2==0 for y in range(1,7) if y%2==1]
# print(L)
```

**例6：已知 `L = [[1,2,3],[4,5,6],[7,8,9]]`求`[3,6,9]`组成的列表**

```python
# L1 = [i[2] for i in L]
# print(L1)
```

**例7：求上面列表中`[1,5,9]`组成的列表**

```python
# L1 = [L[i][i] for i in range(len(L))]
# print(L1)

# i = 0,1,2
# 当i = 0  L[i] = [1,2,3]  L[i][i] = 1
# 当i = 1  L[i] = [4,5,6]  L[i][i] = 5
# 当i = 2  L[i] = [7,8,9]  L[i][i] = 9
```

### 深浅拷贝

**赋值操作 赋值后的列表跟随元列表进行改变**

```python
# L = [2,1,4,3,[5,6]]
# L = [1,2,[3,4,[5,6]]]
# L1 = L
# L.append(5)
# L[2][2].append(7)
# print(L)
# print(L1)
```

**浅拷贝  只拷贝外层列表  内层列表跟随原列表进行改变**

```python
# L1 = copy.copy(L)
# L.append(5)
# L[2][2].append(7)
# print(L)
# print(L1)
```

**深拷贝  深拷贝拷贝整个列表   不跟随原列表进行改变**

```python
# L1 = copy.deepcopy(L)
# L.append(5)
# L[2][2].append(7)
# print(L)
# print(L1)
```

## 元组的操作

### 元组的遍历

**for ... in**

```
变量 = (值1,值2,值3...)
for 变量 in 元组:
    使用变量获取元组的每个值
```

```python
# t = (1,2,3,4)
# for val in t:
#     print(val)
```

**while**

```
i = 0
while i<len(元组):
    使用元组变量[i]访问每个值
    i += 1
```

```python
# t = (1,2,3,4)
# i = 0
# while i < len(t):
#     print(t[i])
#     i += 1
```

**遍历长度相同的多级元组**

```
元组 = ((值1,值2...),(值1,值2...)...)
for 变量1，变量2.. in 元组:
    使用变量1和变量2
```

```python
# t = ((1,2),(3,4),(5,6))
# for val,var in t:
#     print(val,var)
```

**遍历长度不同的多级元组**

```
元组 = ((值1,值2...),(值1,值2...)...)
for 变量1 in 元组:
    for 变量2 in 变量1：
        使用变量2获取每个值
```

```python
# t = ((1,2),(3,4,5),(6,7))
# for val in t:
#     for var in val:
#         print(val,var)
```

### 元组的操作方法

**index()**

```python
获取指定值在元组中的索引值
格式：元组.index(值)
返回值：整数
print(t.index(2))
```

**count()**

```python
计算某个值在元组中出现的次数
格式：元组.count(值)
返回值：整数
print(t.count(2))
```

### 元组推导式

**基本格式：**

```
格式： 变量 = (i for i in 元组)
结果：不是元组而是一个生成器
```

**带条件格式：**

```
格式： 变量 = (i for i in 元组 if 条件表达式)
结果：不是元组而是一个生成器
```

**多循环推导式：**

```
格式： 变量 = (x+y for x in 元组1 for y in 元组2)
结果：不是元组而是一个生成器   x+y可以是其他操作
```

**带条件的多循环推导式：**

```
格式： 变量 = (x+y for x in 元组1 for y in 元组2 if 条件表达式)
结果：不是元组而是一个生成器   x+y可以是其他操作
```