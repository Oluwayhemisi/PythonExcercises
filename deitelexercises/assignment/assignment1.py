text = ["shoes", "bags", "pants","shoes", "bracelet","bags", "cap", "socks","bracelet", "skirt","bracelet", "skirt","cap"]

print(f'{"WORD":<12}{"COUNT"}')

for i in text:
    print(f'{i:<12}{text.count(i)}')