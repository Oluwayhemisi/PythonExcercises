# number1 = int(input("enter an integer: "))
# number2 = int(input("enter an integer: "))
# number3 = int(input("enter an integer: "))
#
# sum = number1 +number2 + number3
# print("the sum total of the three numbers is: ",sum)
#
# average = sum/3
# print("the  average is: ",average)
#
# product = number1 * number2 *number3
# print(product)




firstnum =int(input("enter an integer: "))
sum = firstnum
count = 0
product = firstnum
largest = firstnum
lowest = firstnum

while (count < 2):
    number = int(input("enter an integer: "))
    sum = sum + number
    product = product * number
    if number > largest:
     largest = number
    if number < lowest:
     lowest = number

    count +=1
    average = sum / count
print("the sum is: ",sum)
print("the average is: ",average )
print("the product is: ",product)
print("the largest is: ", largest)
print("the lowest is: ", lowest)