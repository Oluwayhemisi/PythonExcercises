
range_ = [1,2,3,4,5,6,7,8,9]
a_list = []

for number in range_:
    a_list.append(number)
print(a_list)

list1 = [10,20,30,40]
list2 = [30, 70]

concatenate = list1 + list2
print(concatenate)

for i in range(len(concatenate)):
    print(f'{i}: {concatenate[i]}')


def cube_list(values):
    for i in range(len(values)):
        values[i] **= 3

numbers = [1,2,3,4,5,6,7,8,9,10]
cube_list(numbers)
print(numbers)

characters =[]
characters += 'BirthDay'
print(characters)

# Tuple

student_tuple = ()
student_tuple = 'John', 'Green', 3.3
print(student_tuple)
tuple1 =(10, 20, 30)
tuple1 +=(40, 50)
print(tuple1)

tuple__ = ()
tuple__+= (10,20,30,40,50)
print(tuple__)

# mutable object

student_tuple = ('Jane', 'Doe', [87,45,70])
student_tuple[2][2] = 50
print(student_tuple)

student_tuple = ('Jane', [87,45,70])
first_name, grades = student_tuple
print(first_name)
print(grades)

first, second = 'hi'
print(f'{first} {second}')

number1, number2, number3 =[2,3,4]
print(f'{number1} {number2} {number3}')

colors = ['red', 'green', 'black']
x = list(enumerate(colors))
print (x)

color_names =['orange', 'yellow', 'blue']
color_names.insert(0, 'purple')
print(color_names)

color_names.append('brown')
print(color_names)

color_names.extend(['white', 'green'])
print(color_names)

color_names.remove('brown')
print(color_names)

color_names.clear()
print(color_names)

color_names =['orange', 'yellow', 'blue']
color_names.reverse()
print(color_names)

copy_list = color_names.copy()
print(copy_list)

rainbow =['green', 'orange', 'violet']
rainbow.insert(2,'red')
print(rainbow)

rainbow.append('yellow')
print(rainbow)

rainbow.reverse()
print(rainbow)

rainbow.remove('orange')
print(rainbow)