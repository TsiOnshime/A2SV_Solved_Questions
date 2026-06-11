class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [0] * len(arr)

        dp[0] = 1
        if len(set(arr)) == 1:
            return 1

        def calculateSize(i):
            nonlocal dp
            if i >= len(arr) - 1:
                return 
            # turbulent
            if arr[i - 1] > arr[i] < arr[i + 1] or arr[i - 1] < arr[i] > arr[i + 1]:
                dp[i] = dp[i - 1] + 1
      
            else:
                dp[i] = 1
            
            calculateSize(i + 1)

        calculateSize(1)

        ans = max(dp) + 1
        return ans

# 8 < 12 < 16
# [1, 2, 1, 0]
# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna