class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            index = nums[i] - 1
            if nums[i] < 1 or nums[i] > len(nums) or nums[index] == nums[i]:
                i += 1
            elif 1 <= nums[i] <= len(nums):
                index = nums[i] - 1
                nums[i], nums[index] = nums[index], nums[i]


        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna