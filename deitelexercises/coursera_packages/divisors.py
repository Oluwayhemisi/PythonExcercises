def divisors(n):
    get = []
    for i in range(1, n + 1):
        if n % i == 0:
            get.append(i)
    return get


print(divisors(7))
