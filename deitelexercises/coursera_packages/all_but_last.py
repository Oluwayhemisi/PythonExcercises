def all_but_last(seq):
    if seq == []:
        return None
    else:
        get = seq.pop()
        print(seq)
        return seq


total = [1, 2, 3, 4]
all_but_last(total)
