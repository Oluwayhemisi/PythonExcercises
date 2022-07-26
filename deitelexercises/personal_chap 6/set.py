colors = {'red', 'orange', 'yellow', 'green','red','blue'}
print(colors)
print(len(colors))
print('red' in colors)

for color in colors:
    print(color.upper(), end=" ")

numbers = list(range(10)) + list(range(5))
print(numbers)
print(set(numbers))

set1 ={1,3,5}
set2 = {1,5,3}

print(set1 == set2)


text = 'to be or not to be that is the question'

text_set = {}

text_set = set(text.split())

for word in sorted(text_set):
    print(word, end=" ")
set3 = {1,3,5}
set4 = {2,3,4}
print(set3.union(set4))
print(set3.intersection(set4))

num1 = {10,20,30}
num2 = {5,10,15,20}

print(num1 - num2)
print(num1 ^ num2)
print(num1.union(num2))
print(num1 & num2)

numbers = {1,3,5}
numbers |= {2,3,4}
print(numbers)
numbers.add(17)
print(numbers)
numbers.remove(17)
print(numbers)
numbers.pop()
numbers.pop()
print(numbers)
set_numbers =[1,2,2,3,4,5,6,6,7,8,9,10,10]
evens ={item for item in set_numbers if item % 2 == 0}
print(evens)