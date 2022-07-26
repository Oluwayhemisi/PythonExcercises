colors = ["red","yellow","green", "blue"]
colors.sort()
print(colors)


colors.sort(key=len)
print(colors)


def get_second_element(item):
    return item[1]


items = [(4,1),(1,2),(-9,0)]
items.sort(key=get_second_element)
print(items)



data = ((1,2), (3,4))

count = 0
sum = 0
for i in data:
    for j in i:
        sum = sum + j
    count+=1
    print(f"Row {count} sum: {sum}")
    sum = 0



num = [4,3,2,1]
copy_num = num[:]
copy_num.sort()
print(copy_num)












