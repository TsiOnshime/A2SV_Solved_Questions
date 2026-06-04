class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # down = m - 1
        # left = n - 1
        # total moves = n - 1 + m - 1 = n + m - 2

        # c(total, min(down, left))

        #   6 * 5  
        #   _____
        #   2 * 1

        ans = 1

        total = n + m - 2
        choose = min(m - 1, n - 1)

        for i in range(1, choose + 1):
            numerator = total - choose + i
            ans *= numerator
            ans //= i

        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna