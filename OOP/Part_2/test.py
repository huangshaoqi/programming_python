class Person:
	def __init__(self,name,age,sex):
		self.name = name
		self.age = age
		self.sex = sex

	def print_info(self):
		return self.name,self.age,self.sex

p = Person("小花", 18, "男")

print(p.print_info())