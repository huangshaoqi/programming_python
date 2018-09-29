list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""
map(func,seq)
"""
# def myfunc(x):
# 	if x % 2 == 0:
# 		return x
# 	else:
# 		return 0

# res = list(map(myfunc,list1))
# print(res)

# for i in res:
# 	print(i)

"""
filter(func,seq)
"""
# def myfunc(x):
# 	if x % 2 == 0:
# 		return True
# 	else:
# 		return False

# res = list(filter(myfunc,list1))
# print(res)

"""
reduce(func,seq)
"""
# from functools import reduce
# def myfunc(x,y):
# 	if x % 2 == 0 and y % 2 == 0:
# 		print("我们是偶数：%s  %s" % (x,y))
# 		return x * y
# 	else:
# 		print("我们是奇数：%s  %s" % (x,y))
# 		return x + y

# res = reduce(myfunc,list1)
# print(res)


"""
sorted
"""


# res = sorted(list1)
# print(res)

"""
lambda x,y: x+y
"""

# res = lambda x,y: x+y
# for x in list1:
# 	if x % 2 ==0:
# 		for y in list1:
# 			if y % 2 ==0:
# 				print(res(x,y))
# # print(res)
