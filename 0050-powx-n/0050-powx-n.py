class Solution:
    def myPow(self, x: float, n: int) -> float:
        
    
        
        def power(x, n):
            if n == 0:
                return 1.0
            
            half = power(x, n // 2)
            result = half * half

            if n % 2:
                result *= x
            return result
        res = power(x, abs(n))
        return res if n > 0 else 1 / res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna