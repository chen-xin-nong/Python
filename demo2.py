
def isGood(a):
    # if a >= 0 and a <= 100:
    #     if a >= 80:
    #         print('very good')
    #     elif a >= 60:
    #         print('pass')
    #     else:
    #         print('fail')
    # else:
    #     print(f'{a} is an invalid number')

    if a >= 80 and a <= 100:
        print('very good')
    elif a >= 60 and a < 80:
        print('pass')
    elif a >= 0 and a < 60:
        print('fail')
    else:
        print(f'{a} is an invalid number')
    


isGood(a = 80)
# isGood(a = 60)
# isGood(a = 20)
# isGood(a = -200)

