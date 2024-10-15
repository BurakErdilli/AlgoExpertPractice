class Solution:
    def jump(self, array):
        i = 0
        counter = 0

        while i < len(array) - 1:
            if array[i] >= len(array) - i - 1:
                return counter + 1

            # Find the next optimal jump
            max_reach = 0
            next_index = i
            for j in range(1, array[i] + 1):
                if i + j >= len(array) - 1:
                    return counter + 1
                if array[i + j] + j > max_reach:
                    max_reach = array[i + j] + j
                    next_index = i + j

            i = next_index
            counter += 1

        return counter
