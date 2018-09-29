
# def myfunc(x):
# 	list1 = {1:"a",2:"b",3:"c"}.get(x,"")
# 	return list1


# for x in range(1,100):

# 	print(myfunc(x),end="")


import random

list1 = list(range(1,101))

random.shuffle(list1)

print(list1)
