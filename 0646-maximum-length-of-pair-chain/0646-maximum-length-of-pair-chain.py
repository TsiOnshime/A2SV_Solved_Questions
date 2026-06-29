class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x:x[1])
        dp = [[0] * (len(pairs) + 1) for _ in range(len(pairs) + 1)]

        max_length = 0

        for i in range(len(pairs) - 1, -1, -1):
            for j in range(-1, len(pairs)):
                take = 0 
                if j == -1 or pairs[j][1] < pairs[i][0]:
                    take = 1 + dp[i + 1][i + 1]
                notake = dp[i + 1][j + 1]
                dp[i][j + 1] = max(take, notake)

        for i in range(len(pairs)):
            max_length = max(max_length, dp[i][0])
        return max_length

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna