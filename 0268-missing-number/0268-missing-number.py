class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        missing = n
        for i in range(n):
            missing ^= i ^ nums[i]

        return missing


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna