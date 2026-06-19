class Solution:
    def numberofLIS(self, nums):
        
        n = len(arr)
        dp = [1] * n
        count = [1] * n
        maxi = 0
        _max = set()
        
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 == dp[i]:
                        count[i] += count[j]
                    elif dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                        dp[i] = dp[j] + 1
            if dp[i] > dp[maxi]:
                maxi = i
                _max = {maxi}
            elif dp[i] == dp[maxi]:
                _max.add(i)
                
        res = 0
        for i in _max:
            res += count[i]
            
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna