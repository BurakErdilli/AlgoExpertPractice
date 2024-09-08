def smallestDifference(array1, array2):
    array1 = sorted(array1)
    array2 = sorted(array2)
    i1 = 0
    i2 = 0
    couple = [None, None]
    minDiff = abs(array1[i1]-array2[i2])
    while i1 <= len(array1)-1 and i2 <= len(array2)-1:
        if minDiff > abs(array1[i1]-array2[i2]):
            minDiff = abs(array1[i1]-array2[i2])
            couple[0] = array1[i1]
            couple[1] = array2[i2]
        if array1[i1] > array2[i2]:
            i2 += 1
        elif array1[i1] < array2[i2]:
            i1 += 1
        else:
            return minDiff, sorted(couple)

    return minDiff, couple


array1 = [-1, 5, 10, 20, 28, 3]
array2 = [26, 134, 135, 15, 17]

a, pair = smallestDifference(array1, array2)
