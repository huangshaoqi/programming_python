<<<<<<< HEAD
# -*- coding:utf-8 -*-
import abc
=======
# coding:UTF-8
"""
This is Module
"""
import sys

>>>>>>> 1466e80ce29f553b69063063decde59716b572cd

class Myclass:
    """"This is Myclass"""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_name(self):
        """This is test mothod."""
        print(self.name)

    def print_age(self):
        """This is test mothod"""
        print(self.age)


<<<<<<< HEAD
my.print_name()
=======
MY_INSTANCE = Myclass("小花", 20)
MY_INSTANCE.print_name()
MY_INSTANCE2 = Myclass("小绿", 30)
MY_INSTANCE2.print_age()
print(sys.version_info)
>>>>>>> 1466e80ce29f553b69063063decde59716b572cd
