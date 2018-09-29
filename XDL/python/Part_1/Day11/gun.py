class Gun:
    """枪"""

    def __init__(self, bullet):
        self.bullet = bullet

    def shoot(self, m=1):
        """发射"""
        if 0 < self.bullet.num <= m:
            print("突~" * self.bullet.num + "\n子弹打完了..")
            self.bullet.num = 0
        elif self.bullet.num > m:
            print("突~" * m + "\n还剩下%s颗子弹" % (self.bullet.num - m))
            self.bullet.num -= m
        else:
            print("弹夹子弹不足，请填充弹！")
