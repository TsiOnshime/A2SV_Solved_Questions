class Solution:
    def findComplement(self, num: int) -> int:
        res = 0
        temp = num
        count = 0
        while num:
            num >>= 1
            count += 1

        mask = (1 << count) - 1
        return temp ^ mask


    
    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna