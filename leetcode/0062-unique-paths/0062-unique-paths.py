class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cols = [1] * m

        for i in range(1, n):
            for j in range(1, m):
                cols[j] = cols[j] + cols[j - 1]

        
        return cols[-1]

        # [1, 1, 1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna