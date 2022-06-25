try:
    number = int(input("Enter an integer"))
except ValueError:
    print("That was not an integer")



def divide(num1, num2):
    try:
        print(num1/num2)
    except TypeError:
        print("Both argument must be numbers")
    except ZeroDivisionError:
        print("num2 must not be zero")

divide(3,0)

