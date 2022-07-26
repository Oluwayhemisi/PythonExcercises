class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I speak"


class Dog(Animal):
    def __init__(self, name, type_):
        super(Dog, self).__init__()
        self.type_ = type_

    pass


class Cat(Animal):
    pass


dog = Dog("Bingo")
cat = Cat("Kitten")

print(dog.name)
print(cat.name)
