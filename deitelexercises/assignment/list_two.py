import sys

even_num = [num for num in range (1,11) if num % 2==0]
print(even_num)

even_and_squared = [num if num % 2 ==0 else num **2 for num in range(1,11)]
print(even_and_squared)

list_nested = [(x,y) for x in range(1,5) for y in range (6,10)]
print(list_nested)

upper_names =[name.upper() for name in ["dolapo","tolani","shola","ayo"] if name[-1] == "o" ]
print(upper_names)

list_len = [len(name) for name in ["dolapo","tolani","shola","ayo"] ]
print(list_len)

list_ = [num for num in range(1,11)]
print(list_)
print(sys.getsizeof(list_))

gen = (num for num in range(1,11))
print(list(gen))

list_ = {num for num in range(1,11)}
print(list_)

dict_comp = {k:v for k, v in zip(range(5),range(5))}
print(dict_comp)

s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}

s1 &= s2
print(s1)
print(s1 | s2)
s1 |= s2
print(s1)

s1 = {1,2,3,4,5,6,7,8}
s2 = {4,5,6,7,8}
print(s1 ^ s2)
print(s1 < s2)

dict_play = {"name":"Tolani","age":18,"influenced":"samson"}
print(dict_play["name"])
print(dict_play.get("name"))
print(dict_play.pop("age"))
print(dict_play)

def get_first(s: str) -> str:
    return s[-1]
l = [get_first(val) for val in ["Hello", "How", "Are", "You",]]
print(l)

def mutable_ish(a=None):
    if a is None:
        a = []
    a.append('python')
    return a

print(mutable_ish())
print(mutable_ish([1,2,3,4]))

student_1 = [2,3,4,5,6]
student_2 = [2,4,6,8,10]
student_3 = [1,3,5,7,9]

print(list(zip(student_1,student_2,student_3)))

sum_per_subject = []
highest_ =[max(subject) for subject in zip(student_1,student_2,student_3)]
print("the max value is: ",highest_)
sum_ = [sum(subject) for subject in zip(student_1,student_2,student_3)]
print("the sum is",sum_)

s = "Hello"
print(s[0:-1])