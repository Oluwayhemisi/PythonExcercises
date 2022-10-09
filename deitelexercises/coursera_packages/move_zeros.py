def move_zero(lst):
    list1 = []
    list2 = []
    for i in lst:
        if i != 0:
            list1.append(i)
        else:
            list2.append(i)

    lst = list1 + list2

    return lst
lst_ = [0,1,0,2,0,3,0,4]
print(move_zero(lst_))