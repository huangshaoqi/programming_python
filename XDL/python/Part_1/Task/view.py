import time


class View:

    def login(self):
        while True:
            name = input("请输入管理员账号:")
            pwd = input("请输入管理员密码:")
            if name == "admin" and pwd == "123":
                self.login_view()
                time.sleep(1)
                self.opration_view()
                break
            else:
                print("管理员账号或密码不正确!")

    def login_view(self):
        print("********************************************")
        print("*                                          *")
        print("*                                          *")
        print("*           Welcome to XDL Bank            *")
        print("*                                          *")
        print("*                                          *")
        print("********************************************")

    def opration_view(self):
        print("********************************************")
        print("*       开户(1)           查询(2)          *")
        print("*       存钱(3)           取钱(4)          *")
        print("*       转账(5)           改密(6)          *")
        print("*       锁卡(7)           解卡(8)          *")
        print("*       补卡(9)           退出(0)          *")
        print("*              返回首页(10)                *")
        print("********************************************")
