```python
"""
需求：
1、创建一支军队，包含骑兵，弓箭手，法师
2、所有兵种都能进攻和防守，但是形态各异
3、通过输入命令，控制每个兵种的攻守细节
"""
```

```python
class Cavalry:
    def attack(self):
        print("见识一下暗影岛的力量!")
    def defend(self):
        print("骑兵防守")

class Archer:
    def attack(self):
        print("明智之选，我瞄的很准，正对眉心！")
    def defend(self):
        print("弓箭手防守")

class Master:
    def attack(self):
        print("即使是死亡，也会因为我的出场而颤抖不已!")
    def defend(self):
        print("法师防守")

if __name__ == '__main__':
    Army = []

    c = Cavalry()
    a = Archer()
    m = Master()

    Army.append(c)
    Army.append(a)
    Army.append(m)

    command = input("请将军下令:")
    if command == "一起上":
        for var in Army:
            var.attack()
    elif command == "布阵":
        for var in Army:
            var.defend()
    elif command == "弓箭手":
        for var in Army:
            # 判断var是Archer的实例
            if isinstance(var,Archer):
                var.attack()
            else:
                var.defend()
    elif command == "骑兵":
        for var in Army:
            if isinstance(var,Cavalry):
                var.attack()
            else:
                var.defend()
    elif command == "法师":
        for var in Army:
            if isinstance(var,Master):
                var.attack()
            else:
                var.defend()
    else:
        print("没听清命令！")
```

## 装饰器

**普通函数**

```python
def foo(fn):
    start = time.time()
    fn()
    runtime = time.time() - start
    return runtime

def func():
    for i in range(9999999):
        pass
    print("hello")

res = foo(func)
print(res)
```

**最简单的装饰器**

```python
def outer(fn):
    def inner():
        start = time.time()
        fn()
        runtime = time.time() - start
        print(runtime)
    return inner

# 装饰器
@outer
def func():
    for i in range(9999999):
        pass
    print("hello")
func()
```

**带固定参数的装饰器**

```python
def outer(fn):
    def inner(name):
        start = time.time()
        fn(name)
        runtime = time.time() - start
        print(runtime)
    return inner

# 装饰器
@outer
def func(name):
    for i in range(9999999):
        pass
    print("hello",name)
func("jack")
```

**带不定长参数的装饰器**

```python
def outer(fn):
    def inner(*args,**kwargs):
        start = time.time()
        fn(*args,**kwargs)
        runtime = time.time() - start
        print(runtime)
    return inner

#装饰器
@outer
def func(user,name,pwd):
    for i in range(9999999):
        pass
    print(user,name,pwd)
func("jack","rose",123456)

@outer
def foo1():
    print("hello")
foo1()
```

**装饰器带参数**

```python
def foo(num):
    def outer(fn):
        def inner(*args,**kwargs):
            start = time.time()
            for i in range(num):
                fn(*args,**kwargs)
            runtime = time.time() - start
            print(runtime)
        return inner
    return outer

# 装饰器
@foo(5)
def func(user,name,pwd):
    for i in range(9999999):
        pass
    print(user,name,pwd)
func("jack","rose",123)
```

## property的作用

```python
class Person:

    def __init__(self,age,name):
        self.__age = age
        self.__name = name
        # self.age = age
    """
    def getage(self):
        return self.__age

    def setage(self,age):
        if age < 0:
            return 0
        else:
            self.__age = age

    # 把方法当作属性来使用
    @property
    def age(self):
        return self.__age
    @age.setter  # 去掉下划线的私有属性 .setter
    def age(self,age):
        if age < 0:
            self.__age = 0
        else:
            self.__age = age
    """
    @property
    def names(self):
        return self.__name

    @names.setter
    def names(self,name):
        self.__name = name

if __name__ == '__main__':

    p = Person(18,"jack")

    # p.setage(10)
    # res = p.getage()
    # print(res)

    # p.age = 10
    # print(p.age)

    # p.age = -1
    # print(p.age)

    p.names = "rose"
    print(p.names)
```

## `__repr__` 和 `__str__`

```python
class Test:

    def __init__(self,name="jack",age=12):
        self.name = name
        self.age = age

# 重写__str__
class TestStr(Test):
    # 在没有__str__的时候  __repr__ == __str__
    # 在交互模式下输入实例  回车之后自动调用
    def __repr__(self):
        return "%s:%s?"%(self.name,self.age)
    # 在调用print函数打印实例的时候自动调用
    def __str__(self):
        return "%s:%s!"%(self.name,self.age)

t = TestStr()
print(t)
```

## 运算符重载

```python
# class Person:
#     def __init__(self,num):
#         self.num = num

    # 运算符重载
#     def __add__(self, other):
#         return Person(self.num + other.num)
#
#     def __str__(self):
#         return "num = "+str(self.num)
#
# p1 = Person(2)
# p2 = Person(6)

# print(1+1) --> 2
# print("1"+"1") --> 11
# res = p1 + p2
# print(res.num)

# print(p2+p1)
```

## @staticmethod  &  @classmethod

```python
class Person:
    name = "tom"
    def __init__(self,name):
        # 添加一个实例属性
        self.name = name

    def tell(self):
        # self 是一个实例对象
        print(self.name)

    @classmethod
    def say(cls):
        # cls就是我们定义的类
        print(cls.name)

    @staticmethod
    # 绑定在类里边的一个普通函数
    def talk():
        print(Person.name)

if __name__ == '__main__':
    # p = Person("rose")
    # p.tell()
    # p.say()
    # p.talk()
    # Person.tell("rose")
    Person.say()
    Person.talk()
```









