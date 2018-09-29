# -*- coding:utf-8 -*-
class Person:
    name = "某某某"
    age = 18
    rmb = 20

    def __init__(self, name=name, age=age, rmb=rmb):
        self.__name = name
        self.__age = age
        self.__rmb = rmb
        self.__job = "Software"
        self.__password = 123
        self.n = 1
        # self.person_info()

    def password(self):
        if self.n == 1:
            pwd = int(input("请输入设置密码:"))
            if pwd == self.__password:
                self.n = 0
                return True
            else:
                return False
        else:
            return True

    def welcome(self):
        print("1：查询职业\t\t2：设置职业\t\t3：修改姓名\t\t4：修改年龄\t\t5：打印个人信息".center(50, "*"))
        num = input("请输入你要执行的步骤编号：")
        if num == "1":
            self.getjob()
            self.welcome()
        elif num == "2":
            self.setjob()
            self.welcome()
        elif num == "3":
            self.setname()
            self.welcome()
        elif num == "4":
            self.setage()
            self.welcome()
        elif num == "5":
            self.person_info()
            self.welcome()
        else:
            print("不能识别你输入的编号！")
            self.welcome()

    def __setname(self, name):
        self.__name = name

    def setname(self):
        if self.password():
            name = input("请输入您的姓名：")
            self.__setname(name)
            print("你设置的姓名是:", self.__name)
        else:
            print("你没有设置权限！")

    def __setage(self, age):
        self.__age = age

    def setage(self):
        if self.password():
            age = input("请输入您的年龄：")
            self.__setage(age)
            print("你设置的年龄是:", self.__age)
        else:
            print("你没有设置权限！")

    def __setjob(self, job):
        self.__job = job

    def setjob(self):
        if self.password():
            job = input("请输入您的职业：")
            self.__setjob(job)
            print("你设置的职业是:", self.__job)
        else:
            print("你没有设置权限！")

    def getjob(self):
        if self.password():
            print("你的职业是:", self.__job)
        else:
            print("您没有查询权限！")

    def person_info(self):
        print("您的信息如下：\n姓名:%s\t\t年龄:%s\t\t收入:%s万元\t\t职业：保密" %
              (self.__name, self.__age, self.__rmb))


if __name__ == '__main__':
    p1 = Person()
    p1.welcome()
