# -*- coding:utf-8 -*-
"""
购物消费
"""
import sys

# 商品信息，{编号,[商品名称,价格]}
Products = {
    1: ["iphone", 5000],
    2: ["bike", 800],
    3: ["ipad", 6000],
    4: ["computer", 8000]
}

# 期初余额
Balance = 0

# 已购买的商品
Buy_Product = set()

# 当前消费金额
Cost = 0


# 购物消费操作
def buy():
    # 输入卡内余额
    global Balance
    Balance = input("请输入您的卡内余额:").strip()

    if Balance.isnumeric():
        Balance = int(Balance)
    else:
        print("请输入的余额不正确，请重新输入")
        buy()

    # 定义顶端显示
    head_info = "%sXDL超市%s\n" % (("=" * 21,) * 2)

    # 打印商品信息
    product_info = ""
    for num in sorted(Products.keys()):
        product_info += str(num) + " " + Products[num][0] + " " + str(Products[num][1]) + "\n"

    tips = "输入0退出\n"

    # 定义底端显示
    bottom_info = "%s" % ("=" * len(head_info))

    # 打印所有消息
    info = head_info + product_info + tips + bottom_info
    print(info)

    def select_product():
        """
        选择商品编号消费
        """
        global Buy_Product
        global Balance
        global Cost

        number = input("请输入要购买的商品编号:").strip()
        if number.isdigit():
            number = int(number)
            if number == 0:
                buy_info = "您本次购买的商品如下:"
                products_info = ""
                for p in Buy_Product:
                    products_info += "\n" + p
                end_info = "\n您本次共消费%d元,卡内余额为%d元,欢迎下次光临." % (Cost, Balance)
                print(buy_info + products_info + end_info, end='')
                sys.exit()
            if number in [i for i in list(Products)]:
                number = number
            else:
                print("没有此商品编号，请重新输入")
                select_product()
        else:
            print("没有此商品编号，请重新输入")
            select_product()

        # 如果余额小于商品价格，提示余额不足，不予购买
        if Balance >= Products[number][1]:
            Balance -= Products[number][1]

            # 统计当前共消费的金额
            Cost += Products[number][1]
            Buy_Product.add(Products[number][0])
            print("购买%s成功，本次消费%d元,卡内余额%d元." % (Products[number][0], Products[number][1], Balance))
            select_product()
        else:
            print("余额不足！")
            select_product()

    # 执行消费
    select_product()


if __name__ == '__main__':
    buy()
