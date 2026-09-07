class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            res = power(x, n // 2)
            res = res * res

            return x * res if n % 2 else res
        

        res = power(x, abs(n))

        return res if n >= 0 else 1/ res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna