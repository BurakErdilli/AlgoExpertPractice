def findThreeLargest(array):
    threeLargest = [None, None, None]
    for num in array:
        updateThreeLargest(threeLargest, num)
    return threeLargest


def updateThreeLargest(threeLargest, num):
    if threeLargest[2] is None:
        threeLargest[2] = num
        return

    if threeLargest[1] is None:
        threeLargest[1] = num
        return

    if threeLargest[0] is None:
        threeLargest[0] = num
        return

    if num < threeLargest[0]:
        return
    elif num > threeLargest[2]:
        threeLargest[0] = threeLargest[1]
        threeLargest[1] = threeLargest[2]
        threeLargest[2] = num
        return
    elif num > threeLargest[1]:
        threeLargest[0] = threeLargest[1]
        threeLargest[1] = num
        return
    elif num > threeLargest[0]:
        threeLargest[0] = num
        return


array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
largestThree = findThreeLargest(array)
