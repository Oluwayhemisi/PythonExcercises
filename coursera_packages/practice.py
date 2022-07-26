# x = y = 10
# z = 2 * x + y
# print(z)
#
# x = int(input("2 + 2 = "))
# if x == 4:
#     print("Basic Arithmetic Holds")
# else:
#     print("...try again")

# age = int(input("Enter your age: "))
#
# if age == 0:
#     print("Seriously? ")
# elif age < 100:
#     print("In", 100- age, "Years you will be 100 years old")
# else: print("A century and going")


# grade = int(input("Enter the student's grade"))
#
# if grade >= 90 <= 100:
#     print(" A ")
# elif grade >= 80 < 90:
#     print(" B ")
# elif grade >= 70 < 80:
#     print(" C ")
# elif grade >= 60 < 70:
#     print(" D ")
# elif grade >= 50 < 60:
#     print(" E ")
# elif grade >= 40 < 50:
#     print(" F ")

# number = input("Please enter an integer: ")
# if number.isnumeric():
    # number = int(number)
    # if number > 20:
    #     print("your input: " +str(number) + "> 20")
    # if number > 10:
    #     print("your input: " +str(number) + " > 10")
    # if number > 0:
    #     print("your input: " +str(number) + "> 0")



number = input("Please enter an integer: ")
try:
    number = int(number)
except ValueError as e:
    print("Your input is not an Integer")
    print(e)
else:
    print(str(number)+ "is indeed an integer")