class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        count = 0
        while n: 
            count += n & 1
            n = n >> 1
            if count > 1:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna