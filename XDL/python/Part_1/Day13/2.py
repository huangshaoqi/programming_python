lsd = ["1","2","5","6","3","4","7","9","8"]


# 筛选偶数
# 筛选奇数

# int_lsd = list(map(int,lsd))
#
# res1 = filter(lambda x:True if x %2 ==0 else False,int_lsd)
#
# res2 = filter(lambda x:True if x %2 ==1 else False,int_lsd)

from functools import reduce

res = reduce(lambda x,y:x*10+y,sorted(filter(lambda x:True if x % 2 ==0 else False,map(int,lsd)),reverse=True))
res1 = reduce(lambda x,y:x*10+y,sorted(filter(lambda x:True if x % 2 ==1 else False,map(int,lsd))))
print(res,res1)