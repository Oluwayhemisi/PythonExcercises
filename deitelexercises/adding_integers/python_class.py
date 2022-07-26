class player:


    def __init__(self,nameless: str,age: int)-> None:
        self.name = nameless
        self.age =age

    def say_my_name(self):
        print()

player1 = player("Messi", 45)
print(player1.name)
print(player1.age)


player2 = player("Sharon", 15)
print(player2.name)
print(player2.age)