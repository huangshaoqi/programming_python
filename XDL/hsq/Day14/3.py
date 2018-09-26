
class A:

    def __init__(self):
        print("print A")


class B(A):

    def __init__(self):
        super().__init__()
        print("print B")


class C(A):

    def __init__(self):
        super().__init__()
        print("print C")


class D(B, C):

    def __init__(self):
        super().__init__()
        print("print D")

print(D.mro())

d = D()
