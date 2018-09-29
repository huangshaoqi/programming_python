""""""
import os
import pickle
import random
from XDL.python.Part_1.Task.card import Card
from XDL.python.Part_1.Task.person import Person
import sys

"""
信息存储:字典   键为卡号   值person()
起初定义一个user_dict = {}  写入到文件
第一次打开系统  字典为空
再次打开系统  加载所有用的用户信息
"""


class Operation:
    def __init__(self):
        self.load_user()

    def load_user(self):
        """加载用户信息"""
        # 首先判断文件是否存在
        if os.path.exists("user.txt"):
            with open("user.txt", "rb") as f:
                self.user_dict = pickle.load(f)
                print([[self.user_dict[cardid].card.cardid, self.user_dict[cardid].card.islock,
                        self.user_dict[cardid].card.password,
                        self.user_dict[cardid].name, self.user_dict[cardid].userid, self.user_dict[cardid].phone] for
                       cardid in self.user_dict.keys()])
        else:
            self.user_dict = {}

    def save(self):
        """保存新增修改信息"""
        with open("user.txt", "wb") as f:
            pickle.dump(self.user_dict, f)

    def register(self):
        """1.开户"""
        name = input("请输入您的姓名:")
        userid = self.cread_userid()
        phone = input("请输入您的手机号:")
        passwd = self.get_passwd()
        cardid = self.get_cardid()

        card = Card(cardid, passwd, 10)
        person = Person(name, userid, phone, card)
        self.user_dict[card.cardid] = person
        self.save()
        print("恭喜%s开户成功,您的卡号为:%s,卡内余额为:%s元" % (person.name, card.cardid, card.money))

    def get_passwd(self):
        """创建开户密码"""
        while True:
            passwd1 = input("请输入开户密码:")
            passwd2 = input("请输入确认密码:")
            if passwd1 == passwd2:
                return passwd1
            else:
                print("您输入的两次密码不一致，请重新输入！")

    def get_cardid(self):
        """生成卡号"""
        while True:
            cardid = random.randint(100000, 999999)
            if cardid not in self.user_dict:
                return cardid

    def cread_userid(self):
        """输入身份证号并检测身份证号是否已经注册"""
        while True:
            userid = input("请输入您的身份号:")
            if userid in [person.userid for person in self.user_dict.values()]:
                print("该身份证号已经被注册，请重新输入！")
            else:
                return userid

    def query(self):
        """2.查询余额"""
        card = self.get_card_info()
        # print(list(self.user_dict.keys()))
        # print(card)
        if not card:
            print("卡号不存在！")
        else:
            if card.islock:
                print("卡已被锁！")
            else:
                if self.check_password(card):
                    print("卡内余额为%s元" % card.money)

    def get_card_info(self):
        """获取卡信息"""
        cardid = int(input("请输入需要查询的卡号:"))
        # print(cardid)
        if cardid in self.user_dict.keys():
            user = self.user_dict[cardid]
            card = user.card
            return card
        else:
            # print(cardid)
            return False

    def check_password(self, card):
        """检测密码"""
        n = 1
        while n <= 3:
            password = input("请输入密码:")
            if password == card.password:
                return True
            else:
                print("密码错误，您还有%s次机会" % (3 - n))
                n += 1
                if n == 4:
                    print("密码输错三次，卡已被锁！")
                    card.islock = True
                    self.save()

    def save_money(self):
        """3.存钱"""
        card = self.get_card_info()
        if card:
            if card.islock:
                print("卡已被锁,请先解锁！")
            else:
                if self.check_password(card):
                    money = int(input("请输入存款金额："))
                    card.money += money
                    self.save()
                    print("成功存入%s，您卡内余额为%s元" % (money, card.money))
        else:
            print("卡不存在！")

    def withdraw_money(self):
        """4.取钱"""
        card = self.get_card_info()
        if card:
            if card.islock:
                print("卡已被锁，请先解锁!")
            else:
                if self.check_password(card):
                    money = int(input("请输入取款金额："))
                    if 0 < money <= card.money:
                        card.money -= money
                        self.save()
                        print("你已取款%s元，您卡内余额为%s元" % (money, card.money))
                    else:
                        print("卡内余额为%s元,取款金额不能大于卡内剩余余额" % card.money)

    def transfer_money(self):
        """5.转账"""
        card = self.get_card_info()
        if card:
            if card.islock:
                print("卡已被锁！")
            else:
                if self.check_password(card):
                    cardid = int(input("请输入转入的卡号:"))
                    if cardid not in self.user_dict.keys():
                        print("您输入的卡号不存在！")
                    else:
                        print("你输入的卡号姓名为:%s" % self.user_dict[cardid].name)
                        sure = int(input("按1确认转账,按0退出并返回主界面:"))
                        if sure == 1:
                            money = int(input("请输入转账金额："))
                            if 0 < money <= card.money:
                                card.money -= money
                                self.user_dict[cardid].card.money += money
                                self.save()
                                print("转账给%s%s元，您当前卡内余额为%s" % (self.user_dict[cardid].name, money, card.money))
                            else:
                                print("输入的金额不正确！")

    def change_password(self):
        """6.改密"""
        card = self.get_card_info()
        if card:
            if card.islock:
                print("卡已被锁！")
            else:
                if self.check_password(card):
                    password = input("请输入新密码：")
                    card.password = password
                    self.save()
                    print("密码修改成功，请牢记！")

    def lock_card(self):
        """7.锁卡"""
        card = self.get_card_info()
        if card:
            if card.islock:
                print("卡已被锁！")
            else:
                if self.check_password(card):
                    card.islock = True
                    self.save()
                    print("卡已被锁！")

    def unlock_card(self):
        """8.解卡"""
        card = self.get_card_info()
        if not card:
            print("卡不存在")
        else:
            if card.islock:
                user = self.user_dict[card.cardid]
                name = input("请输入持卡人的姓名:")
                userid = input("请输入持卡人的身份证号:")
                phone = input("请输入卡号绑定的手机号:")
                if name == user.name and userid == user.userid and phone == user.phone:
                    card.islock = False
                    self.save()
                    print("您的卡已解锁成功！")
            else:
                print("卡状态正常，不需要解锁！")

    def reissue_card(self):
        """9.补卡"""
        card = self.get_card_info()
        if not card:
            print("卡不存在")
        else:
            if card.islock:
                if self.check_password(card):

                    user = self.user_dict[card.cardid]

                    name = input("请输入持卡人的姓名:")
                    userid = input("请输入持卡人的身份证号:")

                    if name == user.name and userid == user.userid:

                        phone = input("请输入卡号绑定的手机号:")
                        password = self.get_passwd()
                        cardid = self.get_cardid()

                        new_card = Card(cardid, password, card.money)
                        user.card = new_card
                        user.phone = phone

                        self.user_dict[cardid] = user
                        del self.user_dict[card.cardid]
                        self.save()
                        print("恭喜%s补卡成功,新的卡号为:%s,卡内余额为:%s元" % (user.name, new_card.cardid, new_card.money))
                    else:
                        print("身份信息不匹配，请重新输入")
                        self.reissue_card()
            else:
                print("请先锁卡")
                sure = int(input("按1操作锁卡，按0退出:"))
                if sure == 1:
                    if self.check_password(card):
                        card.islock = True
                        self.save()
                        print("卡已被锁！")
                        print("开始进入补卡环节：")
                        self.reissue_card()

    def exit(self):
        """0.退出"""
        sys.exit()
