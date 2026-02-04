class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        maximum = max(nums)
        minimum = min(nums)

        for i in range(minimum, maximum):
            if i not in nums:
                return i
        return maximum + 1