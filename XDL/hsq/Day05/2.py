"""'字符串的操作"""

str1 = "this is a test"
str2 = "123456789"
str3 = "\t\n\r"
str4 = "ABCDefgh"
str5 = "有一个说法"

# 将字符串中的每个单词首字母大写
a = str1.title()
print(a)

# 将字符串中的大写转换称小写
b = str1.lower()
print(b)

# 将字符串中的小写转换成大写
c = str4.upper()
print(c)

# 将字符串中的大写转换称小写,将字符串中的小写转换成大写
d = str4.swapcase()
print(d)

# 统计字符串的长度
e = len(str2)
print(e)

# 查找字符串中指定字符首次出现的位置,后面2个数字参数指定查找范围
f = str4.find('e', 1, 7)
print(f)

# 替换指定字符，第三个数字参数为指定替换个数
aa = str1.replace('i', 'I', 1)
print(aa)

# 去掉字符串中的指定字符strip(),rstrip(),lstrip()
bb = str1.strip('t')
print(bb)

# 统计指定字符出现的个数,后面2个数字参数指定统计范围
cc = str1.count('s', 0, 9)
print(cc)
