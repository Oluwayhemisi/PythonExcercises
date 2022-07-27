password = " "
# while password != "secret":
#     password = input("please Enter password ")
#     if password == "secret":
#         print("welcome")
    # else: print("The password you entered is incorrect. Please try again!")

x = 1
while x <= 10:
    if x == 5:
        break
    print("X is now: ", x)
    x += 1

for i in range(1,20):
    if (i % 2 != 0):
      if (i % 3 == 0):
          continue
    print(i)
    
for i in range(1, 4):
    print('i:', i)
    for j in range(1,3):
        if(j<= 1):
            break
        print('\t', 'j:', j)
num_list = []
i = 0
playing = True

while (playing == True):
    num =int(input("Enter num: "))
    if (num == -1):
        playing =  False
    else: num_list.append(num)
    i += 1
print(i)
