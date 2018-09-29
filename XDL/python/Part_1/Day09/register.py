# -*- coding:utf-8 -*-
f = open("userinfo.txt", "a+")
flag = 1  # 当flag为0时结束注册

while flag:
    # 用户名输入检测
    username = input("请输入您的用户名:")
    if username != "" and " " not in username:
        f.seek(0, 0)
        content = f.readlines()
        username_list = [i.split(":")[0] for i in content]
        if username in username_list:
            print("您输入的用户名已被占用，请重新输入！")
            continue
    else:
        print("您输入的用户名存在非法字符，请重新输入！")
        continue

    # 密码输入检测
    while True:
        passwd = input("请输入您的密码：")
        if passwd != "" and " " not in passwd:
            passwd1 = input("请确认您的密码：")
            if passwd == passwd1:
                # 用户名和密码合格，写入文件
                f.write("%s:%s\n" % (username, passwd))
                f.flush()
                print("注册成功！")
                flag = 0
                break
            else:
                print("两次密码输入不匹配，请重新输入！")
        else:
            print("您输入的密码格式不正确，请重新输入！")
f.close()
