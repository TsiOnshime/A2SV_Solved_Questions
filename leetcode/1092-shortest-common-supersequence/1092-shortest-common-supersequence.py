class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 0
        for j in range(m + 1):
            dp[0][j] = 0
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = 0 + max(dp[i - 1][j], dp[i][j - 1])


        ans = []
        i, j = n, m
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                ans.append(str1[i - 1])
                print(str1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    print(str1[i - 1])
                    ans.append(str1[i - 1])
                    i -= 1
                else:
                    ans.append(str2[j - 1])
                    j -= 1
        if i > 0:
            ans.append(str1[:i])
        if j > 0:
            ans.append(str2[:j])
        return "".join(reversed(ans))
        



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna