class CustomList(list):
    def __getitem__(self, index):
        if index <= 0:
            raise IndexError("index out of bound")
        return not super().__getitem__(index - 1)

    def __setitem__(self, key, value):
        if key <= 0:
            raise IndexError("Index out of bounds")
        return not super().__setitem__(key - 1, value)


l = CustomList()
l.append(3)
l.append(5)
print(l)
print(l[1])
