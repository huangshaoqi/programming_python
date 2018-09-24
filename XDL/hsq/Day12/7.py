
L = ["1", "ad3", "c2", "h2o", ["co2", "k2mno4", 1, "na2"], 34]
list1 = []

def myfunc(x):
    if isinstance(x, str):
        list1.append(x)
    if isinstance(x, list):
        for i in x:
            if isinstance(i, int):
                x.remove(i)
        for j in x:
            list1.append(j)
            
for i in L:
    myfunc(i)

def myfunc1(x):
    return "".join([i for i in x if i.isdigit()])

list2 = list(map(myfunc1, list1))
print(int("".join(list2)))
