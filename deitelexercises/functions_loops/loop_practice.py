word = "python"
index = 0


while index < len(word):
    print(word[index])
    index = index + 1



for letter in "python":
    print(letter, end=" ")
print("\n")


amount = float(input("Enter an amount: "))

for num_people in range(2,6):
    print(f"{num_people} people: {amount / num_people:,.2f} each")


for n in range(1,4):
    for j in range(4,7):
        print(f"n = {n} and j = {j}")


for n in range(2,10):
    print(f"n = {n}")
print("\n")


integer = (2,3,4,5,6,7,8,9,10)
index = 0

while index < len(integer):
    print(integer[index])
    index = index + 1




x ="Hello world"

def func():
    x = 2
    print(f"Inside 'func', x has the value {x}")
func()
print(f"Outside 'func', x has the value {x}")


def outer_func():
    y =3

    def inner_func():
        z = x + y
        return z
    return inner_func()

sum_of_evens = 0

for n in range(1,100):
    if n % 2==0:
        sum_of_evens = sum_of_evens + n

print(sum_of_evens)


for i in range(0,4):
    if i == 2:
        break
    print(i)

print(f" finished with n = {i}")


for letter in range(3):
    password = input("Enter password")
    if password == "I<3Bieber":
        break
    print("password is incorrect")

else:
    print("Suspicious activity. The authorities have been alerted")






























