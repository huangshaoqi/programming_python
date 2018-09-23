class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "Hello" + self.name


print(Person("xiaohong"))
