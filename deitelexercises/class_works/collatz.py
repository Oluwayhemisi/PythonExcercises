#
# number = int(input("Enter a number "))
# while number != 1:
#     if number % 2 != 0:
#         number = number * 3 + 1
#     elif number % 2 == 0:
#         number = number // 2
#     print(number, end=" ")


nterms = int(input('How many figures'))
n1, n2 = 0, 1
count = 0
if nterms == 0:
    print('Enter a positive number')
elif nterms <= 1:
    print('This is a fibonacci series')
while count < nterms:
    print(n1)
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
# import math
# radius = int(input("enter a number"))
# circumference = 2 *math.pi *radius
# print (circumference)


