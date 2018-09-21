# coding:UTF-8
"""
This is Module
"""
import sys


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


MY_INSTANCE = Myclass("小花", 20)
MY_INSTANCE.print_name()
MY_INSTANCE2 = Myclass("小绿", 30)
MY_INSTANCE2.print_age()
print(sys.version_info)
