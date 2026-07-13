class Solution:
    def findXOR(self, l, r):
        # code here

        def xor(n):
            if n % 4 == 0:
                return n
            if n % 4 == 1:
                return 1
            if n % 4 == 2:
                return n + 1
            return 0
        
        return xor(l - 1) ^ xor(r)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna