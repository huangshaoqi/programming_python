# class Person:
# 	def __init__(self,name,age,sex):
# 		self.name = name
# 		self.age = age
# 		self.sex = sex

# 	def print_info(self):
# 		return self.name,self.age,self.sex

# p = Person("小花", 18, "男")

# print(p.print_info())

# from functools import partial

# def myfunc(x,y):
# 	return x + y

# par1 = partial(myfunc, 10)

# print(par1(20))

import sys

print(sys.api_version)
print(sys.getdefaultencoding())
print(sys.getfilesystemencoding())

def func(*args,**kwargs):
	return args
	
l = [1,2,3,4,5]
list1 = (6,7,8,9,10)
res = func(*l)
print(res)

print(func(*list1))