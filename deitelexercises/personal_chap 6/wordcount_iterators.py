from collections import Counter

text = ('My mommy just got back from the market'
        'mommy got pack of sweets on her way from the market')

counter = Counter(text.split())

for word,count in sorted(counter.items()):
    print(f'{word:<12}{count}')
