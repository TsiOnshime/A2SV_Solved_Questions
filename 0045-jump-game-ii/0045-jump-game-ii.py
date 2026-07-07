class Solution:
    def jump(self, nums: List[int]) -> int:
            dp = [-1] * len(nums)

            def min_jump(i):
                if i >= len(nums) - 1:
                    return 0
                if dp[i] != -1:
                    return dp[i]

                
                minimum = float('inf')
                for j in range(1,nums[i] + 1):
                    minimum = min(minimum, 1 + min_jump(i + j))

                dp[i] = minimum
                return minimum

            return min_jump(0)



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna