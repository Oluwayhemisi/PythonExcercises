amount = float(input("Enter amount: "))
rate = float(input("Enter the rate: "))
year = int(input("Enter the year: "))


def invest(amount, rate, years):
    for i in range(1,year+1):
        amount = amount *(rate/100) + amount
        print(f"year {i:} ₦{amount:.2f}")


invest(amount,rate,year)