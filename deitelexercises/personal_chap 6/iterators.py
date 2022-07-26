s = "hello"
it = iter(s)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


for lst in [1,2,3,4,5,]:
    print(lst)

def custom_for(iterable,func):
    it = iter(iterable)


    while True:
        try:
            func(next(it))
        except StopIteration:
            break
        # print(next(it))

def cube(num):
    print(num ** 3)

custom_for([1,2,3,4,5], print)
custom_for([1,2,3,4,5], cube)
# print(custom_for([1,2,3,4,5]))