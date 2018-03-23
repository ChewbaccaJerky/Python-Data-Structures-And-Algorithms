
def merge_sort(array):
    if len(array) <= 1
        return array

    mid = len(array) / 2
    left = merge_sort(array[0:mid-1])
    right = merge_sort(array[mid:-1])

    return merge(left, right)

def merge(left, right):
    if len(right) == 0:
        return left
    
    if len(left) == 0:
        return right

    result = []

    while len(left) > 0 and len(right) > 0:

        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:-1]
        else:
            result.append(right[0])
            right = right[1:-1]
    
    result += right if len(left) == 0 else result += left

    result

