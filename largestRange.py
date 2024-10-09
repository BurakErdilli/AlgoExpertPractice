def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}

    for i in array:
        nums[i] = True

    for i in array:
        if not nums[i]:
            continue
        nums[i] = False
        currentLenght = 1
        left = i-1
        right = i+1
        while left in nums:
            nums[left] = False
            currentLenght += 1
            left -= 1

        while right in nums:
            nums[right] = False
            currentLenght += 1
            right += 1

        if currentLenght > longestLength:
            longestLength = currentLenght
            bestRange = [left+1, right-1]

    return bestRange


array = [1, 3, 5, 6, 7, 8, 9, 10]
a = largestRange(array)
