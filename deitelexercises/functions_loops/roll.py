import random


def roll():
    # if random.randint(1,6) == 1:
    #     random_num = 1
    # elif random.randint(1,6) == 2:
    #     random_num = 2
    # elif random.randint(1,6) == 3:
    #     random_num = 3
    # elif random.randint(1,6) == 4:
    #     random_num = 4
    # elif random.randint(1,6) == 5:
    #     random_num = 5
    # else:
    #     random_num = 6
    #
    # return random_num

    # for i in range(1,6):
    return random.randint(1, 7)


print(roll())


for i in range(10_000):
    count = 0
    if roll() == 1:
        count += 1

print(count)

