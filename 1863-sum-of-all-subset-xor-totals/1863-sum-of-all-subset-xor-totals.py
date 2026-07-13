class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        mask = 0
        for n in nums:
            mask |= n
        return mask * (2**(len(nums)))//2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna