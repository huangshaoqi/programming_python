# 系统默认6种数据类型
# 1数值类型number
# 整型Int
# 浮点类型float
# 布尔类型bool
# 复数类型complex
# 2字符串类型string
# 单引号
# 双引号
# 三引号
# 3列表类型list
# 标识符：[]
# 4元组类型tuple
# 标识符：，
# 5字典类型dict
# 标识符：{}
# 6集合类型set
# 无标识符

# type()  查看一个变量的数据类型
a = 1 + 0j
b = 3j
print(a, type(a))
print(b, type(b))

str1 = """'金星'说:"人不犯我，我不犯人，人若犯我，忍让三分，人若再犯，铲草除根。" """
print(str1, type(str1))

str2 = "金星说:人不犯我，我不犯人，" \
       "人若犯我，忍让三分，" \
       "人若再犯，铲草除根。"
print(str2, type(str2))

str3 = """金星说:人不犯我，
我不犯人，人若犯我，忍让三分，
人若再犯，铲草除根。"""
print(str3, type(str3))

str4 = "金星说:人不犯我，\n我不犯人，人若犯我，\n礼让三分，人若再犯，铲草除根。"
print(str4)

# \表示转义  把后边的字母转换成有特殊含义的
a = "D:\兄弟连\python15期\代码\\tew"
print(a)

a = "a\\\\nb"
print(a)

# r 代表元字符
a = r"\n"
print(a)

str4 = "金星说:\"人不犯我，我不犯人，人若犯我，礼让三分，人若再犯，铲草除根。\""
print(str4)

a = [1, 2, 3]
print(a, type(a))

a = (1, 2, 3)
print(a, type(a))

b = ()
print(b, type(b))

a = {"a": 1, "b": 2, "c": 3}
print(a, type(a))
b = {}
print(b, type(b))

a = {1, 2, 3, 4, 5, 2, 4, 3, 5}
print(a, type(a))
b = set()
print(b, type(b))
