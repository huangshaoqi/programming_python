class C:
    name1 = "xxx"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_attr(self):
        print(self.name)

    @staticmethod
    def print_hello():
        print("hello, world!")
        print()

    @classmethod
    def print_hello2(cls):
        print("Hello,%s" % cls.name1)


if __name__ == "__main__":
    c = C("小花", 35)
    c.print_hello()
    c.print_hello2()
