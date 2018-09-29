"""
format格式化
"""
# 顺序传参
a = "hello,my name is {},my age is {}".format("miss", 18)
print(a)

# 按照索引值来传参
a = "hello,my name is {1},my age is {0}".format(18, "miss")
print(a)

# 按照索引来传参
info = ["miss", 18]
a = "hello,my name is {0[0]},my age is {0[1]}".format(info)
print(a)

# 按照关键字来传参
a = "hello,my name is {name},my age is {age}".format(name="miss", age=18)
print(a)

"""
字符串填充
"{:[填充字符][对齐方式][填充位数]}".format(string)

居中 ^
左对齐 <
右对齐 >
"""
str1 = 'miss'
str2 = "{:_<10}".format(str1)
print(str2)

"""
调整精度
"{:.[精度位数]f}".format(string)
"""

"""
进制转换
"{:[b,o,d,x]}".format(string)
"""

"""
逗号，金额千位分隔符
"{:,}".format(string)
"""
