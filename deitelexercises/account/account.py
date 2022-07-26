# def add(x,y):
#     return x + y
#
# def subtract(x,y):
#     return x - y

class Account:
    def __init__(self, name: str,password:  str, phone_number: str):
        self.password = password
        self.phone_number = phone_number
        self.balance = 0
        self.name = name

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Insufficient fund")
        if amount > self.balance:
            raise ValueError("Transaction cannot be completed!")
        self.balance = self.balance - amount

    def transfer(self,other_account: str, amount: int):
        self.withdraw(amount)
        # other_account.deposit(amount)

