class Person:
    """人"""

    def __init__(self, gun):
        self.gun = gun

    def fire(self, m=1):
        """开火"""
        self.gun.shoot(m)

    def fill(self, n=1):
        """装载子弹"""
        self.gun.bullet.num += n
