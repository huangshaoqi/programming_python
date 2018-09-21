# -*- coding:utf-8 -*-
import abc

class Myclass:
	def __init__(self,name):
		self.name = name

	def print_name(self):
		print(self.name)

my = Myclass("小花")

my.print_name()
