a = 1
b = 10
c = "hello"

# usingprintf
print("i read the {} textbook {} times in {} day".format(c, b,a))

print(f"i read the {c} textbook {b} times in {1} day")

print ("i read the {1} textbook {0} times in {1} day".format(a,b))

print(("i read the {1} textbook {0} times in {1} day".format(5,20)))

f'{10:>20.2f}'
print(f'{10:>20.2f}')

f'{10:^20.2f}'
print(f'{10:^20.2f}')


smiley = "\U0001f600"

for i in range(1, 21, 2):
    print(f"{smiley * i:>20}")


for i in range(1, 21, 2):
    print(f"{'x' * i:^20}")

star = "*"

for i in range(1, 11):
        print(f"{star * i:<10}      {star *(11 - i):<10}    {star *(11 - i):>10}   {star * i:>10}")


f"{0.1:.2%}"

letter = "hello world"
for index, letter in enumerate(letter):
    print(f"{index} ----> {letter} ")

# space

name = "john Marwood cleese"
first, middle, last = name.split()
transformed = last+ ', ' + first+ ' '+middle

