# -*- coding:utf-8 -*-
import pickle
import sys


def login():
    n = 3  # 密码初始输入最大次数
    username = input("请输入您的用户名:").strip()

    # 读取数据库信息，为后面检测用户和密码提供比对信息
    try:
        with open("user_info.data", "rb") as f:
            users_dict = pickle.load(f)
            # print(users_dict)
    except Exception:
        users_dict = {}

    # 与数据库信息比对，检测账户是否被冻结
    if username in users_dict.keys():
        if users_dict[username][1] == False:
            print("用户已被冻结！")
            login()
    else:
        print("输入的用户不存在，请重新输入！")
        login()

    def password():
        """
        检测密码输入次数，账户是否被冻结
        """
        passwd = input("请输入您的密码:").strip()
        nonlocal n
        nonlocal users_dict

        # 与数据库信息比对，密码是否正确
        if users_dict[username][0] == passwd:
            n = 3  # 登陆成功后，重置密码可允许输错次数
            print("登陆成功！")
            sys.exit()
        else:
            n -= 1  # 输错一次，可允许密码输错次数n的值减少一次
            if n <= 0:
                users_dict[username][1] = False

                # 更新数据的账户状态
                try:
                    with open("user_info.data", "wb") as f:
                        pickle.dump(users_dict, f)
                except Exception:
                    users_dict = {}

                print("密码输入三次失败，账户被锁定")
                # 密码输错三次被锁定之后，重新进入登陆界面
                login()
            else:
                print("输入密码错误，您还剩下%d次机会！" % n)
                # 密码输错之后，重新进入密码输入界面
                password()

    # 检测完用户名之后开始执行密码输入与检测
    password()


if __name__ == "__main__":
    # 执行登陆操作
    login()
