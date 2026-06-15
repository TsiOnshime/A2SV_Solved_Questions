class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)
        dp = [[float('-inf')]*(n + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp[0][i] = 0
        for j in range(n + 1):
            dp[j][0] = 0
        def lcs(s, t):

            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if s[i - 1] == t[j - 1]:
                        dp[i][j] = 1 + dp[i -1][j - 1]
                    else:
                        dp[i][j] = 0 + max(dp[i - 1][j], dp[i][j - 1])
        
        lcs(s, t)
        # print(dp)
        ################ Print Palindrom ##############
        # i = j = n
        # ans = []
        # while i > 0 and j > 0:
        #     if s[i - 1] == t[j - 1]:
        #         ans.append(s[i - 1])
        #         i -= 1
        #         j -= 1
        #     else:
        #         if dp[i - 1][j] > dp[i][j - 1]:
        #             i -= 1
        #         else:
        #             j -= 1
        # ans = "".join(reversed(ans))
        return dp[n][n]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna