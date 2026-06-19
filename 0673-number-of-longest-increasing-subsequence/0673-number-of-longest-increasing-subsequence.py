class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # [1,3,5,4,7]

        # dp = [1, 2, 3, 3, 4]
        #cnt = [1, 1, 1, 1, 2]
        n = len(nums)
        dp = [1] * n
        count = [1] * n
        maxi = 0
        _max = float('-inf')

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
            
            if dp[i] > dp[maxi]:
                maxi = i

        res = 0
        for i in range(n):
            if dp[i] == dp[maxi]: res += count[i]

        return res     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna