# input("请输入一个整数")
"""
请输入一个整数：  6 
请再输入一个整数： 5
6 + 5 = 11
"""
# str(6)
# int("6")

def integer():
    a = input("请输入一个整数： ")
    b = input("请再输入一个整数： ")
    c = int(a)
    h = int(b)
    var = c + h
    print(a + " + " + b + " = " + str(var))




def desim():
    f = input("请输入一个小数： ")
    g = input("请再输入一个小数： ")
    c = float(f)
    d = float(g)
    e = c + d
    print(f"{c} + {d} = {e}")

integer()
desim()