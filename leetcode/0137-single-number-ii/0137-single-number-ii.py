class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 1
        while i < len(nums):
            if nums[i] != nums[i - 1]:
                return nums[i-1]
            i += 3
        return nums[len(nums) - 1]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna