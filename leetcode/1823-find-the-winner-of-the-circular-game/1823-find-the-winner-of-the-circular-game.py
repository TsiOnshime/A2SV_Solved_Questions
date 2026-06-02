class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        def helper(n, k):
            if n == 0:
                return 0

            return (helper(n - 1, k) + k) % n

        return helper(n,k) + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna