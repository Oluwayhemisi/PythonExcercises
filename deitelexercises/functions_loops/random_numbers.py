import random

# print(random.randint(1,10))



def coin_flip():
    if random.randint(0,1) == 0:
        return "heads"
    else:
        return "tails"

heads_tally = 0
tails_tally = 0


for trial in range(10_000):
    if coin_flip() == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio = heads_tally / tails_tally
print(f"The ratio of heads to tail is{ratio}")


def unfair_coin_flip(probabilty_of_tails):
    if random.random() < probabilty_of_tails:
        return "tails"
    else:
        return "heads"


for trial in range(10_000):
    if unfair_coin_flip(.7) == "heads":
        heads_tally = heads_tally + 1
    else:
        tails_tally = tails_tally + 1

ratio1 = heads_tally/tails_tally
print(f"The ratio of heads to tail is {ratio1}")
        
