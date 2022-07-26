import random
a = random.randint(0, 10)
print(a)


# using seed so everyone can get the same number
# random.seed(76)
# print(random.randint(0,10))
# print(random.randint(0,100))
#
# print(random.randrange(0,10,2))
#
# print(random.random())
#
# list = [1,2,3,4,5,6,7]
# print(random.choice(list))

# this is to shuffle the numbers
# print(random.shuffle(list))
# print(list)
# print(random.choice(list))

#






#
# def get_digit(number,position):
#     """return digit at position in number,counting from right"""
#     assert  4 == 2, "4 is not equal 2"
#     return number //(10**position)%10
# # it is counting backward hat is,position zero is 4
# print(get_digit(234,2))