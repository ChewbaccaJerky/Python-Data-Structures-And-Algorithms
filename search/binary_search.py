
def binary_search(value, array):
    mid = len(array) / 2

    if value == array[mid]:
        return True
    elif value < array[mid]:
        return binary_search(value, array[0:mid-1])
    else:
        return binary_search(value, array[mid+1:-1])