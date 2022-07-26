def rotate_number(list, num):
    new_list = []
    for number in range(len(list) - num, len(list)):
        new_list.append(list[number])

    for number in range(0, len(list) - num):
        new_list.append(list[number])

    return new_list
#
#
# arg_num = 4
# lists = [19, 45, 65, 2, 6, 0]
#
# print(rotate_number(lists, arg_num))
# print(lists)

def rotate(lst,k):

    return lst[-2:] + lst[:-2]
lst = [1,2,3,4,5]
num = 2
print(rotate(lst,num))



#rotating more than the length

def rotate(lst,k):
    k = k % len(lst)
    return lst[-k:] + lst[:-k]