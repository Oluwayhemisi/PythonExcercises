from dataclasses import dataclass, field


@dataclass(frozen=True, order=True)
class Person:
    # __slots__ = ['name', 'age']
    name: str
    age: int = field(default=16)
    children: list = field(default_factory=lambda: [])

    def is_minor(self):
        return self.age < 18


p1 = Person("Adeola", 16)
p2 = Person("Adeola", 16)
print(p1.is_minor())
print(p1 >= p2)
