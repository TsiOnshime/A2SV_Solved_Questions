class Solution:
    def findMinInsertions(self, s):
        
        
        # abcd
        # dcba
        
        n = len(s)
        t = s[::-1]
        palindrome = 0
        dp = [[float('-inf')] * (n + 1) for _ in range(n + 1)]
        
        for i in range(n + 1):
            dp[i][0] = 0
            dp[0][i] = 0
        
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                
                palindrome = max(palindrome, dp[i][j])
                
        return n - palindrome
                        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna