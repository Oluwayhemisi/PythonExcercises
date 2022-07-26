import sys

lst=[]
for i in range(1,11):
    lst.append(i)
print(lst)

 # you can try it in another method
# list(range(1,10))

# using list composition

x =[i for i in range(1,11) if i % 2 ==0]
print(x)
#
# list_ =[num for num in range(1,11)]
even = [num for num in range (1,11) if num % 2 == 0]
even_and_squared_odds = [num if num % 2 == 0 else num **2 for num in range(1,11)]
# list_input = [int(input("Enter a number: ")) for num in range(1,4)]
# print(list_)
print(even)
print(even_and_squared_odds)
# print(list_input)


list_nested_for = [(x,y) for x in range (1,5) for y in range (6,10)]
print(list_nested_for)

upper_names =[name.upper() for name in ["dolapo","tolani","florence"]]
# length_name =[len(name) for name in ["dolapo","tolani","florence"]]
print(upper_names)

# list_of_dicts = [{key:value} for key,value in zip(upper_names,even)]
#
# # generator expression is a bracket list
list_ =[num for num in range(1,11)]
#
# gen =(num for num in range(1,11))
# print(list_)
# print(list(gen))
#
#
# # to get the size
# print(sys.getsizeof(list_))
# print(sys.getsizeof(gen))
#
#
# # set comprehension uses curlybraces
# list_ ={num for num in range(1,11)}
#
# # dictionary comprehension
#
# dict_comp = {k:v for k, v in zip(range(5),range(5))}
# print(dict_comp)


# # intersection update
# s1 = {1,2,3,4,5,6}
# s2 = {4,5,6,7,8,9}
# #
# s1 &= s2
# # print(s1)
#
# # # union
# print(s1 | s2)
#
# # update
# s1 |= s2
# print(s1)
#
# # pop
# s1.pop()
# print(s1)

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,8,9}

# print(s1 - s2)


# subset and superset

s1 = {1,2,3,4,5,6}
s2 = {4,5,6,7,}
print(s1 ^ s2)
print(s1 > s2)
print(s1 < s2)


dict_play = {"name":"Tolani","age":18, "influenced":"samson"}
print(dict_play["name"])

# if name is not found return argument get
dict = {"age":18, "influenced":"samson"}
print(dict.get("name","samson"))


dict.pop("influenced")

# dict.items()
# iterating the keys from empty dict
print({}.fromkeys("hello", "UNKNOWN"))

# Function to get a string and return a string
def get_first(s: str) -> str:
    return s[0]

l = [get_first(val) for val in ["Hello", "How", "Are","You"]]
print(l)