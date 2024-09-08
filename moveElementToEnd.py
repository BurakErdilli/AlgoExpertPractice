def moveToEnd(array, key):
    i = 0
    j = len(array)-1
    while j > i:
        if array[j] == key:
            j -= 1

        elif array[i] == key:
            array[i] = array[j]
            array[j] = key
            j -= 1
            i += 1
        else:
            i += 1

    return array


array = [2, 1, 2, 2, 2, 3, 4, 2, 4, 4, 4]
key = 4
a = moveToEnd(array, key)
