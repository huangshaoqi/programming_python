"""
assert 断言
assert 条件,"条件不为真时，程序将出现异常，输出的字符串"
"""


def my_div(value, dividend):
    assert dividend != 0, "分母不为零!"
    return value / dividend


print('[my_div(10, 2)]', my_div(10, 2))
print('[my_div(10, 0)]', my_div(10, 0))
