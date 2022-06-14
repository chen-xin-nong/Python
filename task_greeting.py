"""
What is your surname: xxx
Please input your given name: xxx
Hello, xxx xxx 
the length of your surname = 6
the length of your given name = 7
"""



surname = input("What is your surname: ")
name = input("Please input your given name: ")
print("Hello " + surname + " " + name)
a = len(surname)
b = str(a)
print("the length of your surname = " + b)
# print(len(surname))
c = len(name)
print("the length of your givenname = " + str(c))
# print(len(name))