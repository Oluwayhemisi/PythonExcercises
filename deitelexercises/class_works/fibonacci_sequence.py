
number = int(input("enter a number: "))
a,b = 0,1
count = 0
while count <= number:
    print(a,end=" ")
    a,b = b,a+b
    count += 1



