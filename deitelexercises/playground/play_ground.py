import time

#
# def decorator(fn):
#     def wrapper(*args,**kwargs):
#         print("I am decorating you")
#         fn(*args, **kwargs)
#         print("okay bye")
#     return wrapper
#
# def timer(fn):
#     def inner_function(*args, **kwargs):
#         start = time.time()
#         fn(*args, **kwargs)
#         total_time = time.time() - start
#         print(f"you took{total_time:.2f} seconds to run")
#     return inner_function()
#
#
#     @timer
#     def square(a: int):
#         print(a * a)










class Playground:
    def __init__(self,firstname: str, lastname: str, age:int):
        self._fullname = f"{firstname}{lastname}"
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if age< 0:
            raise ValueError("Age cannot be negative")
        self._age = age

    @age.deleter
    def age(self):
        print("Deleting soon....")
        del self._age



p1 = Playground( 78)
print(p1.age)
p1.age = 16
print(p1.age)

del p1.age
print(p1.age)