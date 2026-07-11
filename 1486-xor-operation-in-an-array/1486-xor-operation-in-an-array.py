class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        xor = 0

 
        i = 0

        while i < n:
            num = start + 2 * i
            xor ^= num
            i += 1
        return xor

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna