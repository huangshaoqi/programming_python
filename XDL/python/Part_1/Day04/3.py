"""
小球降落
"""
m = 100  # 距离地面长度
k = 0  # 每次上升的高度
a = 0  # 轨迹长度
while True:
    if m <= 1:
        print(m)
        break
    else:
        a = a + m + k
        k = m * 0.5
        m = m - m * 0.5
        print(a)
print(a)

print("#" * 50)

height = 100
sum = 0
while True:
    if height < 1:
        sum -= height
        print(height)
        break
    else:
        sum += height + height * 0.5
        print(sum)
        height -= height / 2
        # print(height)
print(sum)
