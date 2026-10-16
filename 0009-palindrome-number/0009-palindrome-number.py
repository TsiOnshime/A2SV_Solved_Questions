class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        r = 0
        while x > 0:
            r = (r * 10) + (x % 10)
            x //= 10
        
        return r == n


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna