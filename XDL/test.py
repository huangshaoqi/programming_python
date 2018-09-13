def get_score():
    score = int(input("请输入你的成绩："))
    if 0 <= score <= 100:
        if score == 100:
            print("满分")
        elif score >= 90:
            print("优秀")
        elif score >= 80:
            print("良好")
        elif score >= 60:
            print("及格")
        else:
            print("不及格")
    else:
        print("你输入的成绩不正确，请重新输入！")
        get_score()


get_score()
