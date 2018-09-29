# 什么是变量？
# x + y = 10
# x = 5
# y = ?

# python中  一个 = 表示赋值
a = "hello world"
print(a)
print("a")

# 变量的命名方式
# 1、python3版本支持中文命名,但是python大神都不用
# 2、只能以数字、字母、下划线命名
# 3、数字不能作为开头
# 4、下划线可以作为开头，但是有特殊意义
# 5、python严格区分大小写
# 6、命名要具有描述性
# 7、不能和内部函数以及关键字发生冲突

帅 = "python"
print(帅)

# 不能有空格
# a @ 1 = "python"
# print(a @ 1)

# 不能数字开头
# 1a = "python"
# print(1a)

__a = "python"
print(__a)

name = "tom"
Name = "jerry"
print(name)
print(Name)

name = "jack"
age = 18

# id() 查看变量的内存地址
age1 = age2 = age3 = -10000
print(age1, id(age1))
print(age2, id(age2))
print(age3, id(age3))

age1 = -5.1
age2 = -5.1
age3 = -5.1
print(age1, id(age1))
print(age2, id(age2))
print(age3, id(age3))

name, age, sex = "rose", 18, "women"
print(name)
print(age)
print(sex)

# * 可以看作是一个垃圾站   接收没人要的值
a, b, *c = 1, 2, 3, 4, 5, 6
print(a)
print(b)
print(c)
