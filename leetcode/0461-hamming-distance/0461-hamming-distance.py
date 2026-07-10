class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y 
        count = 0
        while ans:
            count += ans & 1
            ans >>= 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna