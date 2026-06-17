class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[-1] * (n + 1) for _ in range(n + 1)]

        def calcLength(i, prev_idx):
            if i == n:
                return 0
            if dp[i][prev_idx + 1] != -1:
                return dp[i][prev_idx + 1]
            # take
            take = 0
            if prev_idx == -1 or nums[i] > nums[prev_idx]:
                take = 1 + calcLength(i + 1, i)
            # notake
            notake = calcLength(i + 1, prev_idx)
            val = max(take, notake)
            dp[i][prev_idx + 1] = val
            return val

        return calcLength(0, -1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna