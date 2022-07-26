def gen():
    count = 0
    while True:
        yield count
        count += 1


tiger = gen()

print(next(tiger))
print(next(tiger))
print(next(tiger))


#
# for i in gen():
#     print(i)


def counter(low, high, step=1):
    while low <= high:
        yield low
        low += step


for i in counter(2, 10):
    print(i)

print(list(counter(2, 6, 2)))
