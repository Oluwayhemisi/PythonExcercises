def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        great = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(great)


print(quicksort([2, 4, 6, 7, 8]))
