

# def sum(n: int):
#     a = 0
#     for i in range(1, n + 1, 2):
#         if i % 3 == 0:
#             a = a + i

#     print(a)

# m = 11
# # sum(m)



def sum1():
    a = 0
    for i in range(1, 101):
        if i % 2 == 0 and i % 10 == 0:
            a = a + i
            
    print(a)

# sum1()

def sum2(n: int):
    a = 0
    for i in range(1, n + 1, 3):
        if i % 2 == 0 and i % 10 == 0:
            print(f"i = {i}")
            a = a + i
    print(a)

n = 200

sum2(n)
