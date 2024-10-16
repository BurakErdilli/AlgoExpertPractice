class Solution:
    def summaryRanges(self, nums):
        subArray = []
        result = []
        if not nums:  # Handle the empty input case
            return []
        if len(nums) == 1:
            result.append(f"{nums[0]}")
            return result

        for i in range(1, len(nums)):
            subArray.append(nums[i-1])
            if nums[i-1]+1 != nums[i]:
                if len(subArray) == 1:
                    result.append(str(subArray[0]))
                else:
                    result.append(f"{subArray[0]}->{subArray[-1]}")
                subArray = []
            if i == len(nums)-1:
                subArray.append(nums[i])
                if len(subArray) == 1:
                    result.append(str(subArray[0]))
                else:
                    result.append(f"{subArray[0]}->{subArray[-1]}")

        return result


obj = Solution()
nums = [1]
result = obj.summaryRanges(nums)
print(result)
