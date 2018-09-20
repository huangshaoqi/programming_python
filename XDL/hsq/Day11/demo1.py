from XDL.hsq.Day11.demo import Person

class man(Person):
    def __init__(self, sex, **kwargs):
        super().__init__(sex, **kwargs)
        # Person.__init__(self,sex,**kwargs)
        self.sex = sex

    def print_sex(self):
        print("我是%s" % self.sex)

    def tell(self):

        pass


if __name__ == '__main__':
    p = man("男")
    p.print_sex()
    p.welcome()

