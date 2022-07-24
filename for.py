# print('Hello World')
# print('Hello World')
# print('Hello World')


# for i in range(11):
#     print(i)





def sum(a):
    sum = 0
    for i in range(5,11):
        print(i)
        # sum = sum + i


    print(sum)


# sum(a = 10) # 1 + 2 + .. + 10 = 55
   


def print_numbers(n: int):
    for i in range(1, n + 1, 2):
        print(i)
    for i in range(10, 16):
        print(i)
# print_numbers(n = 10)


def nested_loop():
    for i in range(4):
        for j in range(4):
            if j > 0 and i > 2:
                print(i + j)
            


def nested_loop():
    for i in range(4):
        if i > 2:
            for j in range(4):
                if j > 0:
                    print(i + j)
nested_loop()