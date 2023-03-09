def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        less = [x for x in array[1:] if x <= pivot]
        greater = [x for x in array[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(quick_sort([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
print(quick_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print(quick_sort([11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
