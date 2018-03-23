
def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    left = []
    right = []

    for num in array[1:-1]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return quick_sort(left) + [pivot] + quick_sort(right)