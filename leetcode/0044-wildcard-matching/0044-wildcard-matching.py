class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if the strings match / ? decrement i and j
        # if they don't match and the p[j] == * treat that * as empty and move j - 1 or treat * as sequence of characters and move i - 1 but if they don't match and p[j] != * return False

        dp = [[float('inf')] * len(p) for _ in range(len(s))]
        def matchPattern(i, j):
            if i < 0 and j < 0:
                return True
            if i >= 0 and j < 0:
                return False
            if i < 0 and j >= 0:
                for i in range(0, j + 1):
                    if p[i] != "*":
                        return False
                return True
            
            if dp[i][j] != float('inf'):
                return dp[i][j]


            if s[i] == p[j] or p[j] == "?":
                dp[i][j] =  matchPattern(i - 1, j - 1)
            else:
                if p[j] != "*":
                    return False
                else:
                    dp[i][j] = matchPattern(i, j - 1) or matchPattern(i - 1, j)
                
            return dp[i][j]


        return matchPattern(len(s) - 1, len(p) - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna