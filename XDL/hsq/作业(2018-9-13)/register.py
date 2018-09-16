# -*- coding:utf-8 -*-
import pickle
import os
import sys


def register():
    name = input("请输入一个用户名:").strip()

    # 读取数据库信息，为后面检测用户提供比对信息
    try:
        with open("user_info.data", "rb") as f:
            users_dict = pickle.load(f)
            # print(users_dict)
    except Exception:
        users_dict = {}

    # 与数据库信息比对，检测用户名是否被占用
    if name in users_dict.keys():
        print("用户名已被占用，请重新注册.")
        register()

    def password_confirm():
        """
        检验密码
        """
        passwd = input("请输入您的密码:").strip()

        # 检测密码格式是否正确和2次密码是否一致
        if passwd.isnumeric():
            passwd_confir = input("请确认您的密码:").strip()

            # 2次密码是否一致
            if passwd == passwd_confir:
                return passwd
            else:
                print("两次密码不正确，请重新输入！")
                password_confirm()
        else:
            print("输入的字符不支持,请重新输入！")
            password_confirm()

    # 获取输入的密码信息
    password = password_confirm()

    # 临时生成一个空字典来存储用户注册提交的信息
    user_info = dict()
    user_info[name] = [password, True]
    users_dict.update(user_info)

    # 将账户密码信息写入数据库中
    with open("user_info.data", "wb") as fd:
        pickle.dump(users_dict, fd)
    print("注册成功！")
    sys.exit()


if __name__ == "__main__":
    # 检测数据库文件是否存在，不存在则新增文件
    if not os.path.exists("user_info.data"):
        with open("user_info.data", "wb") as fd:
            users_dict = dict()
            pickle.dump(users_dict, fd)

    register()
