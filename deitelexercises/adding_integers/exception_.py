def divide(a,b):
    if b == 0:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("At least you can see the the function is divide")
        raise ValueError("Denominator cannot be zero")
    return a/b
# print(divide(2,0))



num = input("Enter the numerator: ")
den = input("enter the denominator: ")
while True:
    try:
        print(divide(num,den))
        break
    except ValueError:
        print("wrong value")
        num = int(input("Enter the numerator: "))
        den = int(input("enter the denominator: "))
    except TypeError:
        print("wrong value")

# try:
#     print(divide(2,0))
# except:
#     print("wrong value")