groceries = "egg, milk,cheese"
print(groceries.split(","))


# pop
# insert
# append
# extend


colors = ["red", "yellow","blue"]
colors.insert(1,"milk")
print(colors)


nums = [1,2,3,4,5]
total = 0
for number in nums:
    total = total + number


print(total)


numbers = (1,2,3,4,5,6)
square = [num**2 for num in numbers]
print(square)

# OR

squares = []
for num in numbers:
    squares.append(num**2)
print(squares)



food = ["rice", "beans"]
food.append("broccoli")
print(food)
food.extend(["bread", "pizza"])
print(food)
print(food[:2])
print(food[3:])

breakfast = ["eggs, fruit, orange, juice"]
# print(breakfast.split())

print(len(breakfast))
print(len(food))

# print(len(food[1]))
# print(len(food[2]))
print(len(food[3]))