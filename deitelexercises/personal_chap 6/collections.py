import collections
c1 = collections.Counter("Hello world")
print (c1)
c2 = collections.Counter("Hi you")
print(c2)
c1.subtract(c2)
print(c1)

Person = collections.namedtuple("person","name age")
p1 = Person(name="Adeola", age= 16)
print(p1.name)

c1 = collections.Counter("")