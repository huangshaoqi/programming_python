# -*- coding:utf-8 -*-

flag = 1  # 为0 时结束登陆环节
while flag:
    username = input("请输入您的用户名:")
    # 1.黑名单检测
    with open("black_userinfo.txt", "a+") as f:
        f.seek(0, 0)
        content = f.readlines()
        if username in [line.rstrip("\n") for line in content]:
            print("您的用户已被冻结，请联系管理员")
            continue

    with open("userinfo.txt", "r") as f:
        f.seek(0, 0)
        # 读取账户信息，转换为字典形式{用户名:密码}
        accounts = [line.rstrip("\n").split(":") for line in f.readlines()]
        accounts_dict = dict(accounts)

        # 2.用户名是否存在检测
        if username not in accounts_dict.keys():
            print("用户名不存在，请重新输入!")
            continue
        else:
            # 3.检测密码
            n = 3
            while n > 0:
                pawd = input("请输入您的密码:")
                # 两次密码相等
                if pawd == accounts_dict[username]:
                    print("登陆成功！")
                    flag = 0
                    break
                else:
                    # 两次密码不相等情况
                    if n == 1:
                        with open("black_userinfo.txt", "a") as f:
                            # 输错3次，写入黑名单
                            f.write("%s\n" % username)
                            print("密码输错3次，账户已被冻结")
                            break
                    else:
                        n -= 1
                        print("您的密码已输错，还有%s次机会" % n)
