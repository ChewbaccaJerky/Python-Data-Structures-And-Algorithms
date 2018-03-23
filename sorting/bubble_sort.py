
def bubble_sort(array):

    sorted = False

    while not sorted:

        sorted = True

        i = 0
        while i+1 < len(array):
            if array[i+1] < array[i]:
                # swap
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                sorted = False
            i += 1
    
    return array
            
