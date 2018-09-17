Products = [
    ["iphone", 5000],
    ["bike", 800],
    ["ipad", 6000],
    ["computer", 8000]
]
cost = 0
buy_product = set()

top_info = "超市".center(50, "=")
print(top_info)
for num, product in enumerate(Products):
    print(num + 1, product[0], product[1])
button_info = "=" * len(top_info)
print("输入0退出")
print(button_info)

flag = 1
while flag:
    salary = input("请输入卡内余额:")
    if salary.isdigit():
        salary = int(salary)
        while True:
            if salary > 0:
                input_num = input("请输入你要购买的商品编号:")
                if input_num.isdigit():
                    input_num = int(input_num)
                    if input_num == 0:
                        print("您本次购买的商品如下：")
                        for product in buy_product:
                            print(product)
                        print("您本次共消费%s元,卡内余额为%s元,欢迎下次光临." % (cost, salary))
                        flag = 0
                        break
                    elif 0 < input_num <= len(Products):
                        if salary >= Products[input_num - 1][1]:
                            salary -= Products[input_num - 1][1]
                            cost += Products[input_num - 1][1]
                            buy_product.add(Products[input_num - 1][0])
                            print("您本次购买的%s,价格为%s,卡内余额为:%s" % (
                                Products[input_num - 1][0], Products[input_num - 1][1], salary))
                        else:
                            print("卡内剩余%s元，不足以购买此商品!" % salary)
                    else:
                        print("没有找到你输入的商品编号，请重新输入！")
                else:
                    print("请正确输入商品编号！")
            else:
                print("卡内余额不足，请充值！")
                break
    else:
        print("只支持正整数，请重新输入！")
