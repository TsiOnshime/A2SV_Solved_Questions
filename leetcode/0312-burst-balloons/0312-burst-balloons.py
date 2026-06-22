class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums.insert(0,1)
        nums.append(1)
        dp = [[0] * (len(nums) + 1) for _ in range(len(nums) + 1)]

        
        for i in range(len(nums) - 2, 0, -1):
            for j in range(1, len(nums) - 1):
                if i > j:
                    continue
                maxi = float('-inf')
                for k in range(i, j + 1):
                    op = nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j]
                    maxi = max(maxi, op)
                dp[i][j] = maxi

        return dp[1][len(nums) - 2]

        #    i     j
        # [1,3,1,5,8,1]
        # op = 1*3*1 + (0,0) + (2,4)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna