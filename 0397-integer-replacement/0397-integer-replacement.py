class Solution:
    def integerReplacement(self, n: int) -> int:
        def find_min(n):
            if n == 1:
                return 0
            if n < 1:
                return float('inf')

            if n % 2 == 0:
                cnt = 1 + find_min(n // 2)
            else:
                cnt = min(1 + find_min(n + 1), 1 + find_min(n - 1))

            return cnt

        return find_min(n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna