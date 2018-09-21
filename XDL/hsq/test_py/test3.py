import abc
"""抽象基类"""
class A(metaclass=abc.ABCMeta):
	"""禁止实例化"""
	@abc.abstractmethod
	def bet(self):
		return 1

	def record_win(self):
		pass

	def record_loss(self):
		pass

class B(A):
	def bet(self):
		return "Hello world!"

# bet = BettingStrategy2()

# print(bet.bet())
		
b = B()
print(b.bet())

import sys

from tkinter import *

root = Tk()

widget = Button(master=root, cnf={"text": "Press", "command": sys.exit})
widget.pack(side=TOP, fill=BOTH)
root.mainloop()
