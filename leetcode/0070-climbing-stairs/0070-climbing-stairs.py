class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        # without memoization
        def climb(n):
            if n == 1: return 1
            if n == 2: return 2
            if n in cache:
                return cache[n]

            val = climb(n - 1) + climb(n - 2)
            cache[n] = val

            return val

        return climb(n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna