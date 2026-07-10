class Solution:
    def reverseBits(self, n: int) -> int:
        res = []
        for i in range(32):
            if n & (1 << i) != 0:
                
                res.append((2) ** (31 - i))
        return sum(res)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna