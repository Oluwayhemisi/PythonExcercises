voucher = []


class Basket:
    def __init__(self, basket_length: int, amount: int):
        self.basket_length = basket_length
        self.basket = []
        self.bought_item = []
        self.amount = amount
        self.counter = 0
        self.spent_amount = 0

    def add(self, item: str, amount: int):
        if self.counter == self.basket_length:
            first_item = self.basket[0]
            self.spent_amount = self.spent_amount - first_item[1]
            self.basket.remove(first_item)
            Basket.add_item(self, item, amount)

        else:
            Basket.add_item(self, item, amount)

    def get_length(self):
        return self.counter

    def get_basket(self):
        return self.basket

    def add_item(self, item, amount):
        self.bought_item.append(item)
        self.bought_item.append(amount)
        self.spent_amount += amount
        self.basket.append(self.bought_item)
        self.bought_item = []
        self.counter += 1
