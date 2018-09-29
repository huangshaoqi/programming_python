""""""
"""
类名:card
属性:卡号,密码,余额

类名:person
属性:姓名，身份证号，手机号，卡

类名:view
属性:无

类名:ATM机功能
"""
from XDL.python.Part_1.Task.view import View
from XDL.python.Part_1.Task.operation import Operation

v = View()


def main():
    v.login()
    o = Operation()
    while True:
        choice = input("请选择需要办理的业务:")
        if choice == "1":  # 开户
            o.register()
        elif choice == "2":  # 查询
            o.query()
        elif choice == "3":  # 存钱
            o.save_money()
        elif choice == "4":  # 取钱
            o.withdraw_money()
        elif choice == "5":  # 转账
            o.transfer_money()
        elif choice == "6":  # 改密
            o.change_password()
        elif choice == "7":  # 锁卡
            o.lock_card()
        elif choice == "8":  # 解卡
            o.unlock_card()
        elif choice == "9":  # 补卡
            o.reissue_card()
        elif choice == "10":  # 返回首页
            v.opration_view()
        elif choice == "0":  # 退出
            o.exit()


if __name__ == '__main__':
    main()
