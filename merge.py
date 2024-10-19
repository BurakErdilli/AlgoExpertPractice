class Solution:
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort()  # Sort by the first element of each interval

        result = []
        sub = intervals[0]  # Start with the first interval

        for i in range(1, len(intervals)):
            # Check if current interval overlaps with sub
            if intervals[i][0] <= sub[-1]:  # Overlapping intervals
                # Merge intervals by updating the end of the current interval
                sub = [sub[0], max(sub[-1], intervals[i][-1])]
            else:
                # If no overlap, add the previous sub interval to the result
                result.append(sub)
                sub = intervals[i]  # Move to the next interval

        # Append the last interval
        result.append(sub)

        return result


obj = Solution()

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

result = obj.merge(intervals)
print(result)
