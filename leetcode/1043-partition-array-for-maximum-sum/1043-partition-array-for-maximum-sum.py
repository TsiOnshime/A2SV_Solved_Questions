class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        dp = [-1] * (len(arr) + 1)
        dp[len(arr)] = 0
        for i in range(len(arr) - 1, -1, -1):
            max_sum = float('-inf')
            curr_max = 0
            for j in range(i, len(arr)):
                if j - i + 1 <= k:
                    curr_max = max(curr_max, arr[j])
                    _sum = (j - i + 1) * curr_max + dp[j + 1]
                    max_sum = max(max_sum, _sum)
            dp[i] = max_sum
        return dp[0]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna