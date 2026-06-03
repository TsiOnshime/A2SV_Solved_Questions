class Solution:
    def rob(self, nums: List[int]) -> int:
        
        dp = [-1] * len(nums)
        def robbery(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            if dp[i] != -1:
                return dp[i]

            pick = nums[i] + robbery(i - 2)
            noPick = robbery(i - 1)

            val = max(pick, noPick)

            dp[i] = val

            return val


        
        return robbery(len(nums) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna