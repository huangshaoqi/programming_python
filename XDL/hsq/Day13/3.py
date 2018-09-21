li = [1, 2, 3, 4, 5, 6, 7, 8, 8]
list1 = list(map(str, set(li)))
list2 = []

for i in range(len(list1)):
    for a in list(list1[i]):
        for b in list(list1[i + 1:]):
            list2.append(int(a + b))
            list2.append(int(b + a))

print(len(set(list2)))


def num(n):
    print(n)
    if n > 1:
        num(n - 1)
    print(n)

# num(4)
