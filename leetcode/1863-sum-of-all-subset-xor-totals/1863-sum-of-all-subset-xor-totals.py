class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor = 0
        subsets = 1 << len(nums)

        for number in range(subsets):
            subset_xor = 0
            for i in range(len(nums)):
                if number & (1 << i):
                    subset_xor ^= nums[i]
            xor += subset_xor

        return xor

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna