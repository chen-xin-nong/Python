def number_to_month():
    
    a = input("请输入一个数字： ")
    a =int(a)
    if a == 1:
        print("一月份，第一季度")
    elif a == 2:
        print("二月份，第一季度")
    elif a == 3:
        print("三月份，第一季度")
    elif a == 4:
        print("四月份，第二季度")
    elif a == 5:
        print("五月份，第二季度")
    elif a == 6:
        print("六月份，第二季度")
    elif a == 7:
        print("七月份，第三季度")
    elif a == 8:
        print("八月份，第三季度")
    elif a == 9:
        print("九月份，第三季度")
    elif a == 10:
        print("十月份，第四季度")
    elif a == 11:
        print("十一月份，第四季度")
    elif a == 12:
        print("十二月份，第四季度")

    else:
        print("对不起，无效输入")


number_to_month()