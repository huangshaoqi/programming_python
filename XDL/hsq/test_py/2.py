"""123"""

class Buttlet:
    """
    弹夹
    """

    def __init__(self, buttletcount):
        self.buttletcount = buttletcount


class Gun:
    """
    枪
    """

    def __init__(self, buttlet):
        self.buttlet = buttlet

    def shoot(self, n):
        if self.buttlet.buttletcount >= n:
            print("突~" * n)
            print("您还剩下%s颗子弹!" % (self.buttlet.buttletcount - n))
            self.buttlet.buttletcount -= n

        elif 0 < self.buttlet.buttletcount < n:
            print("突~" * self.buttlet.buttletcount)
            self.buttlet.buttletcount = 0
            print("您子弹打完了..")
        else:
            print("没子弹，请填充子弹!")


class Person:
    """123"""

    def __init__(self, gun):
        self.gun = gun

    def fire(self, n=1):
        self.gun.shoot(n)

    def fill(self, m=1):
        self.gun.buttlet.buttletcount += m


buttlet = Buttlet(10)
gun = Gun(buttlet)
p = Person(gun)

p.fire(9)
p.fire(9)
p.fill(15)
p.fire(5)
p.fire(10)
p.fire(1)
