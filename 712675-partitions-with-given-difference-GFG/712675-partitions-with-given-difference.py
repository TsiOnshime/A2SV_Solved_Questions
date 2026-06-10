class Solution:
    def countPartitions(self, arr, diff):
        # code here
        
        # s1 + s2 = total
        # s1 - s2 = d
        # s1 = d + s2
        # d + 2s2 = total
        # s2 = (total - d) // 2
        total = sum(arr)
        if total < diff or (total- diff) % 2:
            return 0
        n = len(arr)
        target = (total - diff) // 2
        dp = [[0] * (target + 1) for i in range(n)]
        
        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            
        if arr[0] != 0 and arr[0] <= target:
            dp[0][arr[0]] = 1
            
        for i in range(1, n):
            for t in range(target + 1):
                notake = dp[i - 1][t]
                take = 0 
                if arr[i] <= t:
                    take = dp[i - 1][t - arr[i]]
                dp[i][t] = take + notake
                
        return dp[n - 1][target]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna