"""
var = input("input a number: ")
var = int(var)
if var == 8:
    print("good")
    print("var = 9")
elif var > 8:
    print("var > 8")
elif var < 8:
    print("var < 8")
else:
    print("var does not equal to 9")
    
print("end")
"""

def number_to_week_day():
    b = input("Please input a number: ")
    
    b = int(b)
   

    if b == 1:
        print("Today is Monday")
    elif b == 2:
        print("Today is Tuesday")
    elif b == 3:
        print("Today is Wednesday")
    elif b == 4:
        print("Today is Thursday")
    elif b == 5:
        print("Today is Firday")
    elif b == 6:
        print("Today is Saturday")
    elif b == 7:
        print("Today is Sunday")

    else:
        print("Sorry invalid input")

number_to_week_day()
