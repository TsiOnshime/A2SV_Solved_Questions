class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            for j in range(-1, i):
                # take
                take = 0
                if j == -1 or nums[i] > nums[j]:
                    take = 1 + dp[i + 1][i + 1]
                # notake
                notake = dp[i + 1][j + 1]
                val = max(take, notake)
                dp[i][j + 1] = val   
        return dp[0][0]           
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna