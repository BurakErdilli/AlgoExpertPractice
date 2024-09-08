def productSum(array, m=1):
    total = 0
    for i in array:
        if type(i) is int:
            total += i
        else:
            total += productSum(i, m+1)
    return total*m


# Example
array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
a = productSum(array)
