class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # if the strings match / ? decrement i and j
        # if they don't match and the p[j] == * treat that * as empty and move j - 1 or treat * as sequence of characters and move i - 1 but if they don't match and p[j] != * return False

        dp = [[float('inf')] * (len(p) + 1) for _ in range(len(s) + 1)]
        dp[0][0] = True
        for i in range(1, len(s) + 1):
            dp[i][0] = False
        
        for j in range(1, len(p) + 1):
            flag = True
            for k in range(j):
                if p[k] != "*":
                    flag = False
            dp[0][j] = flag

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):

                if s[i - 1] == p[j - 1] or p[j - 1] == "?":
                    dp[i][j] =  dp[i - 1][j - 1]
                else:
                    if p[j - 1] != "*":
                        dp[i][j] = False
                    else:
                        dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        return dp[len(s)][len(p)]
                        

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