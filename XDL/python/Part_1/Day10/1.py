# # def myfun():
# #     return 0
# # for i in (1,2,3):
# #     print(myfun)
# # print("########################")
def outer():
    fs = []
    for i in (1, 2, 3, 4):
        def inner():
            return 0

        print(inner)
        # fs.append(inner)
    return fs


outer()

# print("########################")
# def outer():
#     def inner():
#         return 0
#     print(inner)
#     f1 = id(inner)
#
#     def inner():
#         return 0
#     print(inner)
#     f2 = id(inner)
#
#     def inner():
#         return 0
#     print(inner)
#     f3 = id(inner)
#
#     def inner():
#         return 0
#     print(inner)
#     f4 = id(inner)
# outer()
