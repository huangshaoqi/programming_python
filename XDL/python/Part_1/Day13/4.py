li = [1, 2, 3, 4, 5, 6, 7, 8, 8]
li2 = []
li3 = []
for i in li:
    for x in li:
        if i != x:
            a = "%d%d" % (i, x)
            li2.append(a)
print(li2)
for y in li2:
    if y not in li3:
        li3.append(y)
print(li3)
print(len(li3))
