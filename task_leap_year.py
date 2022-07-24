# def isLeapYear():

#      a =2000

#      if a % 100 == 0:
#              if a % 4 == 0:
#                   print("is leap year")
#               else:
#                      print("is common year")

          
#      else:
#             print("is common year")



# y = 2000
# isLeapYear()

def isLeapYear(a, b):
      print(b)
      if a % 4 == 0 and a % 100 != 0:
            print(f"{a} is leap year")
      else:
            print("is common year")



y = 2000
isLeapYear(a = y, b = y)