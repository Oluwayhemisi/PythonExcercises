def factors_(x):
    result_ = []
    for i in range(1, x + 1):
        if x % i == 0:
            result_.append(i)
    return result_


print(factors_(4))


def prime_num(x):
    if x == 1:
        return False
    for num in range(2,x):
        if x % num == 0:
            return False
    return True


print(prime_num(24))


def composite(x):
    count = 0
    for number in range(1, x+1):
        if x % number == 0:
            count += 1
    if count > 2:
        return True
    return False


print(composite(9))


def perfect_num(x):
    count = 0
    for num in range(1, x):
        if x % num == 0:
            count += num
    if count == x:
        return True
    return False

print(perfect_num(15))

def abundant_number(x):
    count = 0
    for num in range(1, x):
        if x % num == 0:
            count +=num
    if count > x:
        return True
    return False


print(abundant_number(12))