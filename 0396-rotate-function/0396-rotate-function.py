class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        numSum = 0
        prev = 0
        n = len(nums)
        

        for i in range(n):
            numSum += nums[i]
            prev += (i * nums[i])

        maxValue = prev
        
        for i in range(1, n):
            f = prev + numSum - (n * nums[n - i])
            prev = f
            maxValue = max(maxValue, f)

        return maxValue


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna