# a = str(6)
# print(a)
# print(str(6))

# # c = type(a)
# # print(c)
# # print(type(a))

# # c = type("abc")
# # print(c)
# # print(type("abc"))

# # l = len("Hello")
# # print(l)
# # print(len("Hello"))



# # c = "Hello"
# # l = len(c)
# # print(l)
# # print(len(c))


# import random
# n = random.randint(0, 5)
# print(n)


# import random
# def my_Randint(n: int, s: int):
#     if n > 9:
#         if s > 8:
#             print(s)
#             print("suit masterwork")
#         else:
#             print(n)
#             print(s)
#             print("masterwork")
#     elif n > 7 and n < 10:
#         print(n)
#         print("choiceness")
#     elif n > 4 and n < 8:
#         print(n)
#         print("ordinary")
#     else:
#         print(n)
#         print("inferior")
        

# s = random.randint(1, 10)
# n = random.randint(0, 10)

# my_Randint(n, s)


from ast import fix_missing_locations
import random
def my_Randint(n: int, s: int, count: int):
    if count <= 10:
        # do nothing
        pass
    elif count <= 20:
        n = n + 1
    elif count <= 30:
        n = n + 2
    
    if n >= 10:
        if s >= 9:
            print(s)
            print("suit masterwork")
        else:
            print(n)
            print(s)
            print("masterwork")
    elif n >= 8:
        print(n)
        print("choiceness")
    elif n >= 5:
        print(n)
        print("ordinary")
    else:
        print(n)
        print("inferior")
        

ss = random.randint(1, 10)
# count = random.randint(1, 50)
nn = random.randint(0, 10)


# for count in range(30, 35):
    # my_Randint(n = nn, s = ss, count = count)


from typing import List
def my_list(l: List[int]):
    a = 0
    b = 0.0
    for i in range(len(l)):
        a = a + len(l)
        b = a / 6
    print(b)
    c = 0
    for i in range(2, 4):
        c = c + l[i]
        d = c / 2
    print(d)


l = [1, 3, 5, 6, 9, 11]
my_list(l)
