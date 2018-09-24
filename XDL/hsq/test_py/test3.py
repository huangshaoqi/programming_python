"""抽象基类"""
import sys
import abc


class Aclass(metaclass=abc.ABCMeta):
    """禁止实例化"""

    @abc.abstractmethod
    def bet(self):
        """1"""
        return 1

    def record_win(self):
        """2"""
        pass

    def record_loss(self):
        """3"""
        pass


class Bclass(Aclass):
    """4"""

    def bet(self):
        return "Hello world!"


# bet = BettingStrategy2()
# print(bet.bet())
<<<<<<< HEAD
		
b = B()
print(b.bet())

import sys

from tkinter import *

root = Tk()

widget = Button(master=root, cnf={"text": "Press", "command": sys.exit})
widget.pack(side=TOP, fill=BOTH)
root.mainloop()
=======
B = Bclass()
print(B.bet())
print(sys.version_info)
>>>>>>> 1466e80ce29f553b69063063decde59716b572cd
