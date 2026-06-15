class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        t = s[::-1]
        n = len(s)

        prev = [0] * (n + 1)
        curr = [0] * (n + 1)

        def lcs(s, t):
            nonlocal prev
            nonlocal curr

            for i in range(1, n + 1):
                for j in range(1, n + 1):
                    if s[i - 1] == t[j - 1]:
                        curr[j] = 1 + prev[j - 1]
                    else:
                        curr[j] = 0 + max(prev[j], curr[j - 1])
                prev = curr.copy()
        
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
        return prev[n]
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna