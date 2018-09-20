class Person:

    # __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age


# @property
# def age(self):
#     return self.__age

# @age.setter
# def age(self, age):
#     self.__age = age


from types import MethodType


def tell(self):
    print("my name is %s" % self.name)


def talk(self):
    print("This is outer method")


p = Person("xiaohong", 21)

print(p.name)
print(p.age)

# p.sex = "man"
# print(p.sex)


p.speak = MethodType(tell, p)
p.speak()

p2 = Person("小绿", 18)
Person.talk = MethodType(talk, Person)
p2.talk()
