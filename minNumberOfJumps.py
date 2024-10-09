def minNumberOfJumps(array):
    i = 0
    counter = 0
    while i < len(array)-1:
        if array[i] > len(array)-i:
            return counter+1
        nextJump = getMaxInRange(array, i)
        i = nextJump
        counter += 1

    return counter


def getMaxInRange(array, i):
    Max = 0
    index = 0
    value = array[i]
    for j in range(value):
        if array[j+i+1] > len(array)-i:
            return j+i+1
        if array[j+i+1] > Max:
            Max = array[j+i+1]
            index = j+i+1

    return index


array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]
a = minNumberOfJumps(array)
