def singleCycleCheck(array):

    n = len(array)
    cycleList = [0 for i in range(n)]
    index = 0
    for i in range(n):
        cycleList[index] += 1
        nextIdx = (index+array[index]) % n
        if nextIdx < 0:
            nextIdx += n
        index = nextIdx
    if any(i != 1 for i in cycleList):
        return False, cycleList
    return True, cycleList


test = [2, 2, -1, 3, 1, -5, -2]


a, b = singleCycleCheck(test)
