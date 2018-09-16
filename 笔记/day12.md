**类的引入的好处：**

**之前我们学过了函数，函数的好处是，把功能封装起来，以便我们后边可以随时的调用，但是这些都可以说是面向过程变成，他注重的是结果，而我们今天所讲的面向对象它更注重程序的过程，比方说我们现在有一个人走在一条长达一千米的公路上，如果他的行走速度为两米每秒，那他需要多长时间呢？如果用面向过程来解释的话那就直接用1000/2，我们就可以得到结果了，但是如果我们用面向对象来解释的话，我们可以在程序中创建一条长达1000米的公路，然后再创建一个人，设置它的行走速度为两米每秒，然后让程序去运算它会走多少时间，它更加注重过程了，这就是面向对象！**

**面向对象有三大特征，封装，继承，多态：**

**封装：我们把乱七八糟的数据都放到一个列表当中，这是一种封装，但是这是属于数据层面的封装，我们还可以把常用的代码段打包成一个函数，这是语句的封装，咱们今天学的面向对象就是这两种的合一。对象是模拟真实世界，把数据和代码都封装到一起，为什么说对象是对真实世界的封装呢，一会我们就可以感受到了。封装更是一种信息隐蔽技术，让我们的数据更加安全，比如说：列表，列表是Python的一个序列对象，那我们需要对里边的数据进行数据排序，我们怎么做呢？那咱们不由自主的就想起来用到sort方法,那我们提到了方法二字，没错，python的列表事实上就是一个对象，提供了诺干种方法，供我们根据需求调整列表，但是咱们知道列表对象里边的这些方法是怎么实现的吗？必然不知道！我们知道列表对象里边有哪些变量么？必然也不知道！这就是所谓的封装，它封装起来，只给我们每个方法的名字，当咱们需要用到这个方法的时候，直接调用这个名字就可以了。那他具体怎么实现的有没有告诉我们？----没有。OK！这就是封装。**

**继承：继承，就是子类自动共享父类之间数据和方法的机制,比如说我们随便先定义一个类，然后我们让他继承list，下边我们用Pass代替，也就是说我们不做任何事情，只是继承list，然后我们把这个类实例化出来，那么我们这个类也就有了List的所有方法，这就是继承**

```python
class MyList(list):
    pass

# 实例化对象
list1 = MyList()

list1.append(5)
list1.append(6)
print(list1)
```

**多态：比方说同学们过来培训，那么有的学H5，有的学java，有的学python等等，我们学的内容都不一样，但是只要我们来了，我们就要学习，那我们上自习的时候，班主任说上课了，开始自习，也就是说我们只是调用了一个开始学习的方法，那么各个学科的同学都去调用自己的学习方法了吧，而班主任是不需要管你是哪个学科的吧，他只要调用一个学习的方法就可以了，剩下的就是H5的调用H5的学习方法，python的调用python的学习方法，也就是说你们都是学生的子类，都继承了学生类，但是你们分为不同形态，也就是说多态就是一个父类有多种具体实现各不相同的子类形态，这就是多态，所以有了继承和多态我们就可以实现大规模的复用，这就是面向对象的好处。**

```python
"""
需求：
1、封装一个Person类，
2、封装一下属性：姓名、年龄、存款，
3、封装自我介绍的方法，陈述以上属性，
4、创建一个人，设置基本信息，
5、打印此人信息，
6、令此人进行自我介绍。
"""
```

```python
# 所有的类都继承于 object 类
class Person:
    # 类属性
    name = "韩梅梅"
    age = 18
    rmb = 20
    # 构造方法:在实例化的时候自动被调用
    def __init__(self,name,age,rmb):
        self.name = name
        self.age = age
        self.rmb = rmb

    # 析构方法:在程序结束的时候自动被调用
    # def __del__(self):
    #     print("__del__:我被调用了!",self.name)
    # 方法
    def tell(self):
        # name = "韩梅梅"
        # age = 18
        # rmb = 20
        print("我叫%s,我今年%s岁了,我有存款%.2f万元"%(self.name,self.age,self.rmb))

# 创建一个人
p = Person("小明",16,10)
p.tell()

p1 = Person("小红",16,11)
p1.tell()
```

```python
"""
下边我们再来看一个需求：
1、为存款信息添加保护，使其不能直接被访问
2、添加设置密码功能
3、添加存款查询功能，只有输入密码正确的情况下才能查询存款信息
"""
```

```python
class Person:

    def __init__(self,name,age,rmb):
        # 公有属性
        self.__name = name
        self.age = age
        # 私有属性  不能被直接访问  通过公有方法访问私有属性
        self.__rmb = rmb

    # 公有方法
    def getrmb(self):
        pwd = input("请输入查询密码:")
        if pwd == "123":
            print("我有存款%.2f万元"%(self.__rmb))
        else:
            print("您没有访问权限!")

    # 私有方法  不能直接被访问  通过公有方法访问私有方法
    # def __setrmb(self,rmb):
    #     self.__rmb = rmb

    # def setrmb(self,rmb):
    #     pwd = input("请输入设置密码:")
    #     if pwd == "456":
    #         self.__rmb = rmb
    #         print(self.__rmb)
    #     else:
    #         print("没有设置权限!")

if __name__ == '__main__':
    p = Person("韩梅梅",18,20)
    # print(p.__rmb)

    # p.setrmb(1)
    # p.getrmb()

    # p.name = "小明"
    # print(p.name)

    # p.setrmb(10)
```

```python
"""
1、封装坏蛋类用以存储坏蛋的信息
2、坏蛋拥有人的一切正常属性和功能
3、坏蛋有恶习属性和作恶方法
4、创建一个坏蛋，为他设置最基本信息和恶习
5、让他作恶
"""
```

```python
from day12.person import Person
class Bastard(Person):

    def __init__(self,name,age,rmb,badhobby):
        # 拓展父类属性
        super().__init__(name,age,rmb)
        # self.name = name
        # self.age = age
        # self.rmb = rmb
        self.badhobby = badhobby

    # 父类方法重写
    # def tell(self):
    #     print("劳资乃%s,今年%s岁了,劳资有存款%.2f万元,劳资就是喜欢%s"%
    #               (self.name,self.age,self.rmb,self.badhobby))

    # 方法拓展
    # def tell(self):
    #     super().tell()
    #     print("劳资乃%s,今年%s岁了,劳资有存款%.2f万元,劳资就是喜欢%s"%
    #           (self.name,self.age,self.rmb,self.badhobby))

    # def talk(self):
    #     print("劳资乃%s,今年%s岁了,劳资有存款%.2f万元,劳资就是喜欢%s"%
    #           (self.name,self.age,self.rmb,self.badhobby))

if __name__ == '__main__':
    b = Bastard("谢文东",20,200,"喝酒打架")
    b.tell()
    # b.talk()
```

```python
"""
需求：
1、封装男人类，继承于person类，使之有阳刚风格的自我介绍，使之能咆哮
2、封装女人类，继承于person类，使之有阴柔风格的自我介绍，使之能撒娇
3、封装gay类，使之同时具有男人和女人的特性
4、令其咆哮，令其撒娇
5、令其偏阳刚的进行自我介绍，令其偏阴柔的进行自我介绍
"""
```

```python
from day12.person import Person
class Man(Person):

    def tell(self):
        print("劳资乃%s,今年%s岁了,劳资有存款%.2f万元"%
              (self.name, self.age, self.rmb))

    def paoxiao(self):
        print("┗|｀O′|┛ 嗷~~，劳资就是天下第一！")

class Women(Person):

    def talk(self):
        print("小女子%s，小女今年%d了，小女有存款%.2f万元！" %
              (self.name, self.age, self.rmb))

    def sajiao(self):
        print("喵~~~ 你真讨厌了啦！")

class Gay(Women,Man):
    pass

# m = Man("史泰龙",50,3000)
# m.tell()
# m.paoxiao()
#
# w = Women("金莲",16,0.1)
# w.tell()
# w.sajiao()

g = Gay("库克",45,10000000)
g.tell()
g.talk()
g.paoxiao()
g.sajiao()
```

