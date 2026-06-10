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
        dp = [[-1] * (target + 1) for i in range(n)]
        def countSubset(i, target):
            if i == 0:
                if target == 0 and arr[i] == 0:
                    return 2
                if target == 0 or arr[i] == target:
                    return 1
                return 0
            if dp[i][target] != -1:
                return dp[i][target]
            
            notake = countSubset(i - 1, target)
            take = 0
            if target >= arr[i]:
                take = countSubset(i - 1, target - arr[i])
            val = notake + take
            dp[i][target] = val
            return val
            
        return countSubset(n - 1, target)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna