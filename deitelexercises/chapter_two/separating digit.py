
# count =0
# first = []
# while (count < 2):
#     number = int(input("Enter number: "))
#     first.append(number)
#     count+=1
#
# print(first, end="  ")



number = int(input("Enter numbers: "))

first_number = number % 100000
second_number = number % 10000
third_number = number % 1000
fourth_number = number % 100
fifth_number = number % 10

num1= int(first_number/10000)
num2 =int (second_number/1000)
num3 = int(third_number/100)
num4 = int(fourth_number/10)
num5 = int(fifth_number/1)

print(num1,"  ",num2,"  ",num3,"  ",num4,"  ",num5 )