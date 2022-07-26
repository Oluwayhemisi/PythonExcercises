x = "python"
print(tuple(x))

name = "david"
print(name[1])

numbers = (1, 2, 3, 4)
print(len(numbers))

name, age, occupation = "David", 42, "programmer"
print(name)

vowels = ("a", "e", "i", "o", "u")
y = "o" in vowels
print(y)

# to pack tuples
coordinates = 4.21, 9.29
print(coordinates)

#unpack tuples

i,j = coordinates
print(i)
print(j)


def adder_subtractor(num1, num2):
    return (num1 + num2, num1 - num2)





print(adder_subtractor(5,3))

# pack tuples
cardinal_numbers = "first", "second", "third"
print(cardinal_numbers[1])

# unpack tuples

position1, position2, position3 =cardinal_numbers
print(position1)
print(position2)
print(position3)

my_name = ("y", "e", "m", "i", "s", "i")
check = "x" in my_name
print(check)

print(my_name[1:])