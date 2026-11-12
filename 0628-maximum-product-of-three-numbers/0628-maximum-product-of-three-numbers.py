class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        if nums[-1] < 0:
         
            return nums[-1] * nums[-2] * nums[-3]
        if nums[0] < 0 and nums[1] < 0:
            if nums[0] * nums[1] > nums[-2] * nums[-3]:
                return nums[0] * nums[1] * nums[-1]
        return nums[-1] * nums[-2] * nums[-3]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna