text = ('My mommy just got back from the market'
        'mommy got pack of sweets on her way from the market')

word_counts = {}

for word in text.split():
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f'{"WORD":<12}{"COUNT"}')
for word,count in sorted(word_counts.items()):
    print(f'{word:<12}{count}')










