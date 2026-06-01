class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {}
        def triSum(n):
            if n == 0: return 0
            if n == 1: return 1
            if n == 2: return 1
            if n in cache: return cache[n]

            val = triSum(n - 3) + triSum(n - 2) + triSum(n - 1)
            cache[n] = val
            return val
        
        return triSum(n)


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna