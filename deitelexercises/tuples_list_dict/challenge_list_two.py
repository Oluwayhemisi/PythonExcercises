import random

nouns = ["fossil","horse", "aardvark", "judge", "chef", "mango","extrovert", "gorilla"]
verbs = [ "kicks","jingles","bounces","slurps","meows","explodes", "curdles"]
adjectives = [ "furry","balding","incredulous","fragrant","exuberant", "glistening"]
prepositions = ["against","after","into","beneath","upon","for", "in", "like", "over", "within"]
adverbs  = ["curiously","extravagantly","tantalizingly","furiously", "sensuously"]


random_nouns = []
random_element = random.choice(["fossil","horse", "aardvark", "judge", "chef", "mango","extrovert", "gorilla"])
random_element_two = random.choice([ "kicks","jingles","bounces","slurps","meows","explodes", "curdles"])
random_element_three = random.choice([ "furry","balding","incredulous","fragrant","exuberant", "glistening"])
random_element_four = random.choice(["against","after","into","beneath","upon","for", "in", "like", "over", "within"])
random_element_five = random.choice(["curiously","extravagantly","tantalizingly","furiously", "sensuously"])


random_nouns.append(random_element)
random_nouns.append(random_element_two)
random_nouns.append(random_element_three)
random_nouns.append(random_element_four)
random_nouns.append(random_element_five)
print(random_nouns)

wax_poetic = [ ["fossil","horse", "aardvark", "judge", "chef", "mango","extrovert", "gorilla"],
               [ "kicks","jingles","bounces","slurps","meows","explodes", "curdles"],
               [ "furry","balding","incredulous","fragrant","exuberant", "glistening"],
               ["against","after","into","beneath","upon","for", "in", "like", "over", "within"],
               ["curiously","extravagantly","tantalizingly","furiously", "sensuously"]
]

random.choice(wax_poetic)


