class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        new_nums = [0] * len(nums)
        current = 0
        for i in range(len(nums)):
            new_nums[i] = current + nums[i]
            current += nums[i]
        startValue = min(new_nums) - 1
        if startValue >= 0:
            return 1
        else:
            return abs(startValue)