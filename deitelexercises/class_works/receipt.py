
num = 'X'
num1 = "Florence & Sons Group of Company"
num2 = "312, Herbert Macaulay,Sabo,Yaba,Lagos."
num3 = "07017623456 flo@gmail.com"
num4 = "-"


products_ = []
price_ = []
qty = []
total_ = []


count = 0
state = True
while state:
    product = str(input("Enter the product you want to buy: "))
    products_.append(product)

    price = int(input("Enter the price of the product: "))
    price_.append(price)

    quantity = int(input("enter the quantity: "))
    qty.append(quantity)

    total = price * quantity
    total_.append(total)

    count += 1
    print(" do you want to buy more? ")
    reply = int(input("""enter
                      1 --> Yes
                      2 --> No """ ))
    print()
    print()
    print()

    if reply == 1:
        state =True
    elif reply == 2:
     state = False

final_total = sum(total_)
print()
print()
print()
print()
print()
print()
print()
print()

print(' '*20, num1)
print('                    ',num2)
print('                    ',num3)
print(num *90)

print('                   product        quantity       price      total')
for i in range(0, count):
    print(f'{products_[i]:>25}   {qty[i]:>10}     {price_[i]:>9}    {total_[i]:>9}')
print(num4 * 90)
print(" "*16 + "The total is:       ", final_total)
print(num * 90)


print("Thank you for your patronage.")


