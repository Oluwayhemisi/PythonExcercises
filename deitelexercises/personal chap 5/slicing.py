numbers = [2,3,5,7,11,13,17,19]
print(numbers[2:6])

print(numbers[:8])
print(numbers[0:8])

print(numbers[2:])
print(numbers[2:len(numbers)])
print(numbers[:])
print(numbers[::-1])

numbers[0:3]= ['Two','Three', 'Four']
print(numbers)


num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(num[1:len(num):2])

num[5:10]=[0] * len(num[5:10])
print(num)

num[5:]=[]
print(num)

num[:] =[]
print(num)

num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
del(num[0:2])
print(num)

def modify_element(items):
    for i in range (len(items)):
        items[i] *= 2

numbers_ =[10, 3, 7, 1, 9]
modify_element(numbers_)
print(numbers_)
