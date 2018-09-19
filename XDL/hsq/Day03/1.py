"""
if分支语句
"""

# 单项分支
a = 1
if a != 2:
    print("学习")

# 双向分支
a = 2
if a != 2:
    print("学习")
else:
    print("不学习")

# 多项分支
a = 3
if a == 1:
    print("学习")
elif a == 2:
    print("不学习")
else:
    print("要学习么")

# 巢项分支
name = input("请输入你的名字：")
age = input("请输入你的年龄：")
if name == "王八蛋":
    if int(age) >= 40:
        print("你老了！")
    else:
        print("你太年轻了")
else:
    print("名字不好听！")
