list_ = ['food','love','money','shopping','travelling']
list1 = []
for item in list_:
    list1.append(item)
print(list1)

list3 =[item **3 for item in range(1,6)]
print(list3)

list4 =[item for item in range(1,20) if item % 2 ==  0]
print(list4)

colors = ['red', 'yellow', 'green', 'blue', 'pink', 'black', 'white']
colors2 = [item.upper() for item in colors]
print(colors2)

cubes =[(x, x**3) for x in range(1,6)]
print(cubes)