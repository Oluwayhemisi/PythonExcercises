from collections import Counter

text = ["shoes", "bags", "pants","shoes", "bracelet","bags", "cap", "socks","bracelet", "skirt","bracelet", "skirt","cap"]

counter = Counter()
for word, count in sorted(counter.items()):
    print(f'{word}:<12{count}')


def func(lst):
    counter = {}
    for item in lst:
        if item in counter:
            counter[item] +=1
        else:
            counter[item] = 1


def func1(lst):
    from collections import defaultdict
    counter = defaultdict(int)
    for l in lst:
        counter[l] += 1

    return [k for k,_ in sorted(counter.items(), key=lambda x: x[1], reverse=True)]