## time模块

**1、time.tme() 时间戳**

```python
res = time.time()
print(res)
```

**2、time.localtime()  参数可以加一个秒数**

```python
res = time.localtime(120)
print(res)
```

**3、time.gmtime()**

```python
res = time.gmtime(120)
print(res) 
```

**4、mktime()  结构化时间转换为时间戳**

```python
res = time.gmtime()
print(res)
var = time.mktime(res)
print(var)
```

**5、time.ctime()**

```python
res = time.ctime(120)
print(res)
```

**6、time.strftime()**

```python
res = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print(res)
```

**7、time.strptime()**

```python
var = time.strptime(res,"%Y-%m-%d %X")
print(var)
```

**8、time.sleep()**

```python
print(res)
time.sleep(3)
print(res)
```

**9、time.clock()**

```python
# res = time.clock()
# print(res)
```

### 时间元组struct_time

```python
时间元组就是一个用于表示时间格式的元组数据而已，他是time模块操作时间的主要方式。
(tm_year=2017, tm_mon=7, tm_mday=4, tm_hour=9, tm_min=4, tm_sec=21, tm_wday=1, tm_yday=185, tm_isdst=0)
格式:（年，月，日，时，分，秒，周几，一年中的第几天，是否是夏令时）
索引        名称          内容           取值
 0        tm_year        年           4位数年份   2017
 1        tm_month       月           1～12
 2        tm_day         日           1～31
 3        tm_hour        时           0～23 
 4        tm_min         分           0～59 
 5        tm_sec         秒           0～61  60闰秒，61是历史保留
 6        tm_wday        周几          0～6  周一～周天
 7        tm_yday        一年中的第几天  1～366
 8        tm_isdst       夏令时         0 是  其他不是
```

### strftime()

```python
功能：格式化输出时间字符串（str foramt time）
格式：time.strftime('字符串格式'[,时间元组])
返回值：格式化之后的哦字符串
格式    含义        备注
%a    本地（locale）简化星期名称
%A    本地完整星期名称
%b    本地简化月份名称
%B    本地完整月份名称
%c    本地相应的日期和时间表示
%d    一个月中的第几天（01 - 31）
%H    一天中的第几个小时（24 小时制，00 - 23）
%I    一天中的第几个小时（12 小时制，01 - 12）
%j    一年中的第几天（001 - 366）
%m    月份（01 - 12）
%M    分钟数（00 - 59）
%p    本地 am 或者 pm 的相应符    注1
%S    秒（01 - 61）    注2
%U    一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周    注3
%w    一个星期中的第几天（0 - 6，0 是星期天）    注3
%W    和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始
%X    本地相应时间
%y    去掉世纪的年份（00 - 99）
%Y    完整的年份
%z    用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）
%%    %号本身
```

## 异常处理

```python
"""
try：
    可能发生错误的语句
except 异常类型:
    如果try语句发生错误，那么执行此处语句
"""
```

```python
try:
    print(1/0)
# 捕获异常
except ZeroDivisionError:
    # 如果捕获到了异常，那么就执行下边的语句
    print("除数不能为0！")

print("hello")

try:
    L = [1,2,3,4]
    print(L[6])
except IndexError:
    print("超出索引范围！")

Name = "jack"
try:
    print(name)
except NameError:
    print("变量不存在！")

try:
    main()
except BaseException:
    pass

try:
    print(1/0)
except:
	print("除数不能为零!")
```

```python
"""
try:
    有可能发生错误的语句
except 异常信息:
    异常之后要执行的代码
else:
    没有发生异常的时候执行下边的语句
"""
```

```python
try:
    print(1/1)
except BaseException:
    print("除数不能为0！")
else:
    print("hello")
```

```python
"""
try:
    有可能发生错误的语句
except 异常信息:
    异常之后要执行的代码
else:
    没有发生异常的时候执行下边的语句
finally:
    不管是否有异常，都会执行这里的语句
"""
```

```python
try:
    print(1/1)
except BaseException:
    print("除数不能为0！")
finally:
    print("无论如何都会执行我!")
```

### 异常处理的特殊情况

- **python中的错误其实就是class，所有的错误都继承baseexception,所以我们在捕获的时候，它捕获了该类型的错误，并且它还把子类一网打尽**

  - ```python
    try:
        print(1/0)
    except BaseException as e:
        print("异常1")
    except ZeroDivisionError as e:
        print("异常2")
    ```

- **有些错误无法捕获**

  **比如说内存错误，如果我们想开辟一块新的内存空间，那就必须先释放一部分内存**

  

- **跨越多层调用**:

  - ```python
    def func1(num):
        print(1/num)
    def func2(num):
        func1(num)
    def main():
        func2(0)
    try:
        main()
    except ZeroDivisionError as e:
        print("*****")
    #Main调用了func2,func2调用了func1,但是出现错误的是func1，这个时候只要main捕获到了就可以处理
    ```

## pickle模块

```python
"""
1、便于储存  不在存储在内存
2、便于传输  网络传输需要把数据转换为字节流
"""
```

**dumps**

```python
# 数据序列化
res = pickle.dumps(L)
print(res,type(res))
```

**loads**

```python
# 数据反序列化
var = pickle.loads(res)
print(var,type(var))
```

**dump**

```python
with open("user.txt","wb") as f:
    pickle.dump(L,f)
```

**load**

```python
with open("user.txt","rb") as f:
    content = pickle.load(f)
    print(content)
```







