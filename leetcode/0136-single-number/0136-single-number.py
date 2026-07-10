class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for i in range(len(nums)):
            number ^= nums[i]
        return number

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna