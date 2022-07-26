# lst =[1,4,3,2]
# print(lst[1])
#
# lst = [  ]
# # for i in range(1,10,2):
# for i in range(1,10):
#     if i % 2 != 0:
#      lst.append(i)
# print(lst)
#
# # list comprehension
# lst =[ i for i in range(1,10)  if i % 2 != 0 ]
#
# # to collect input from the user
# lst=[ input("enter a number") for _ in range (10)]
# lst=[i:= input("enter a number") for _ in range (10) if i*i  ]
#
#
#
# # converting this to list comprehension
# lst= []
# for i in range (65,91):
#     lst.append(chr(i))
# print(lst)
#
# # list comprehension
# from functools import reduce
#
# lst =[chr(i) for i in range (65,91) ]
# print(lst)
#
#
#
# # LAMBDA
# # using lambda
# add = lambda x,y: x+y
# sub = lambda x,y: x-y
# print(add.__name__)
# print(sub.__name__)
#
#
# # instaed of functions_loops
#
# def add(a,b):
#     return a + b
#
# def sub(c,d):
#     return c-d
#
# def mult( i,j):
#     return i * j
#
# def operate(x,y,func):
#     return func(x,y)
#
# val_sub = operate(5, 24,sub)
# val_add = operate(5,24,add)
# val_mult = operate(5,5,mult)
#
#
#
#
# print(val_sub)
# print(val_add)
# print(val_mult)
#
# # using lambda
# div = operate(4,54, lambda X,Y: Y/X)
# add = operate(4,54, lambda X,Y:  X + Y)
# sub = operate(4,54, lambda X,Y: Y-X)
#
# print(div)
# print(add)
# print(sub)
#
# # another classwork where a function takes one param and a function to double and
# def multiple(x,func):
#     return func(x)
#
# square = multiple(3,lambda x: x**2)
# print(square)
# tripple = multiple(2,lambda x: x**3)
# print(tripple)
#
# # using function any or all
# # any will return true
# # all will return false
# print(all([1,2,3,4,5,6,7,9,0]))
# print(any([True,False,True]))
#
# names = ["Amaka", "Segun", "comb","Samson","foil"]
# print(all([name.istitle() for name in names]))
# print([name.istitle() for name in names])
from functools import reduce

peoples = [
    {"name":"Omosetan Omorele", "age": 30, "year_of_exp":4, "language":["Python","Java"]},
    {"name":"Joe Doe", "age": 25, "year_of_exp":2, "language": ["Javascript","C#"]},
    {"name":"Amaka Stephen", "age": 19, "year_of_exp":5, "language": ["Python"]},
    {"name":"Florence Segun", "age": 26, "year_of_exp":15, "language": ["Python","Java"]},
    {"name":"Ogunnpa Challenge", "age": 30, "year_of_exp":4, "language": ["Kotlin","Java"]} ]
print(all(people for people in peoples))
print([people["age"] <= 28 and "Python" in people["language"] for people in peoples])
print([people["name"] for people in peoples if people ["age"] <= 28 and "Python" in people["language"]])
print(any(True if people["age"] <= 20 else False for people in peoples))
#
# # using map
# lst  = [1,2,3,4,5,6]
# # var = [num ** 2 from num in lst]
#
# lst= map(lambda x:x**2,lst)
# lst_= map(lambda x:x**2,range(1,10))
# print(lst)
#
# # a map object evaluate once
# # anything you can do with list comprehension, you can do it with map
# map_object = map(lambda x: x**2,range(1,10))
# map_object = map(lambda x: x**2 if x % 2 == 0 else x,range(1,10))
# lst1 = list(map_object)
# print(lst1)
#
# # filter
# def isEven(x):
#     return x % 2 ==0
# filter_obj = (filter(isEven,range(1,10)))
# print(filter_obj)
#
#
# # reduce
# lst = reduce(lambda x,y: x+y, range(1,11))
# print(lst)
#
# fruits = ["Apple", "Pear", "Pineapples", "Orange", "Watermelon", "Orange","Watermelon"]
# longest = reduce(lambda x,y: x if len(x) >= len(y) else y,fruits)
# print(longest)
# # the max works aphabetically order, that is letter with highest letter
# # but when you use len, it  them by length
# print(max(fruits, key = len))
# # using the shortest length from shortest to longest
# print(sorted(fruits, key = len))
# # moving from longest to highest by reverse
# print(sorted(fruits, key = len,reverse=True))
# # sorting by the last number using index
# print(sorted(fruits, key = lambda x: x[-1]))
