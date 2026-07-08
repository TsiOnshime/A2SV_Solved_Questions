class Solution:
    def checkValidString(self, s: str) -> bool:
        dp = [[float('-inf')]*len(s) for _ in range(len(s))]

        def is_valid(i, count):
            if count < 0:
                return False
            if i == len(s):
                return count == 0
            if dp[i][count] != float('-inf'):
                return dp[i][count]

            if s[i] == "(":
                dp[i][count] = is_valid(i + 1, count + 1)
                return dp[i][count]
            elif s[i] == ")":
                dp[i][count] = is_valid(i + 1, count - 1)
                return dp[i][count]
            else:
                dp[i][count] = is_valid(i + 1, count + 1) or is_valid(i + 1, count) or is_valid(i + 1, count - 1)
                return dp[i][count]


        return is_valid(0, 0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna