class Person:
	"""docstring for Person"""
	def __init__(self, name,age):
		self.name = name
		self.age = age

	def __str__(self):
		return "age:%s" % (self.age)

	def __add__(self,other):
		return "age相加之和:%s" % (self.age+other.age)
		

p1 = Person("小花",20)
p2 = Person("小军",21)
p3 = p1+p2
print(p3)


		
