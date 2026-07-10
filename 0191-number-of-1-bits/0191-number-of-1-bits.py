class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            count += 1 if n & (1 << i) else 0
        
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna