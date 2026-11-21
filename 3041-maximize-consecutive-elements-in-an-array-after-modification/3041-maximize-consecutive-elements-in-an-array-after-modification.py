class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()
        dp = [0] * (max(nums) + 2)
        # print(nums)
        # print(dp)

        # num = [1, 1, 1, 2, 5]
        # dp = [0, 1, 2, 0, 0, 0]
        # i = 0

        for i in range(len(nums)):
            dp[nums[i] + 1] = dp[nums[i]] + 1
            dp[nums[i]] = dp[nums[i] - 1] + 1
        
        return max(dp)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna