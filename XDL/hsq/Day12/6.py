
L = ["1","ad3","c2","h2o",["co2","k2mno4",1,"na2"],34]

list1 = []
def myfunc(x):
    if type(x) == str:
        list1.append(x)
        # print(list1)
    elif type(x) == list:
            for i in x:
                if type(i) != int:
                    list1.append(i)
                    # print(list1)
    else:
        pass

for i in L:
    myfunc(i)

def myfunc1(x):
    return "".join([i for i in x if i.isdigit()])

list2 = list(map(myfunc1,list1))
print(int("".join(list2)))
