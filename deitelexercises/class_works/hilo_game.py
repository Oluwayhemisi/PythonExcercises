
count = 1
while count > 0:
    number = int(input("enter a number: "))

    if number < 15:
        print("low")
    elif number > 15:
        print("high")
    elif number == 15:
        print("you got it")
        break
        count +=1

